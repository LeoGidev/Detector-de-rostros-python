import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def detect_faces():
    global image_label, image, faces
    
    # Carga la imagen seleccionada
    file_path = filedialog.askopenfilename()
    if file_path:
        image = cv2.imread(file_path)
        
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
    global faces, image
    if faces is not None and len(faces) > 0:
        # Guarda la imagen con los rostros detectados
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
        if file_path:
            # Verifica si la imagen se ha cargado correctamente
            if image is not None:
                # Intenta guardar la imagen con los rostros detectados
                try:
                    # Verifica si la imagen ya está en el formato correcto (BGR)
                    if len(image.shape) == 3 and image.shape[2] == 3:
                        cv2.imwrite(file_path, image)
                        print("Resultado guardado correctamente.")
                    else:
                        # Si no está en el formato correcto, intenta convertirla
                        converted_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                        cv2.imwrite(file_path, converted_image)
                        print("Resultado guardado correctamente.")
                except Exception as e:
                    print("Error al guardar la imagen:", e)
            else:
                print("Error: No se ha cargado ninguna imagen.")
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
