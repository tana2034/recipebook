import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/signup',
      name: 'signup',
      component: () => import('@/views/Signup.vue'),
    },
    {
      path: '/signin',
      name: 'signin',
      component: () => import('@/views/Signin.vue'),
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: () => import('@/views/Dashboard.vue'),
      meta: {
        requiresAuth: true
      },
    },
    {
      path: '/recipe/:id', component: () => import('@/views/Recipe.vue'),
      meta: {
        requiresAuth: true
      },
      children: [
        {
          path: 'edit',
          component: () => import('@/views/RecipeEdit.vue'),
        },
      ],
    },
  ],
})
