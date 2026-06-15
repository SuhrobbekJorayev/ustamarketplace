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
    users: `${BASE_URL}/api/v1/users/`, 
    
    // 👇 SIZNING BACKEND VIEW'LARINGIZ UCHUN YANGI ENDPOINTLAR:
    worker_public: `${BASE_URL}/api/v1/worker-public/`, // WorkerPublicViewSet uchun
    profile: `${BASE_URL}/api/v1/worker-profile/`,      // WorkerProfileView (RetrieveUpdateAPIView) uchun

    dashboard: {
        stats: `${BASE_URL}/api/v1/dashboard/stats/`,
        users: `${BASE_URL}/api/v1/dashboard/users/`,
        services: `${BASE_URL}/api/v1/dashboard/services/`,
        orders: `${BASE_URL}/api/v1/dashboard/orders/`,
        categories: `${BASE_URL}/api/v1/dashboard/categories/`
    }
};