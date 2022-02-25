'''
https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbi1zNXBLaFBJTTRKNlZjYi1QM1lzMHR6Mk9Yd3xBQ3Jtc0tuUk1tMUVzZzVFYl83YV9WMnhldVl5Q3pEc2h6ODk3bERyMXN0WUlTLXpUQzJQOERwN3FVTURsc0FEUTBRWTMydVB3NjZPTmdNYmNqQzIzZ2dkYkpRdXZKNzRvSVBJcFNLNmhUM2Ztd0FTOW1maFpwTQ&q=https%3A%2F%2Fbit.ly%2FIPWebcamPC - ipwbcan para pc

1º baixar no comptador o ipcan 
2º baixar no celular o ipcan
3º conectar celular no computador via usb
4º Ativar a ancoragem de internet  via usb 
5º inciar o ipcon (start server )
6º copiar o ipv4 (que aprece na tela do celular durante a gravação )  
7º colar no browser e escolher  a opção (javascript ou browser para rodar o app)

'''


#capturar imagens via  webCan

import cv2 as cv  #importando a biblioteca opencv e dando-lhe o apelido de cv

captura = cv.VideoCapture(0)

print(captura)

while True:
    ret, frame = captura.read()
    print(ret)
    print(frame)
    cv.imshow("can", frame)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

captura.release()
cv.destroyAllWindows()