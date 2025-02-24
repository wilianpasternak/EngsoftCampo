import cv2

# Carregar a imagem
imagem = cv2.imread("imagem.jpg", cv2.IMREAD_GRAYSCALE)

# Aplicar filtro Sobel
sobelx = cv2.Sobel(imagem, cv2.CV_64F, 1, 0, ksize=5)  
sobely = cv2.Sobel(imagem, cv2.CV_64F, 0, 1, ksize=5)

# Aplicar filtro Laplaciano
laplaciano = cv2.Laplacian(imagem, cv2.CV_64F)

# Aplicar filtro Canny
bordas_canny = cv2.Canny(imagem, 50, 150)

# Mostrar as imagens
cv2.imshow("Sobel X", sobelx)
cv2.imshow("Sobel Y", sobely)
cv2.imshow("Laplaciano", laplaciano)
cv2.imshow("Canny", bordas_canny)

# Salvar as imagens processadas
cv2.imwrite("sobelx.jpg", sobelx)
cv2.imwrite("sobely.jpg", sobely)
cv2.imwrite("laplaciano.jpg", laplaciano)
cv2.imwrite("bordas_canny.jpg", bordas_canny)

cv2.waitKey(0)
cv2.destroyAllWindows()

