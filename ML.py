### Preprocesamiento de datos
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df_user_recomendation = pd.read_csv('FeatureEngData/df_recomendacion_juego.csv', low_memory=False)


def recomendacion_juego(producto_id, df=df_user_recomendation):

    # Creo una matriz TF-IDF
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df_user_recomendation['combinacion'])

    # Calculo la similitud del coseno
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    # Verifico si el ID del producto está presente en el DataFrame
    if producto_id not in df['item_id'].values:
        return "No se encontraron datos para este ID de producto."
    
    idx = df[df['item_id'] == producto_id].index[0]  # Obtener el índice del juego dado su ID
    
    # Calcular la similitud entre el juego dado y los demás juegos
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # Top 5 juegos similares
    
    # Obtener los índices de los juegos similares
    game_indices = [i[0] for i in sim_scores]
    
    # Devolver los nombres de los juegos recomendados
    return df['app_name'].iloc[game_indices]