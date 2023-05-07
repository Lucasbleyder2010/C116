import cv2
img=cv2.imread("C:\\Users\\CLIENTE\\Desktop\\Downloads\\imagem_surf.jpg")

cv2.waitKey(0)
cv2.imshow("Surf",img)
print(img)
img_cinza=cv2.cvtColor(img,cv2.COLOR_GRAY)

cv2.putText(img,
                "Sol",
                (100,80),
                cv2.FONT_HERSHEY_COMPLEX,
                2,
                (0,0,255)
                )

cv2.imshow("Image",img_cinza)
cv2.waitKey(0)