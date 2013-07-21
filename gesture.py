import cv2

name = ""



def createWindow():
    cv2.namedWindow(name, 1)


def closeWindow():
    cv2.destroyWindow(name)


def openCamera():
    return cv2.VideoCapture(1)


if __name__ == '__main__':
    name = "hello"
    createWindow()
    d = openCamera()

    while(True):
        ret, img = d.read()
        cv2.imshow(name, img)
        if (cv2.waitKey(1) > 0):
            break
