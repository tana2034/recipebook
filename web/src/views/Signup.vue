<template>
  <v-container>
        <v-row row>
            <v-col>
                <v-alert type="error" v-if="error">パスワードまたはユーザ名が間違っています</v-alert>
            </v-col>
        </v-row>
        <v-row row class="text-center">
            <v-col xs4 class="grey lighten-4">
                <v-card flat>
                    <v-card-title primary-title>
                        <h4>Sign Up</h4>
                    </v-card-title>
                    <v-form @submit.prevent="signin">
                        <v-card-text>
                            <v-text-field prepend-icon="person" name="Username" v-model="username" label="Username"></v-text-field>
                            <v-text-field prepend-icon="lock" name="Password" v-model="password" label="Password" type="password"></v-text-field>
                        </v-card-text>
                        <v-card-actions>
                            <v-btn primary large block type="submit">Sign Up</v-btn>
                        </v-card-actions>
                    </v-form>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script lang="ts">
import Vue from 'vue'
import Router from 'vue-router'
import { Inject, Component } from 'vue-property-decorator'
import { Store } from 'vuex/types/index';

@Component
export default class SignupView extends Vue {
    public username!: string
    public password!: string
    public error: boolean = false

    @Inject()
    public $router!: Router

    @Inject()
    public $store!: any

    public signup() {
        this.$store.dispatch('signup')
    }
}
</script>