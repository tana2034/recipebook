<template>
  <Recipelist />
</template>

<script lang="ts">
import Vue from 'vue'
import { Inject, Component } from 'vue-property-decorator'
import Recipelist from '@/components/Recipelist.vue'

@Component({
  components: { Recipelist },
})
export default class HomeView extends Vue {}
</script>
