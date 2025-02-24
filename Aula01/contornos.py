import cv2

# Carregar a imagem em escala de cinza
imagem = cv2.imread("imagem.png", cv2.IMREAD_GRAYSCALE)

# Aplicar um desfoque para reduzir ruídos
imagem_suavizada = cv2.GaussianBlur(imagem, (5, 5), 0)

# Aplicar a detecção de bordas com Canny
bordas = cv2.Canny(imagem_suavizada, 30, 100)

# Encontrar contornos na imagem
contornos, _ = cv2.findContours(bordas, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Carregar a imagem original para desenhar os contornos
imagem_colorida = cv2.imread("imagem.png")

# Desenhar os contornos na imagem
cv2.drawContours(imagem_colorida, contornos, -1, (0, 255, 0), 2)

# Salvar e exibir a imagem com contornos
cv2.imwrite("imagem_contornos.jpg", imagem_colorida)
cv2.imshow("Contornos Detectados", imagem_colorida)
cv2.waitKey(0)
cv2.destroyAllWindows()

