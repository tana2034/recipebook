import Vue from 'vue'
import Vuetify from 'vuetify'
import { shallowMount } from '@vue/test-utils'
import RecipeEdit from '@/views/RecipeEdit.vue'

Vue.use(Vuetify)

describe('RecipeEdit.vue', () => {
  test('isVueInstance', () => {
    const wrapper = shallowMount(RecipeEdit)
    expect(wrapper.isVueInstance()).toBeTruthy()
  })
})
