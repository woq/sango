import { createRouter,createWebHistory} from "vue-router";

// 路由信息
const routes = [
    {
        path: "/",
        name: "index",
        component:  () => import('../views/index.vue'),
    },
    {
        path: "/status",
        name: "status",
        component:  () => import('../views/status.vue'),
    },
    {
        path: "/about",
        name: "about",
        component:  () => import('../views/about.vue'),
    },
];

// 导出路由
const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;