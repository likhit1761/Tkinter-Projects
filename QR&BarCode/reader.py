import cv2
from pyzbar import pyzbar as pb
import webbrowser
import requests

file_saved = "barcode_results.txt"
font = cv2.FONT_HERSHEY_DUPLEX


def open_site(url):
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
        "C:\Program Files\Google\Chrome\Application\chrome.exe"))
    webbrowser.get('chrome').open_new(url)
    return


def barcode_reading(frame):
    barcodes = pb.decode(frame)
    for element in barcodes:
        x_cor, y_cor, wid, hig = element.rect
        barcode_data = element.data.decode('utf-8')
        cv2.rectangle(frame, (x_cor, y_cor), (x_cor + wid, y_cor + hig), (0, 255, 0), 2)
        cv2.putText(frame, barcode_data, (x_cor + 6, y_cor - 6), font, 1.0, (255, 255, 255), 1)
        edit = open(file_saved, 'w')
        with edit as file:
            file.write("Recognized barcode data as : " + barcode_data)
    return frame


def main():
    cam = cv2.VideoCapture(0)
    x, screen = cam.read()
    while x:
        x, screen = cam.read()
        screen = barcode_reading(screen)
        cv2.imshow('code_reader', screen)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cam.release()
    cv2.destroyAllWindows()


def open_link():
    main()
    handle = open(file_saved, 'r')
    for line in handle:
        print(line)
        idx = line.index(":")
        site = line[idx + 2:]
    handle.close()
    return site


url = open_link()
print("Encoded data : ", url)
try:
    response = requests.get(url)
    print("URL exists")
    open_site(url)
except requests.ConnectionError or requests.exceptions.MissingSchema as Exception:
    print("The data of the code is not a valid search URL")
