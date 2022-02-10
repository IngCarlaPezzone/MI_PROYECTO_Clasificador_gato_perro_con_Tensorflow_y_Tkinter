from tkinter import *           #permite construir nuestra GUI con distintos Widgets
from tkinter import filedialog  #permite crear un diálogo de archivos
from PIL import Image           #PIL (Python Imaging Library) es una librería que nos permitirá 
from PIL import ImageTk         #trabajar o manipular imágenes
import cv2                      #trabajar o manipular imágenes
import imutils                  #trabajar o manipular imágenes
import numpy as np
from keras.preprocessing import image
from keras.models import load_model


#Función que busca la imagen y realiza la predicción
def elegir_imagen():
    #Formatos de imagen que puede elegir
    path_image=filedialog.askopenfilename(filetypes=[
        ('imagen', '.jpg'),
        ('imagen', '.jpeg'),
        ('imagen', '.png')])
    #Para cada imagne que abro
    if len(path_image)>0:
        global imagen
        #Para leer la imagen de entrada y redimensionar
        imagen = cv2.imread(path_image)
        imagen=imutils.resize(imagen, height=380)
        #Para visualizar la imagen en la pantalla
        imageToShow=imutils.resize(imagen, width=180)
        imageToShow = cv2.cvtColor(imageToShow, cv2.COLOR_BGR2RGB)
        #Para insertar la imagen a la pantalla
        im=Image.fromarray(imageToShow)
        img=ImageTk.PhotoImage(image=im)
        lblInputImage.configure(image=img)
        lblInputImage.image=img
        #Para darle un título a la imagen ingresada
        lblInfo1=Label(root, text="IMAGEN INGRESADA:")
        lblInfo1.grid(column=0, row=1, padx=5, pady=5)

    
    # Para dar la predicción de la imagen seleccionada
    img=image.load_img(path_image, target_size=(150, 150))
      
    x=image.img_to_array(img)
    x /= 255
    x=np.expand_dims(x, axis=0)
    images = np.vstack([x])
      
    model = load_model('perros-gatos.h5')   #para abrir el modelo entrenado
      
    classes = model.predict(images, batch_size=10)
                
    if classes [0][0]>0.5:
        lblInfo2=Label(root, text="ES UN PERRO!!")
        lblInfo2.grid(column=0, row=4, padx=5, pady=5)
    else:
        lblInfo3=Label(root, text="ES UN GATO!!")
        lblInfo3.grid(column=0, row=4, padx=5, pady=5)

#Para programar la interface
imagen=None #variable que almacena la imagen

#Ventana principal
root=Tk()

#Para visualizar la imagen que leamos
lblInputImage=Label(root)
lblInputImage.grid(column=0, row=2) #para ubicarlo en el espacio

#Botón para elegir una imagen
botonImag=Button(root, text="Elegir imagen de gato o perro", width=25, command=elegir_imagen) #command llama a la función con cada click
botonImag.grid(column=0, row=0, padx=5, pady=5) #para ubicarlo en el espacio

root.mainloop()
