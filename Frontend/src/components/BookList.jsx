import React from "react";

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


export default BookList;
