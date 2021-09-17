#################################################
#################################################
##TextDetection Using OpenCV2 and Tessearact-OCR
##################################################
##################################################

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('test.png')

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#################Detecting Characters################
# H_Image, W_Image,_ = img.shape
# conf = r' --oem 3 --psm 11 outputbase text'
# boxes = pytesseract.image_to_boxes(img, config=conf)
# for b in boxes.splitlines():
#         b = b.split(' ')
#         print(b)
#         x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
#         cv2.rectangle(img, (x, H_Image-y), (w,H_Image-h), (50, 50, 255), 3)
#         cv2.putText(img, b[0], (x, H_Image-y+25), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)

#####Detecting Words ############################
# H_Image, W_Image,_ = img.shape
# conf = r' --oem 3 --psm 11 outputbase text'
# boxes = pytesseract.image_to_data(img, config=conf)
# for x, b in enumerate(boxes.splitlines()):
#     if x!=0:
#         b = b.split()
#         print(b)
#         if len(b)==12:
#             x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
#             cv2.rectangle(img, (x, y), (x +w,y + h), (50, 50, 255), 3)
#             cv2.putText(img, b[11], (x + 25, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)

###############Detecting only digits######################
# H_Image, W_Image,_ = img.shape
# conf = r' --oem 3 --psm 6 outputbase digits'
# boxes = pytesseract.image_to_data(img, config=conf)
# for x, b in enumerate(boxes.splitlines()):
#     if x!=0:
#         b = b.split()
#         print(b)
#         if len(b)==12:
#             x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
#             cv2.rectangle(img, (x, y), (x +w,y + h), (50, 50, 255), 3)
#             cv2.putText(img, b[11], (x + 25, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)

##################Detecting only Alpahbets####################
H_Image, W_Image,_ = img.shape
conf = r'-c tessedit_char_blacklist=0123456789 --psm 6'
boxes = pytesseract.image_to_data(img, config=conf)
for x, b in enumerate(boxes.splitlines()):
    if x!=0:
        b = b.split()
        print(b)
        if len(b)==12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x, y), (x +w,y + h), (50, 50, 255), 3)
            cv2.putText(img, b[11], (x + 25, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)
cv2.imshow('img', img)
cv2.waitKey(0)
