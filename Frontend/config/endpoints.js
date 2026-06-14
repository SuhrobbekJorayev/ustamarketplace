// config/endpoints.js
const BASE_URL = "https://ustamarketplace.onrender.com";

const API = {
    auth: {
        login: `${BASE_URL}/api/v1/auth/login/`,
        register: `${BASE_URL}/api/v1/auth/register/`,
        refresh: `${BASE_URL}/api/v1/auth/refresh/`
    },
    services: `${BASE_URL}/api/v1/services/`,
    categories: `${BASE_URL}/api/v1/categories/`,
    orders: `${BASE_URL}/api/v1/orders/`,
    reviews: `${BASE_URL}/api/v1/reviews/`,
    users: `${BASE_URL}/api/v1/users/`, // Profil ma'lumotlari uchun
    dashboard: {
        stats: `${BASE_URL}/api/v1/dashboard/stats/`,
        users: `${BASE_URL}/api/v1/dashboard/users/`,
        services: `${BASE_URL}/api/v1/dashboard/services/`,
        orders: `${BASE_URL}/api/v1/dashboard/orders/`,
        categories: `${BASE_URL}/api/v1/dashboard/categories/`
    }
};

// Token muddati tugaganda parda ortida avtomatik yangilash (JWT auto-refresh) funksiyasi
async function fetchWithAuth(url, options = {}) {
    options.headers = options.headers || {};
    let access = localStorage.getItem("access");

    if (access) {
        options.headers["Authorization"] = `Bearer ${access}`;
    }
    if (!options.headers["Content-Type"] && !(options.body instanceof FormData)) {
        options.headers["Content-Type"] = "application/json";
    }

    let response = await fetch(url, options);

    // Agar 401 Unauthorized qaytsa va refresh token bo'lsa, token yangilanadi
    if (response.status === 401 && localStorage.getItem("refresh")) {
        const refreshRes = await fetch(API.auth.refresh, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ refresh: localStorage.getItem("refresh") })
        });

        if (refreshRes.ok) {
            const data = await refreshRes.json();
            localStorage.setItem("access", data.access);
            
            // So'rovni yangi token bilan qayta yuborish
            options.headers["Authorization"] = `Bearer ${data.access}`;
            response = await fetch(url, options);
        } else {
            // Agar refresh ham o'tgan bo'lsa, sessiyani tozalab login sahifasiga otib yuboradi
            localStorage.clear();
            window.location.href = "login.html";
        }
    }
    return response;
}