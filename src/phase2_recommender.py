import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import os

# =========================
# 1️⃣ Load processed CSV
# =========================
DATA_PATH = "../data/processed_books.csv"
df = pd.read_csv(DATA_PATH)

# Add unique book_id if not already present
if 'book_id' not in df.columns:
    df['book_id'] = df.index

# Fill missing text fields to avoid errors
df['title_clean'] = df['title'].fillna('')
df['author_clean'] = df['author'].fillna('')
df['genre_clean'] = df['genre'].fillna('')
df['desc_clean'] = df['desc'].fillna('')

# Save back CSV with book_id
df.to_csv(DATA_PATH, index=False)
print("✅ CSV loaded and book_id column ensured")

# =========================
# 2️⃣ Combine text columns for TF-IDF
# =========================
df['combined_text'] = (
    df['title_clean'] + ' ' +
    df['author_clean'] + ' ' +
    df['genre_clean'] + ' ' +
    df['desc_clean']
)

# =========================
# 3️⃣ Create TF-IDF vectorizer
# =========================
tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['combined_text'])
print("✅ TF-IDF matrix created with shape:", tfidf_matrix.shape)

# =========================
# 4️⃣ Create mapping from book_id to index
# =========================
book_id_to_index = pd.Series(df.index, index=df['book_id']).to_dict()
print("✅ Book ID to index mapping created")

# =========================
# 5️⃣ Recommendation function
# =========================
def recommend(book_id, top_n=10):
    if book_id not in book_id_to_index:
        return "Book ID not found!"
    
    idx = book_id_to_index[book_id]
    sim_scores = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()
    top_idx = sim_scores.argsort()[::-1][1:top_n+1]  # exclude self
    
    recommendations = []
    for i in top_idx:
        recommendations.append({
            "book_id": int(df.iloc[i]['book_id']),
            "title": df.iloc[i]['title'],
            "author": df.iloc[i]['author'],
            "rating": float(df.iloc[i]['rating']),
            "similarity_score": float(sim_scores[i])
        })
    return recommendations

# =========================
# 6️⃣ Test the recommender
# =========================
test_id = df['book_id'].iloc[0]
print(f"\nTop 5 recommendations for Book ID {test_id} ({df.iloc[0]['title']}):\n")
for book in recommend(test_id, top_n=5):
    print(book)

# =========================
# 7️⃣ Save artifacts for backend
# =========================
ARTIFACTS_DIR = "../artifacts"
os.makedirs(ARTIFACTS_DIR, exist_ok=True)
joblib.dump(tfidf, os.path.join(ARTIFACTS_DIR, "tfidf_vectorizer.pkl"))
joblib.dump(book_id_to_index, os.path.join(ARTIFACTS_DIR, "book_id_to_index.pkl"))
print("\n✅ TF-IDF vectorizer and book ID mapping saved to artifacts/")
