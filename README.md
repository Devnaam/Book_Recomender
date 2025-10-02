# 📚 Book Recommendation System  

A full-stack **Book Recommendation Web App** that helps users discover their next favorite book using **content-based filtering (TF-IDF & Cosine Similarity)**.  
The project is built with **FastAPI (backend)** and **React + Vite + TailwindCSS (frontend)**.  

---

## 🚀 Features  

### ✅ Implemented
- **Search books** by title (integrated with FastAPI backend).  
- **Responsive frontend UI** with TailwindCSS.  
- **Book list with details** (title, author, rating, cover image).  
- **Recommendation endpoint** using TF-IDF similarity.  

### 🔧 In Progress / Planned
- 🔎 **Advanced search functionality** with filters (author, genre, year, rating).  
- 📚 **Categories-wise recommendations** (explore books by genre).  
- 🖼 **Rich book metadata** (title, author, synopsis, cover, publication year, ISBN).  
- 🔥 **Popular / trending books section** for discovery.  
- 📖 **Book detail page** with similar book suggestions.  

---

## 🛠 Tech Stack  

**Backend**  
- [FastAPI](https://fastapi.tiangolo.com/) – REST API framework  
- [scikit-learn](https://scikit-learn.org/) – TF-IDF & Cosine Similarity  
- [pandas](https://pandas.pydata.org/) – data manipulation  
- [joblib](https://joblib.readthedocs.io/) – model persistence  
- [Uvicorn](https://www.uvicorn.org/) – ASGI server  

**Frontend**  
- [React + Vite](https://vitejs.dev/) – modern frontend framework  
- [TailwindCSS](https://tailwindcss.com/) – responsive styling  
- [React Router](https://reactrouter.com/) – routing  

---

## 📂 Project Structure  

BookRecommender/
│
├── backend/
│ ├── main.py # FastAPI entrypoint
│ ├── recommender.py # Recommendation logic
│ ├── requirements.txt # Python dependencies
│ ├── data/
│ │ └── processed_books.csv
│ └── artifacts/
│ ├── tfidf_vectorizer.pkl
│ └── book_id_to_index.pkl
│
├── frontend/
│ ├── src/
│ │ ├── components/ # Navbar, Hero, SearchBar, BookList
│ │ ├── pages/ # Home, BookDetails (planned)
│ │ └── App.jsx
│ ├── index.html
│ ├── package.json
│ └── tailwind.config.js
│
└── README.md

## ⚡ Setup Instructions  

### 1️⃣ Clone Repository  
```bash
git clone https://github.com/yourusername/book-recommender.git
cd book-recommender