import cv2

image = cv2.imread("img1.jpg")

h,w,c = image.shape

print("height: {}, width : {}, color : {}".format(h,w,c))


(b,g,r) = image[10,100]


print("red : {}, green : {}, blue : {}".format(r,g,b))

cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
