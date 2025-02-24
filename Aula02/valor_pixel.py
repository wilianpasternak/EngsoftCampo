import cv2
import numpy as np

# Carregar a imagem
imagem = cv2.imread("imagem.jpg")

# Verificar se a imagem foi carregada corretamente
if imagem is None:
    print("Erro ao carregar a imagem.")
    exit()

# Exibir a imagem
cv2.imshow("Imagem", imagem)

# Obter as dimensões da imagem
altura, largura, canais = imagem.shape
print(f"Dimensões da imagem: {largura}x{altura} com {canais} canais")

# Percorrer cada pixel e mostrar seus valores
for y in range(altura):
    for x in range(largura):
        pixel = imagem[y, x]  # Acessa o pixel na posição (y, x)
        if canais == 3:  # Imagem colorida (BGR)
            print(f"Pixel ({x}, {y}): Azul={pixel[0]}, Verde={pixel[1]}, Vermelho={pixel[2]}")
        else:  # Imagem em escala de cinza
            print(f"Pixel ({x}, {y}): Intensidade={pixel}")

# Aguardar a tecla para fechar a janela
cv2.waitKey(0)
cv2.destroyAllWindows()

