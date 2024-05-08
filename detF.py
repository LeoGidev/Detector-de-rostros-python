import cv2

# Carga la imagen
image_path = 'img.jpeg'
image = cv2.imread(image_path)

# Crea el clasificador de rostros
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Convierte la imagen a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detecta rostros en la imagen
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Dibuja un rectángulo alrededor de cada rostro detectado
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Muestra la imagen con los rostros detectados
cv2.imshow('Rostros detectados', image)
cv2.waitKey(0)
cv2.destroyAllWindows()