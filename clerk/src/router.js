import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  { path: '/', redirect: '/home' },
  { path: '/home', component: () => import('./views/Home.vue') },
  { path: '/search-member', component: () => import('./views/SearchMember.vue') },
  { path: '/new-consumption', component: () => import('./views/NewConsumption.vue') },
  { path: '/stock', component: () => import('./views/Stock.vue') }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
