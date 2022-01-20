import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'

import router from './router/routes'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

Vue.use(VueRouter)
Vue.use(IconsPlugin)
// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router
}).$mount('#app')