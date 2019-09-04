import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from '@/plugins/vuetify'

Vue.config.productionTip = false

/**
 * ログイン認証
 */
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.getters.loggedin) {
      next({
        path: '/signin',
        query: { redirect: to.fullPath }
      })
    } else {
      next()
    }
  } else {
    next()
  }
})

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount('#app')
