import axios from "axios";

const API_BASE = "http://127.0.0.1:8000";

export const getRecommendations = async (book_id, top_n = 5) => {
    const response = await axios.get(`${API_BASE}/recommend`, {
        params: { book_id, top_n }
    });
    return response.data;
};

export const searchBooks = async (query, limit = 20) => {
    const response = await axios.get(`${API_BASE}/search`, {
        params: { q: query, limit }
    });
    return response.data;
};
