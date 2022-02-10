# Starting
## Introducción
Estos son mis primeros pasos en la programación con Python y en deep learning!
Hace comencé a estudiar Python y tan solo 2 meses a estudiar deep learning, pero la curiosidad me llevó a intentar aplicar los conocimientos en una pequeña aplicación que pudiera compartir.
Claro que es muy simple y puede mejorar mucho, pero la idea es tener un punto de partida para ir aplicando lo aprendido en las especializaciones que voy cursando.

## Objetivo de este repositorio
El objetivo de este proyecto fue programar con python una pequeña aplicación que me permita, mediante con una interface (tkinter), ingresar una imagen de Gato o Perro y me de la predicción de lo observado.
Para ello utilicé una red convolucional.
## Materiales
En este HitHub subí dos archivos:
* RedConvolucionalGatosPerros.py: que es el código que use para entrenar la red. Este código se puede pegar en una Jupyter o en una Colab y correrlo.
Una vez entrenada (que toma un tiempo) usé el comando 

> modelo.save('perros-gatos.h5')

Que permite exportar el modelo ya entrenado, para hacer las predicciones sin necesidad de volver a entrenar.
Esto genera un archivo con extensión .h5 que se debe guardar en la misma carpeta donde se va a desarrollar el proyecto de la aplicación.
* PrimerProyectoV0.pyw: es el código que usé para armar la interface y hacer la predicción.
Yo la corrí en Sublime Text.
La extención .pyw es para que cuando se abra la aplicación desde ese archivo no se abra la consola por detras.
## Desafíos pendientes
Me quedó pendiente de resolver un detalle (escucho recomendaciones!!): ¿Cómo hacer que la predicción se ejecute luego de clikear un segundo botón?
