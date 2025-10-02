import React, { useState } from "react";

const SearchBar = ({ onSearch }) => {
  const [query, setQuery] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!query.trim()) return;
    if (onSearch) {
      onSearch(query);
    } else {
      console.warn("SearchBar used without onSearch prop.");
    }
  };

const BookList = ({ books }) => {
  if (!books || books.length === 0) {
    return <p className="text-gray-500">No books found</p>;
  }

  return (
    <div className="grid grid-cols-2 md:grid-cols-4 gap-6 p-4">
      {books.map((book) => (
        <div key={book.book_id} className="bg-white p-4 rounded-xl shadow hover:shadow-lg transition">
          {book.image_url ? (
            <img src={book.image_url} alt={book.title} className="h-40 w-full object-cover rounded-lg mb-3" />
          ) : (
            <div className="h-40 w-full bg-gray-200 rounded-lg mb-3 flex items-center justify-center text-gray-400">
              No Image
            </div>
          )}
          <h3 className="font-semibold text-lg">{book.title}</h3>
          <p className="text-sm text-gray-500">{book.author}</p>
          <p className="text-yellow-600 text-sm">⭐ {book.rating.toFixed(1)}</p>
        </div>
      ))}
    </div>
  );
};

  return (
    <div className="flex justify-center mt-6 px-4">
      <form
        onSubmit={handleSubmit}
        className="w-full max-w-lg flex bg-white shadow-md rounded-lg overflow-hidden"
      >
        <input
          type="text"
          placeholder="Search for a book..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="flex-grow px-4 py-2 outline-none"
        />
        <button
          type="submit"
          className="bg-indigo-600 text-white px-6 py-2 hover:bg-indigo-700 transition"
        >
          Search
        </button>
      </form>
    </div>
  );
};

export default SearchBar;
