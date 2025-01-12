import cv2
import os
from datetime import datetime

# Abre a câmera (0 é geralmente o ID da câmera integrada)
cap = cv2.VideoCapture(0, cv2.CAP_MSMF)

if not cap.isOpened():
    print("Erro ao abrir a câmera")
    exit()

# Define uma resolução desejada
desired_width = 640
desired_height = 480

# Tenta definir a resolução
cap.set(cv2.CAP_PROP_FRAME_WIDTH, desired_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, desired_height)

# Verifica a resolução atual da câmera
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define o diretório e o nome do arquivo baseado na data atual
output_dir = '~'  # Substitua pelo caminho desejado
date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_file = f'output_{date_str}.mkv'
output_path = os.path.join(output_dir, output_file)

# Verifica se o diretório existe, senão, cria
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define o codec e cria o objeto VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_path, fourcc, 20.0, (width, height))

if not out.isOpened():
    print("Erro ao abrir o VideoWriter")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Falha ao capturar imagem")
        break

    # Escreve o frame no arquivo
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera tudo ao final
cap.release()
out.release()
cv2.destroyAllWindows()
print(f"Vídeo salvo em: {output_path}")
