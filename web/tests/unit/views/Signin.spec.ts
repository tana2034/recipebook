import Vue from 'vue'
import Vuetify from 'vuetify'
import { shallowMount } from '@vue/test-utils'
import Signin from '@/views/Signin.vue'

Vue.use(Vuetify)

describe('Signin.vue', () => {
  test('isVueInstance', () => {
    const wrapper = shallowMount(Signin)
    expect(wrapper.isVueInstance()).toBeTruthy()
  })
})
