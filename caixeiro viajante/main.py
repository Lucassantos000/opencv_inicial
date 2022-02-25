#link de videos para estrada: https://pixabay.com/pt/videos/search/estrada/

import cv2

cv2.namedWindow('show')
img = cv2.imread('campo_color.png')
cv2.imshow('show',img)
cv2.waitKey(1000)
cv2.destroyWindow('show')
