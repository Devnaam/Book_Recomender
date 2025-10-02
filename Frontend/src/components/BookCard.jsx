import React from "react";

export default function BookCard({ book }) {
  return (
    <div className="bg-white shadow-md rounded-lg overflow-hidden w-60 hover:shadow-xl transition duration-300">
      <img
        src={book.image}
        alt={book.title}
        className="w-full h-80 object-cover"
      />
      <div className="p-4">
        <h3 className="text-lg font-semibold mb-2">{book.title}</h3>
        <p className="text-gray-600 text-sm">by {book.author}</p>
      </div>
    </div>
  );
}
