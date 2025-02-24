import cv2

# Carregar a imagem em escala de cinza
imagem = cv2.imread("imagem.jpg", cv2.IMREAD_GRAYSCALE)

# Criar um kernel para operações morfológicas
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

# Aplicar erosão (reduz áreas brancas)
erosao = cv2.erode(imagem, kernel, iterations=1)

# Aplicar dilatação (expande áreas brancas)
dilatacao = cv2.dilate(imagem, kernel, iterations=1)

# Mostrar as imagens
cv2.imshow("Erosão", erosao)
cv2.imshow("Dilatação", dilatacao)

# Salvar as imagens processadas
cv2.imwrite("imagem_erosao.jpg", erosao)
cv2.imwrite("imagem_dilatacao.jpg", dilatacao)

cv2.waitKey(0)
cv2.destroyAllWindows()

