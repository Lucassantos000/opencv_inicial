
import cv2 as cv

#caregamento imagem RGB e segmentando canais
imagem = cv.imread("frutas.png")
azul, verde, vermelho =cv.split(imagem)

#combinar os três canais em única imagem
cv.imshow("primeira", verde )

'''
AQUI FAÇA AS MANIULAÇÕES COMO DEIXAR AS SEM UM TOM, OU INTENSIFCAR O TOM
azul = azul * 0
verde = verde * 0
vermelho = vermelho * 0
'''
azul = azul * 0

imagem1 = cv.merge((azul, verde, vermelho))  # precisa ter as três tonalidares
cv.imshow("merge", imagem1)

cv.waitKey(0)
cv.destroyAllWindows()
