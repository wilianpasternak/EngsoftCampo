import cv2
import numpy as np

# Carregar a imagem
imagem = cv2.imread("imagem.jpg")

# Criar um kernel de nitidez
kernel_nitidez = np.array([[0, -1, 0], 
                           [-1, 5,-1], 
                           [0, -1, 0]])

# Aplicar filtro de nitidez
imagem_nitida = cv2.filter2D(imagem, -1, kernel_nitidez)

# Mostrar a imagem
cv2.imshow("Filtro de Nitidez", imagem_nitida)

# Salvar a imagem processada
cv2.imwrite("imagem_nitida.jpg", imagem_nitida)

cv2.waitKey(0)
cv2.destroyAllWindows()

