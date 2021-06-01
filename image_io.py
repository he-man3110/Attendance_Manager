import cv2
import os
import glob
import time


def capture_query():
    camera = cv2.VideoCapture(0)
    for i in range(3):
        time.sleep(2)
        return_value, image = camera.read()
        path = 'C:/Users/User/PycharmProjects/myproject/unknown'
        cv2.imwrite(os.path.join(path, 'opencv'+str(i)+'.jpeg'), image)
    del(camera)


def delete_query():
    files = glob.glob(os.path.join(
        'C:/Users/User/PycharmProjects/myproject/unknown', "*.jpeg"))
    for f in files:
        os.remove(f)

def dpresize(image):
    #image = cv2.imread("D:/Dev/Python/PyQT/AM/res/Admin.jpg")
    scale = 20
    h = int(image.shape[0]*scale/100)
    w = int(image.shape[1]*scale/100)
    dim = (w, h)
    rimage = cv2.resize(image, dim, cv2.INTER_AREA)
    return rimage
    #cv2.imshow("Resized", rimage)
    #cv2.imshow("original", image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()



if __name__ == "__main__":
    dpresize()
