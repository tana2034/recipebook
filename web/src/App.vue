<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title class="headline text-uppercase">
        <span class="font-weight-light">Recipebook</span>
      </v-toolbar-title>
      <v-spacer />
      <v-btn flat to="/signin">Sign In</v-btn>
      <v-btn flat to="/signup">Sign Up</v-btn>
    </v-app-bar>

    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'App',
  data: () => ({
    //
  }),
})
</script>
