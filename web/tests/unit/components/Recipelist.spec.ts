import Vue from 'vue'
import Vuetify from 'vuetify'
import { shallowMount } from '@vue/test-utils'
import Recipelist from '@/components/Recipelist.vue'

Vue.use(Vuetify)

describe('Recipelist.vue', () => {
  test('isVueInstance', () => {
    const wrapper = shallowMount(Recipelist)
    expect(wrapper.isVueInstance()).toBeTruthy()
  })
})
