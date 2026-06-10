// Frontend/config/endpoints.js
const BASE_URL = "http://127.0.0.1:8000/api/v1";

async function getAuthHeaders() {
    let token = localStorage.getItem("access");
    if (!token) return { "Content-Type": "application/json" };
    return {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`
    };
}

const API = {
    auth: {
        login: `${BASE_URL}/auth/login/`,
        refresh: `${BASE_URL}/auth/refresh/`,
        register: `${BASE_URL}/auth/register/`
    },
    categories: `${BASE_URL}/categories/`,
    services: `${BASE_URL}/services/`,
    orders: `${BASE_URL}/orders/`,
    reviews: `${BASE_URL}/reviews/`,
    workers: `${BASE_URL}/worker-profiles/`,
    users: `${BASE_URL}/users/`
};