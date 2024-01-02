<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PI-MLOPS_Steam Games** </h1>

# <h2> **`Federico Lopez`** </h1>

¡Bienvenido a mi primer proyecto como estudiante de Data Science en SoyHenry! En este proyecto, abordo el desafío de crear un sistema de recomendación de videojuegos para la plataforma Steam. <br> Mi objetivo es implementar un Modelo de Aprendizaje Automático (ML) para ofrecer recomendaciones precisas y útiles a los usuarios.

#### **Descripción del Problema** <br>
**Contexto y Rol a Desarrollar:** <br>
El ciclo de vida de un proyecto de Machine Learning abarca desde la recolección y tratamiento de datos hasta el mantenimiento del modelo de ML con datos entrantes. Mi papel en Steam como Data Scientist implica crear un sistema de recomendación de videojuegos. Los datos disponibles presentan desafíos significativos: están crudos, no hay procesos automatizados para actualizaciones, etc.

#### **Propuesta de Trabajo:** <br>
Transformaciones y Feature Engineering: <br>
El enfoque inicial es leer los datos en el formato correcto. Además, se plantea la creación de la columna 'sentiment_analysis' mediante análisis de sentimientos con NLP para categorizar las reseñas como malas (0), neutrales (1) o positivas (2). En casos donde falte la reseña, se asignará el valor 1.<br>
Éste se encuentra en el archivo de optimizarion.ipynb dentro de la carpeta FinalData

#### **Desarrollo API**
Propongo exponer los datos mediante FastAPI. Las consultas que se pueden realizar incluyen:

##### Funciones a desarrollar 

+ def **PlayTimeGenre( *`genero` : str* )**:
    Debe devolver `año` con mas horas jugadas para dicho género.

+ def **UserForGenre( *`genero` : str* )**:
    Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.

+ def **UsersRecommend( *`año` : int* )**:
   Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)

+ def **UsersNotRecommend( *`año` : int* )**:
   Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)

+ def **sentiment_analysis( *`año` : int* )**:
    Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.
Se propone el despliegue en Render o Railway para que la API sea accesible desde cualquier dispositivo conectado a Internet.<br>

¡Este README.md es una vista general del proyecto que desarrollé como estudiante de Data Science! El proyecto incluye la implementación de una API, análisis de sentimientos, tratamiento de datos y más. ¡Gracias por revisarlo!

