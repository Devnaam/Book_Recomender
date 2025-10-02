import pandas as pd
import re
import os

# 1️⃣ Load CSV
DATA_PATH = "../data/books.csv"
df = pd.read_csv(DATA_PATH)
print("Original shape:", df.shape)

# 2️⃣ Fill missing values for text columns
text_cols = ['title', 'author', 'desc', 'genre', 'bookformat']
for col in text_cols:
    if col in df.columns:
        df[col] = df[col].fillna('')  # empty string for missing text

# 3️⃣ Clean text: lowercase, remove punctuation, strip extra spaces
def clean_text(s):
    s = s.lower()
    s = re.sub(r'[^a-z0-9\s]', ' ', s)  # remove punctuation
    s = re.sub(r'\s+', ' ', s).strip()  # remove extra spaces
    return s

# Apply cleaning
for col in ['title', 'author', 'desc', 'genre']:
    if col in df.columns:
        df[col + "_clean"] = df[col].apply(clean_text)

# 4️⃣ Handle duplicates
# Consider duplicates by title + author
df = df.drop_duplicates(subset=['title', 'author'], keep='first')
print("After removing duplicates:", df.shape)

# 5️⃣ Optional: convert numeric columns
numeric_cols = ['pages', 'rating', 'reviews', 'totalratings']
for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')  # just in case

# 6️⃣ Save processed CSV
PROCESSED_PATH = "../data/processed_books.csv"
df.to_csv(PROCESSED_PATH, index=False)
print("Processed CSV saved:", PROCESSED_PATH)
