import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'

import router from './router/routes'
// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

Vue.use(VueRouter)
Vue.use(IconsPlugin)
// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
Vue.config.productionTip = false

//const router = new VueRouter({ routes })

new Vue({
  render: h => h(App),
  router
}).$mount('#app')