import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  { path: '/', redirect: '/members' },
  { path: '/members', component: () => import('./views/Members.vue') },
  { path: '/consumptions', component: () => import('./views/Consumptions.vue') },
  { path: '/categories', component: () => import('./views/Categories.vue') },
  { path: '/products', component: () => import('./views/Products.vue') },
  { path: '/materials', component: () => import('./views/Materials.vue') },
  { path: '/material-records', component: () => import('./views/MaterialRecords.vue') }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
