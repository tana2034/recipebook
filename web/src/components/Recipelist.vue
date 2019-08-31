<template>
    <v-container>
        <template v-for="item in items">
        <v-row :key="item">
            <v-col>
                <v-card
                    max-width="344"
                    class="mx-auto"
                >
                    <v-card-title>{{ item.title }}</v-card-title>
                    <v-card-text>{{ item.description }}</v-card-text>
                    <v-card-actions>
                    <v-btn link>Link</v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
        </v-row>
        </template>
    </v-container>
</template>

<script lang="ts">
import Vue from 'vue'
import axios from 'axios'
import { Component } from 'vue-property-decorator'

interface Recipe {
    url: string,
    title: string,
    description: string,
    user_id: string,
}

@Component
export default class Recipelist extends Vue {
    public items?: Recipe[] = []

    public mounted() {
        axios.get('http://localhost:5000/all').then((res) => {
            this.items = res.data
        })
    }
}
</script>