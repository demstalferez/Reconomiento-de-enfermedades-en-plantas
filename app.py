import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np

IMG_SIZE = 224
labels = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 
          'Background_without_leaves', 'Blueberry___healthy', 'Cherry___Powdery_mildew', 'Cherry___healthy', 
          'Corn___Cercospora_leaf_spot Gray_leaf_spot', 'Corn___Common_rust', 'Corn___Northern_Leaf_Blight', 
          'Corn___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 
          'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 
          'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 
          'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 
          'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 
          'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 
          'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 
          'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 
          'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 
          'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']

# Mapear las categorías a sus traducciones en español. 
traducciones = ['Manzana___Sarna del manzano', 'Manzana___Podredumbre negra', 
                'Manzana___Roya del cedro', 'Manzana___Sana', 
                'Fondo sin hojas', 'Arándano___Sano', 'Cereza___Mildiu polvoriento', 
                'Cereza___Sana', 'Maíz___Mancha de la hoja de Cercospora y mancha gris de la hoja',
                'Maíz___Roya común', 'Maíz___Tizón de la hoja norte', 'Maíz___Sano',
                'Uva___Podredumbre negra', 'Uva___Esca (Sarampión negro)', 'Uva___Quemadura de la hoja (Mancha de la hoja de Isariopsis)',
                'Uva___Sana', 'Naranja___Huanglongbing (Enverdecimiento de los cítricos)', 
                'Melocotón___Mancha bacteriana', 'Melocotón___Sano', 'Pimiento___Mancha bacteriana',
                'Pimiento___Sano', 'Patata___Tizón temprano', 'Patata___Tizón tardío',
                'Patata___Sana', 'Frambuesa___Sana', 'Soja___Sana', 'Calabaza___Mildiu polvoriento',
                'Fresa___Quemadura de la hoja', 'Fresa___Sana', 'Tomate___Mancha bacteriana', 
                'Tomate___Tizón temprano', 'Tomate___Tizón tardío', 'Tomate___Moho de la hoja', 
                'Tomate___Mancha de Septoria', 'Tomate___Ácaros rojos', 'Tomate___Mancha objetiva', 
                'Tomate___Virus del rizo amarillo del tomate', 'Tomate___Virus del mosaico del tomate', 
                'Tomate___Sano']

@st.cache_data()
def load_model():
    model = tf.keras.models.load_model('modelo/bulbasaur.h5')
    return model

def process_image(image_path):
    img = Image.open(image_path)
    img = img.resize((IMG_SIZE, IMG_SIZE))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    return img

def main():
    st.title("Sistema de prevención de enfermedades de plantas y plagas")
    st.write("Carga una imagen de una planta, y te diré si está enferma o sana, y si está enferma, qué tipo de enfermedad tiene.")

    model = load_model()

    file_uploader = st.file_uploader("Carga tu imagen", type=["png", "jpg", "jpeg"])

    if file_uploader is not None:
        image = Image.open(file_uploader)
        st.image(image, caption='Imagen cargada', use_column_width=True)
        img = process_image(file_uploader)
        prediction = model.predict(img)
        label = np.argmax(prediction)

        if "healthy" in labels[label]:
            st.write("La planta está sana.")
        else:
            st.write(f"La planta está enferma. Tiene {traducciones[label]}.")

if __name__ == "__main__":
    main()


