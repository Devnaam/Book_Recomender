import React, { useState } from "react";

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <nav className="bg-indigo-600 text-white px-6 py-4 shadow-md fixed w-full top-0 z-50">
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-bold">📚 BookRecommender</h1>

        {/* Desktop Links */}
        <div className="hidden md:flex gap-6">
          <a href="/" className="hover:text-gray-200">Home</a>
          <a href="#recommendations" className="hover:text-gray-200">Recommendations</a>
          <a href="#about" className="hover:text-gray-200">About</a>
        </div>

        {/* Mobile Menu Button */}
        <button
          onClick={() => setIsOpen(!isOpen)}
          className="md:hidden focus:outline-none"
        >
          ☰
        </button>
      </div>

      {/* Mobile Links */}
      {isOpen && (
        <div className="md:hidden mt-2 flex flex-col gap-2">
          <a href="/" className="hover:text-gray-200">Home</a>
          <a href="#recommendations" className="hover:text-gray-200">Recommendations</a>
          <a href="#about" className="hover:text-gray-200">About</a>
        </div>
      )}
    </nav>
  );
}
