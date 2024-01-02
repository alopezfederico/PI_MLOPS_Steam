from fastapi import FastAPI
import pandas as pd
import numpy as np


# Carga de datos
df_playtime_genre = pd.read_csv('FeatureEngData/df_playtime_genre.csv',low_memory=False)
df_sentiment_analysis = pd.read_csv('FeatureEngData/df_sentimennt_analysis.csv',low_memory=False)
df_user_for_genre = pd.read_parquet('FeatureEngData/df_user_for_genre.parquet')
df_users_recommend = pd.read_csv('FeatureEngData/df_users_recommend.csv',low_memory=False)
df_recomendacion_juego = pd.read_csv('FeatureEngData/df_recomendacion_juego.csv',low_memory=False)


app = FastAPI()


@app.get('/PlayTimeGenre/{genre}')
# 1 FUNCION PLAYTIMEGENRE
async def PlayTimeGenre(genre: str):

    ### Creo un dataset solo con el listado de datos con el genero brindado
    df_genero = df_playtime_genre[df_playtime_genre['genres'].str.lower() == genre.lower() if isinstance(genre, str) else None]

    ### Si el df está vacio, es porque no encontró informacion para el genero ingreado
    if df_genero.empty:
        return {f"No hay informacion para el genero {genre}": None}

    if not df_genero['playtime_forever'].empty:
        
        max_hours = df_genero.loc[df_genero['playtime_forever'].idxmax(), 'release_year']

        return {f"Año de lanzamiento con mayor horas de juego para el genero {genre}": max_hours}
    else:
        return {f"No hay informacion para el genero {genre}": None}
    

@app.get('/UserForGenre/{genre}')

async def UserForGenre(genre: str | None = None):
    
    genre_df = df_user_for_genre[df_user_for_genre['genres'].str.lower() == genre.lower() if isinstance(genre, str) else None]

    if genre_df.empty:
        return {"Usuario con mas horas jugadas para el genero": None, "Horas jugadas por año": {}}

    if not genre_df.empty:
        user_playtime_sum = genre_df.groupby('user_id')['horas'].sum()

        max_horas = user_playtime_sum.idxmax()

        usuario = genre_df[genre_df['user_id'] == max_horas]

        horas_año = dict(zip(usuario['release_year'], usuario['horas']))

        return {f"Usuario con mas horas jugadas para el genero {genre}": max_horas, "Horas jugadas por año": horas_año}



@app.get('/UsersRecommend/{year}')
async def UsersRecommend(year:int):

    # Verificar si hay revisiones para el año dado
    if not df_users_recommend.empty:
        # Filtrar las revisiones para el año dado y recomendaciones positivas/neutrales
        recomendaciones = df_users_recommend[df_users_recommend['posted'] == str(year)]
        
        # Ordenar en orden descendente por la cantidad de recomendaciones
        recomendaciones = recomendaciones.sort_values('sentiment_analysis', ascending=False)
        
        # Crear una única línea de resultado
        resultado = {
            "Puesto 1": recomendaciones.iloc[0]['app_name'],
            "Puesto 2": recomendaciones.iloc[1]['app_name'],
            "Puesto 3": recomendaciones.iloc[2]['app_name']
        }
        
        return resultado




@app.get('/UsersNotRecommend/{year}')
def UsersNotRecommend(year):
    
    # Verificar si hay revisiones para el año dado
    if not df_users_recommend.empty:
        # Filtrar las revisiones para el año dado y recomendaciones positivas/neutrales
        recomendaciones = df_users_recommend[df_users_recommend['posted'] == str(year)]
        
        # Ordenar en orden descendente por la cantidad de recomendaciones
        recomendaciones = recomendaciones.sort_values('sentiment_analysis', ascending=True)
        
        # Crear una única línea de resultado
        resultado = {
            "Puesto 1": recomendaciones.iloc[0]['app_name'],
            "Puesto 2": recomendaciones.iloc[1]['app_name'],
            "Puesto 3": recomendaciones.iloc[2]['app_name']
        }
        
        return resultado
    

@app.get('/sentiment_analysis/{year}')
def sentiment_analysis( year : int ):
    year = str(year)

    filtered_reviews = df_sentiment_analysis[df_sentiment_analysis['release_year'] == year]
   
    sentiment_counts = filtered_reviews['sentiment_analysis'].value_counts().to_dict()
  
    result = {
        'Negative': sentiment_counts.get(0, 0),
        'Neutral': sentiment_counts.get(1, 0),
        'Positive': sentiment_counts.get(2, 0)
    }
    
    return result



