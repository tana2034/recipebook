import Vue from 'vue'
import Vuetify from 'vuetify'
import { shallowMount } from '@vue/test-utils'
import Recipe from '@/views/Recipe.vue'

Vue.use(Vuetify)

describe('Recipe.vue', () => {
  test('isVueInstance', () => {
    const wrapper = shallowMount(Recipe)
    expect(wrapper.isVueInstance()).toBeTruthy()
  })
})
