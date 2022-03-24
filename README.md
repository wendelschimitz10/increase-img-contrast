#1 code made in the PDI class, to increase the contrast of an image.
Using two Python libraries, called: cv2 and matplotlib.
1) Reading the original image.
2) The image is converted from BGR to HSV, through the lib (cvtColor)
3) The three H.S.V channels are separated through the function (split)
4) Through the function (equalizeHist) the V channel was equalized
5) The three channels are joined again, but now with the V channel equalized. This join is made through the function.
(imageHSVback = cv2.merge((h,s,vEqualized)))
6) The conversion is done again to BGR through the function
(imageEqualized = cv2.cvtColor(imageHSVback, COLOR_HSV2BGR))
7) Finally, this new photo, already altered with the contrast, is saved and the two photos are displayed on the screen.

*Can be shown the histogram of these two photos on screen, just uncomment the following functions: 
#pyplot.hist(imageEqualized.ravel(), 255, [0.255])
#pyplot.hist(img.ravel(), 255, [0.255])
