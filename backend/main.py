from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import joblib
from sklearn.metrics.pairwise import cosine_similarity
import os

# =========================
# 1️⃣ App initialization
# =========================
app = FastAPI(title="Book Recommendation API")

# Enable CORS (for frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# 2️⃣ Load CSV & artifacts
# =========================
DATA_PATH = "../data/processed_books.csv"
ARTIFACTS_DIR = "../artifacts"

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"{DATA_PATH} not found!")

df = pd.read_csv(DATA_PATH)

# Ensure book_id column
if "book_id" not in df.columns:
    df["book_id"] = df.index

# Fill missing fields
df["title"] = df["title"].fillna("Unknown Title")
df["author"] = df["author"].fillna("Unknown Author")
df["genre"] = df["genre"].fillna("")
df["desc"] = df["desc"].fillna("")
df["rating"] = df["rating"].fillna(0.0)

# Load TF-IDF artifacts
tfidf_path = os.path.join(ARTIFACTS_DIR, "tfidf_vectorizer.pkl")
mapping_path = os.path.join(ARTIFACTS_DIR, "book_id_to_index.pkl")

if not os.path.exists(tfidf_path) or not os.path.exists(mapping_path):
    raise FileNotFoundError("TF-IDF vectorizer or book_id mapping not found in artifacts/")

tfidf_vectorizer = joblib.load(tfidf_path)
book_id_to_index = joblib.load(mapping_path)

# TF-IDF Matrix
tfidf_matrix = tfidf_vectorizer.transform(
    (df["title"] + " " + df["author"] + " " + df["genre"] + " " + df["desc"])
)

print("✅ Backend loaded successfully")

# =========================
# 3️⃣ Root endpoint
# =========================
@app.get("/")
def root():
    return {"message": "Book Recommendation API is running!"}


# =========================
# 4️⃣ Recommend by Book ID
# =========================
@app.get("/recommend")
def recommend_by_id(
    book_id: int = Query(..., description="Book ID"),
    top_n: int = Query(5, description="Number of recommendations"),
):
    if book_id not in book_id_to_index:
        raise HTTPException(status_code=404, detail="Book ID not found")

    idx = book_id_to_index[book_id]
    sim_scores = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()
    top_idx = sim_scores.argsort()[::-1][1 : top_n + 1]  # exclude the book itself

    recommendations = []
    for i in top_idx:
        recommendations.append(
            {
                "book_id": int(df.iloc[i]["book_id"]),
                "title": df.iloc[i]["title"],
                "author": df.iloc[i]["author"],
                "rating": float(df.iloc[i]["rating"]),
                "similarity_score": float(sim_scores[i]),
                "image_url": df.iloc[i]['image_url'] if "image_url" in df.columns else "",
            }
        )

    return {
        "book_id": book_id,
        "title": df.iloc[idx]["title"],
        "recommendations": recommendations,
    }


# =========================
# 5️⃣ Recommend by Title / Query (✅ NEW)
# =========================
@app.get("/recommend_by_query")
def recommend_by_query(
    query: str = Query(..., description="Book title or keyword"),
    top_n: int = Query(5, description="Number of recommendations"),
):
    q_lower = query.lower()

    # Find closest matching book
    matches = df[df["title"].str.lower().str.contains(q_lower)]
    if matches.empty:
        raise HTTPException(status_code=404, detail="No books found matching that query")

    # Use first match as reference
    ref_idx = matches.index[0]
    sim_scores = cosine_similarity(tfidf_matrix[ref_idx], tfidf_matrix).flatten()
    top_idx = sim_scores.argsort()[::-1][1 : top_n + 1]

    recommendations = []
    for i in top_idx:
        recommendations.append(
            {
                "book_id": int(df.iloc[i]["book_id"]),
                "title": df.iloc[i]["title"],
                "author": df.iloc[i]["author"],
                "rating": float(df.iloc[i]["rating"]),
                "similarity_score": float(sim_scores[i]),
                "image_url": df.iloc[i]['image_url'] if "image_url" in df.columns else "",
            }
        )

    return {
        "searched_query": query,
        "matched_title": df.iloc[ref_idx]["title"],
        "recommendations": recommendations,
    }


# =========================
# 6️⃣ Search endpoint
# =========================
@app.get("/search")
def search_books(q: str = Query(..., description="Search query"), limit: int = Query(20, description="Max results")):
    q_lower = q.lower()
    results = df[df['title'].str.lower().str.contains(q_lower)][['book_id', 'title', 'author', 'rating']]
    
    # Add image_url if exists
    if "image_url" in df.columns:
        results = df[df['title'].str.lower().str.contains(q_lower)][['book_id', 'title', 'author', 'rating', 'image_url']]
    
    results = results.head(limit)
    return results.to_dict(orient="records")
