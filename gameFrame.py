import cv2
import numpy as np
  import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

path = "falcon.mp4"
video = cv2.VideoCapture(path)
count = 0
while (video.isOpened()):
    ret, image = video.read()
    if(ret == 0):
            break
    img = cv2.resize(image,(512,512))
    # player1 = img[430:480, 90:152]

    # img = cv2.resize(player1,(100,100))
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # kernel = np.ones((5,5),np.uint8)
    # img = cv2.dilate(img, kernel, iterations = 1)
    # img = cv2.Canny(img, 100, 200)
    h, w, c = img.shape
    boxes = pytesseract.image_to_boxes(img) 
    for b in boxes.splitlines():
        b = b.split(' ')
        img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
        # cv2.imshow('img', img)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

    cv2.imwrite(".\\game1\\frame%d.jpg" % count, img)
    count += 1
    print(count)
