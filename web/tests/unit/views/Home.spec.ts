import Vue from 'vue'
import Vuetify from 'vuetify'
import { shallowMount } from '@vue/test-utils'
import Home from '@/views/Home.vue'

Vue.use(Vuetify)

describe('Home.vue', () => {
  test('isVueInstance', () => {
    const wrapper = shallowMount(Home)
    expect(wrapper.isVueInstance()).toBeTruthy()
  })
})
