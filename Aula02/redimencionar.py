import cv2

# Carregar a imagem
imagem = cv2.imread("imagem.jpg")

# Verificar se a imagem foi carregada corretamente
if imagem is None:
    print("Erro ao carregar a imagem.")
    exit()

# Obter as dimensões originais da imagem
altura, largura = imagem.shape[:2]
print(f"Dimensões originais: {largura}x{altura}")

# Definir novas dimensões (exemplo: 50% do tamanho original)
largura_nova = int(largura * 0.5)
altura_nova = int(altura * 0.5)
dimensoes = (largura_nova, altura_nova)

# Redimensionar a imagem
imagem_redimensionada = cv2.resize(imagem, dimensoes, interpolation=cv2.INTER_AREA)

# Exibir as imagens
cv2.imshow("Imagem Original", imagem)
cv2.imshow("Imagem Redimensionada", imagem_redimensionada)

# Salvar a imagem redimensionada
cv2.imwrite("imagem_redimensionada.jpg", imagem_redimensionada)

# Aguardar uma tecla para fechar as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()

