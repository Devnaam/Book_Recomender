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

```
BookRecommender/
├── backend/
│   ├── main.py                # FastAPI entrypoint
│   ├── recommender.py         # Recommendation logic
│   ├── requirements.txt       # Python dependencies
│   ├── data/
│   │   └── processed_books.csv
│   └── artifacts/
│       ├── tfidf_vectorizer.pkl
│       └── book_id_to_index.pkl
│
├── frontend/
│   ├── src/
│   │   ├── components/        # Navbar, Hero, SearchBar, BookList
│   │   ├── pages/            # Home, BookDetails (planned)
│   │   └── App.jsx
│   ├── index.html
│   ├── package.json
│   └── tailwind.config.js
│
└── README.md
```

## ⚡ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/book-recommender.git
cd book-recommender
```

### 2️⃣ Backend Setup (FastAPI)

```bash
# Navigate to backend folder
cd backend

# Create virtual environment & activate
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows

# Install dependencies
pip install -r requirements.txt

# Run backend
uvicorn main:app --reload
```

The API will run at → http://127.0.0.1:8000

### 3️⃣ Frontend Setup (React + Vite)

```bash
# Navigate to frontend folder
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

The frontend will run at → http://127.0.0.1:5173

## 📡 API Endpoints

### Root

```
GET /
```

Response:

```json
{
	"message": "Book Recommendation API is running!"
}
```

### Search Books

```
GET /search?q=harry
```

Optional filters (planned): author, genre, year, rating_min

### Recommend by Book ID

```
GET /recommend?book_id=42&top_n=5
```

### Categories (Planned)

```
GET /categories
GET /recommend_by_category?genre=fantasy
```

### Popular Books (Planned)

```
GET /popular
```

## 🤝 Contribution Guide

We welcome contributions!

### How to Contribute

1. Fork the repo
2. Create a new branch (`feature/advanced-search`)
3. Commit changes (`git commit -m "Added advanced search filters"`)
4. Push branch (`git push origin feature/advanced-search`)
5. Open a Pull Request

### Contribution Ideas

- Improve UI/UX with better design
- Add new recommendation algorithms (collaborative filtering, hybrid models)
- Implement trending books logic (based on usage stats)
- Add unit tests for backend APIs

## 📌 Roadmap

- [ ] Metadata expansion (book year, cover, synopsis)
- [ ] Advanced search with filters
- [ ] Categories-based recommendations
- [ ] Popular/trending section
- [ ] Book detail page with "more like this"

## 📜 License

This project is licensed under the MIT License.

## 👨‍💻 Author

Developed by [Devnaam] 🚀
