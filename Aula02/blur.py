import cv2

# Carregar a imagem
imagem = cv2.imread("imagem.jpg")

# Aplicar filtro de média (blur normal)
imagem_blur = cv2.blur(imagem, (5, 5))

# Aplicar filtro Gaussiano
imagem_gauss = cv2.GaussianBlur(imagem, (5, 5), 0)

# Aplicar filtro Mediana
imagem_mediana = cv2.medianBlur(imagem, 5)

# Mostrar as imagens
cv2.imshow("Filtro Blur", imagem_blur)
cv2.imshow("Filtro Gaussiano", imagem_gauss)
cv2.imshow("Filtro Mediana", imagem_mediana)

# Salvar as imagens processadas
cv2.imwrite("imagem_blur.jpg", imagem_blur)
cv2.imwrite("imagem_gauss.jpg", imagem_gauss)
cv2.imwrite("imagem_mediana.jpg", imagem_mediana)

cv2.waitKey(0)
cv2.destroyAllWindows()

