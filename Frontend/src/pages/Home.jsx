import React, { useState } from "react";
import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import SearchBar from "../components/SearchBar";
import BookList from "../components/BookList";

const Home = () => {
	const [books, setBooks] = useState([]);

	// function passed down to SearchBar
	const fetchRecommendations = async (query) => {
		try {
			const response = await fetch(
				`http://127.0.0.1:8000/recommend_by_query?query=${encodeURIComponent(
					query
				)}`
			);

			if (!response.ok) throw new Error("Failed to fetch recommendations");

			const data = await response.json();
			setBooks(data.recommendations || []);
		} catch (error) {
			console.error("Error fetching recommendations:", error);
		}
	};

	return (
		<div className="bg-gray-100 min-h-screen">
			<Navbar />
			<Hero />
			{/* ✅ Pass fetchRecommendations as onSearch */}
			<SearchBar onSearch={fetchRecommendations} />
			<BookList books={books} />
		</div>
	);
};

export default Home;
