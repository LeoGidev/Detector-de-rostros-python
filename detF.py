import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def detect_faces():
    global image_label, image_path, faces
    
    # Carga la imagen seleccionada
    image_path = filedialog.askopenfilename()
    if image_path:
        # Carga la imagen
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
        
        # Convierte la imagen a formato compatible con tkinter
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        
        # Muestra la imagen en la interfaz gráfica
        image_label.config(image=image)
        image_label.image = image

def save_result():
    global faces, image_path
    if faces is not None and len(faces) > 0:
        # Guarda la imagen con los rostros detectados
        if image_path:
            file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
            if file_path:
                try:
                    # Carga la imagen original para evitar cambios de formato
                    original_image = cv2.imread(image_path)
                    # Dibuja los rectángulos en la imagen original
                    for (x, y, w, h) in faces:
                        cv2.rectangle(original_image, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    # Guarda la imagen con los rostros detectados
                    cv2.imwrite(file_path, original_image)
                    print("Resultado guardado correctamente.")
                except Exception as e:
                    print("Error al guardar la imagen:", e)
        else:
            print("Primero debes cargar una imagen.")
    else:
        print("Primero debes detectar los rostros.")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Detector de Rostros")

# Botones
detect_button = tk.Button(root, text="Detectar Rostros", command=detect_faces)
detect_button.pack(pady=10)

save_button = tk.Button(root, text="Guardar Resultado", command=save_result)
save_button.pack(pady=5)

# Etiqueta de imagen
image_label = tk.Label(root)
image_label.pack(padx=10, pady=10)

# Iniciar la interfaz gráfica
root.mainloop()
