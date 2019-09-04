import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  getters: {
    loggedin: state => {
      return state.loggedin
    }
  },
  state: {
    'loggedin': false
  },
  mutations: {
    login(state) {
      state.loggedin = true
    },
    logout(state) {
      state.loggedin = false
    }
  },
  actions: {
    loginSuccess({ commit }) {
      commit('login')
    },
    logoutSuccess({ commit }) {
      commit('logout')
    }
  },
})
