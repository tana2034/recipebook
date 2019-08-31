import Vue from 'vue'
import Vuetify from 'vuetify'
import { shallowMount } from '@vue/test-utils'
import Dashboard from '@/views/Dashboard.vue'

Vue.use(Vuetify)

describe('Dashboard.vue', () => {
  test('isVueInstance', () => {
    const wrapper = shallowMount(Dashboard)
    expect(wrapper.isVueInstance()).toBeTruthy()
  })
})
