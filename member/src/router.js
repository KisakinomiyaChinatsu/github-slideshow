import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  { path: '/', redirect: '/home' },
  { path: '/home', component: () => import('./views/Home.vue') },
  { path: '/login', component: () => import('./views/Login.vue') },
  { path: '/consumption', component: () => import('./views/Consumption.vue') }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
