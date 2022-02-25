#link para repositório de vídeos  https://pixabay.com/pt/videos/search/estrada/

import cv2 as cv

captura = cv.VideoCapture("./carros.mp4")

while True:
    ret,frame = captura.read()
    cv.imshow("video", frame)

    if(cv.waitKey(1) & 0xFF == ord("q")):
        break

captura.release()
cv.destroyAllWindows()

