import cv2
import os

#chars from the brightest to the deepest
ASCII = [' ', '.', ',', ':', ';', '+', '*', '?', '$', '#', '%', '&', '@']

WIDTH = 90
HEIGHT = 45

piece = 255//(len(ASCII)-1) #subdivision of range

def clear():
    cls = 'clear'
    if os.name == 'nt':
        cls = 'cls'
    os.system(cls)

def toAsciiArt(image):
    text = ''
    for line in image:
        for pixel in line:
            text += ASCII[pixel//piece]
        text += '\n'
    return text

def resizeImage(image):
    return cv2.resize(image, (WIDTH, HEIGHT), interpolation = cv2.INTER_AREA)

def toBlackWhite(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def main():
    cv2.namedWindow("preview")

    cam_port = 0
    cam = cv2.VideoCapture(cam_port)

    status = False
    
    if cam.isOpened(): # try to get the first frame
        status, img = cam.read()

    while status:
        status, img = cam.read()

        cv2.imshow("preview", img)
        img = resizeImage(img)
        img = toBlackWhite(img)

        clear()
        print(toAsciiArt(img))

        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            status = False

    cam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
