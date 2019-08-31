import Vue from 'vue'
import Vuetify from 'vuetify'
import { shallowMount } from '@vue/test-utils'
import Signup from '@/views/Signup.vue'

Vue.use(Vuetify)

describe('Signup.vue', () => {
  test('isVueInstance', () => {
    const wrapper = shallowMount(Signup)
    expect(wrapper.isVueInstance()).toBeTruthy()
  })
})
