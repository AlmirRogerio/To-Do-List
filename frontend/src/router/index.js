import { createRouter, createWebHistory } from 'vue-router'
import { useAuth } from '../composables/useAuth.js'

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/auth/AuthView.vue')
  },
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/tasks/TasksView.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('../views/not-found/NotFoundView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to) => {
  const { isLoggedIn } = useAuth()
  if (to.meta.requiresAuth && !isLoggedIn.value) return '/login'
  if (to.path === '/login' && isLoggedIn.value) return '/'
})

export default router
