<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title class="headline text-uppercase">
        <span class="font-weight-light">Recipebook</span>
      </v-toolbar-title>
      <v-spacer />
      <v-btn v-if="!$store.getters.loggedin" to="/signin">Sign In</v-btn>
      <v-btn v-if="!$store.getters.loggedin" to="/signup">Sign Up</v-btn>
      <v-btn v-if="$store.getters.loggedin" @click="signout">Sign Out</v-btn>
    </v-app-bar>

    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue'
import axios from 'axios'

export default Vue.extend({
  name: 'App',
  data: () => ({
  }),
  methods: {
    signout() {
      axios
      .post(
          '/signout'
      ).then(
          (response) => {
            this.$store.dispatch('logoutSuccess')
            this.$router.push({ path: '/' })
          },
      ).catch((error: any) => {
          alert('ログアウトできませんでした')
      })
    }
  }
})
</script>
