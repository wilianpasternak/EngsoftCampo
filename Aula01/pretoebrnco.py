import cv2

# Carregar a imagem em escala de cinza
imagem = cv2.imread("imagem.png", cv2.IMREAD_GRAYSCALE)

# Aplicar a binarização (Thresholding)
_, imagem_bin = cv2.threshold(imagem, 160, 255, cv2.THRESH_BINARY)

# Salvar e exibir a imagem binarizada
cv2.imwrite("imagem_binarizada.jpg", imagem_bin)
cv2.imshow("Imagem Binarizada", imagem_bin)
cv2.waitKey(0)
cv2.destroyAllWindows()
