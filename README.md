#1 code made in the PDI class, to increase the contrast of an image.
Using two Python libraries, called: cv2 and matplotlib.
1) Reading the original image.
```img = cv2.imread("img/chaves3.jpeg")
```
2) The image is converted from BGR to HSV, through the lib (cvtColor)
```img_hsv = cv2.cvtColor(img, COLOR_BGR2HSV)
```
3) The three H.S.V channels are separated through the function (split)
```h,s,v = cv2.split(img_hsv)
```
4) Through the function (equalizeHist) the V channel was equalized
```vEqualizada = cv2.equalizeHist(v)
```
5) The three channels are joined again, but now with the V channel equalized. This join is made through the function.
```imageHSVback = cv2.merge((h,s,vEqualizada))
```
6) The conversion is done again to BGR through the function
```imageEqualized = cv2.cvtColor(imageHSVback, COLOR_HSV2BGR)
```
7) Finally, this new photo, already altered with the contrast, is saved and the two photos are displayed on the screen.
```
cv2.imwrite("img/chaves3_equaliz.png", imageEqualized)

cv2.imshow("Imagem Original", img)
cv2.imshow("Imagem equalizada", imageEqualized)
```

*Can be shown the histogram of these two photos on screen, just uncomment the following functions: 
```
#pyplot.hist(imageEqualized.ravel(), 255, [0.255])
#pyplot.hist(img.ravel(), 255, [0.255])
```
