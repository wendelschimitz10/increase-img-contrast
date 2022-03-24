import cv2
from cv2 import COLOR_BGR2HSV
from cv2 import COLOR_HSV2BGR
from matplotlib import pyplot

img = cv2.imread("img/chaves3.jpeg")

#transformar para hsv
img_hsv = cv2.cvtColor(img, COLOR_BGR2HSV)

#separando os 3 canais
h,s,v = cv2.split(img_hsv)

# MOSTRANDO OS 3 CANAIS
#cv2.imshow("canal Hue",h)
#cv2.imshow("canal Saturation",s)
#cv2.imshow("canal value",v)

# EQUALIZANDO A IMAGEM DO CANAL V
vEqualizada = cv2.equalizeHist(v)

# MOSTRANDO A IMAGEM V EQUALIZADA
#cv2.imshow("V equalizada", vEqualizada)

# CONVERTENDO IMAGE PARA HSV NOVAMENTE JÁ COM O V EQUALIZADO
imageHSVback = cv2.merge((h,s,vEqualizada))
#cv2.imshow("Imagem Equalizada", imageHSVback)

# CONVERTENDO A IMAGEM HSV PARA BGR
imageEqualized = cv2.cvtColor(imageHSVback, COLOR_HSV2BGR)

# SALVANDO A IMAGEM EQUALIZADA
cv2.imwrite("img/chaves3_equaliz.png", imageEqualized)

# MOSTRANDO A IMAGEM ORIGINAL E A IMAGEM EQUALIZADA
cv2.imshow("Imagem Original", img)
cv2.imshow("Imagem equalizada", imageEqualized)

# MOSTRANDO O HISTOGRAMA DA PRIMEIRA IMAGEM COM A ULTIMA FEITA
#pyplot.hist(imageEqualized.ravel(), 255, [0,255])
#pyplot.hist(img.ravel(), 255, [0,255])


pyplot.show()
cv2.waitKey()