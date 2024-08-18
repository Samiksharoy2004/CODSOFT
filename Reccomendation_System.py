import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.neighbors import NearestNeighbors

# Sample data for Content-Based Filtering
movies_data = {
    'movie_id': [1, 2, 3, 4, 5],
    'title': ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E'],
    'genre': ['Action Comedy', 'Action Drama', 'Comedy Drama', 'Drama', 'Action Comedy']
}

movies_df = pd.DataFrame(movies_data)

# Content-Based Filtering
def content_based_recommendations(title, df):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['genre'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    
    idx = df.index[df['title'] == title].tolist()[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]  # Get top 3 recommendations
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices]

# Sample data for Collaborative Filtering
user_data = {
    'user_id': [1, 1, 2, 2, 3, 3, 4, 4],
    'movie_id': [1, 2, 2, 3, 1, 4, 1, 3],
    'rating': [5, 3, 4, 2, 4, 5, 2, 5]
}

user_df = pd.DataFrame(user_data)
pivot_table = user_df.pivot_table(index='user_id', columns='movie_id', values='rating').fillna(0)

# Collaborative Filtering
def collaborative_recommendations(user_id, pivot_table):
    model = NearestNeighbors(n_neighbors=2, metric='cosine')
    model.fit(pivot_table)
    
    user_row = pivot_table.loc[user_id].values.reshape(1, -1)
    distances, indices = model.kneighbors(user_row)
    similar_users = indices.flatten()
    
    recommended_movies = []
    for similar_user in similar_users:
        similar_user_ratings = pivot_table.iloc[similar_user]
        unrated_movies = similar_user_ratings[similar_user_ratings == 0].index
        recommended_movies.extend(unrated_movies)
    
    recommended_movies = list(set(recommended_movies))
    return recommended_movies

# Example usage
print("Content-Based Recommendations for 'Movie A':")
print(content_based_recommendations('Movie A', movies_df))

print("\nCollaborative Recommendations for User 1:")
print(collaborative_recommendations(1, pivot_table))
