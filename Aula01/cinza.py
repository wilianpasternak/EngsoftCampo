import cv2

# Carregar a imagem em escala de cinza (8 bits)
imagem = cv2.imread("imagem.png", cv2.IMREAD_GRAYSCALE)

# Salvar a imagem convertida
cv2.imwrite("imagem_convertida.jpg", imagem)

# Exibir a imagem original e a convertida
cv2.imshow("Imagem em Escala de Cinza", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()

