// config/endpoints.js

const BASE_URL = "https://ustamarketplace.onrender.com";

const API = {
    auth: {
        login: `${BASE_URL}/api/v1/auth/login/`,
        register: `${BASE_URL}/api/v1/auth/register/`,
        refresh: `${BASE_URL}/api/v1/auth/refresh/`,
        me: `${BASE_URL}/api/v1/me/`
    },

    categories: `${BASE_URL}/api/v1/categories/`,
    services: `${BASE_URL}/api/v1/services/`,
    orders: `${BASE_URL}/api/v1/orders/`,
    reviews: `${BASE_URL}/api/v1/reviews/`,

    worker_public: `${BASE_URL}/api/v1/worker-public/`,
    profile: `${BASE_URL}/api/v1/worker-profile/`,

    dashboard: {
        stats: `${BASE_URL}/api/v1/dashboard/stats/`,

        users: `${BASE_URL}/api/v1/dashboard/users/`,
        worker_profiles: `${BASE_URL}/api/v1/dashboard/worker-profiles/`,

        categories: `${BASE_URL}/api/v1/dashboard/categories/`,
        services: `${BASE_URL}/api/v1/dashboard/services/`,
        orders: `${BASE_URL}/api/v1/dashboard/orders/`,
        reviews: `${BASE_URL}/api/v1/dashboard/reviews/`
    }
};