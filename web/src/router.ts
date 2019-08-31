import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home.vue'
import Signup from '@/views/Signup.vue'
import Signin from '@/views/Signin.vue'
import Dashboard from '@/views/Dashboard.vue'
import Recipe from '@/views/Recipe.vue'
import RecipeEdit from '@/views/RecipeEdit.vue'

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
      component: Signup,
    },
    {
      path: '/signin',
      name: 'signin',
      component: Signin,
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard,
      meta: {
        // requiresAuth: true
      },
    },
    {
      path: '/recipe/:id', component: Recipe,
      meta: {
        // requiresAuth: true
      },
      children: [
        {
          path: 'edit',
          component: RecipeEdit,
        },
      ],
    },
  ],
})
