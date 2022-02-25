


#Segmentaçaõ dos três canais deuma imagem em RGB em três imagens distintas

from unittest import TextTestRunner
import cv2 as cv
import os #sistema operacional 
import numpy as np


def busca_na_pasta(directoryPath):

    if os.path.exists(directoryPath):
        #print("Existe o diretório")
        print(len(os.listdir(directoryPath)))
        print(os.listdir(directoryPath))
        if len(os.listdir(directoryPath)) == 0:
            return True
        else:
            return False
    else:
        return False            


#declaração das variávei:
path = r"C:\Users\aa\Desktop\caixeiro viajante\imagens_main3" # f antes da string se chama fstring

#caregando as imagens esegmentnso canais
imagem = cv.imread("frutas.png")
azul, verde, vermelho = cv.split(imagem)



#Exibindo imagens doscans separados
cv.imshow("Canal R", vermelho)
cv.imshow("Canal G", verde)
cv.imshow("Canal B", azul)

#Salvando imagens dos canais seprados
print(busca_na_pasta(path))
if(busca_na_pasta(path)):
    
    #print(azul)
    np.savetxt("./imagens_main3/azul.txt", azul) #salva como txt (nomw do arquivo, arquivo)
    #print(verde)
    np.savetxt("./imagens_main3/verde.txt", verde) #salva como txt (nomw do arquivo, arquivo)
    #print(vermelho)
    np.savetxt("./imagens_main3/vermelho.txt", vermelho) #salva como txt (nomw do arquivo, arquivo)
    
    cv.imwrite("./imagens_main3/fruta-canal-vermelho.png", vermelho)
    cv.imwrite("./imagens_main3/fruta-canal-verde.png",verde)
    cv.imwrite("./imagens_main3/fruta-canal-zul.png",azul)


#cv.imshow("futas", imagem)
cv.waitKey(0)
cv.destroyAllWindows()
