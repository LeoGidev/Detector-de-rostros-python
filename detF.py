import cv2

# Carga la imagen
image_path = 'imagen.jpg'
image = cv2.imread(image_path)

# Crea el clasificador de rostros
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

