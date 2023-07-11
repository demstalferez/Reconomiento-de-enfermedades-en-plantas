# Clasificador de Enfermedades de Plantas :herb:

Este repositorio alberga un proyecto dedicado al diagnóstico de enfermedades de plantas mediante imágenes. Con más de 122,000 imágenes de 38 categorías diferentes de enfermedades de plantas, este proyecto busca dar un paso hacia la automatización del diagnóstico de enfermedades de las plantas, lo que podría tener un impacto significativo en la economía agrícola y la seguridad alimentaria en todo el mundo.

## Conjunto de datos

El conjunto de datos utilizado para este proyecto es altamente variado y detallado, con 70000 imágenes de plantas tanto saludables como enfermas. Las enfermedades varían desde la mancha bacteriana en los tomates hasta la costra de manzana, ofreciendo un amplio espectro de condiciones para entrenar a nuestro modelo.

## Modelo

Se ha utilizado un modelo de red neuronal convolucional (CNN) para entrenar y clasificar las imágenes. Las CNN son especialmente buenas para analizar imágenes y han demostrado ser efectivas en tareas de clasificación de imágenes.

## Streamlit App

Para demostrar la eficacia de nuestro modelo, hemos creado una aplicación Streamlit que permite a los usuarios subir sus propias imágenes de plantas para diagnósticos. La aplicación entonces pasa la imagen a través de nuestro modelo y devuelve un diagnóstico.


