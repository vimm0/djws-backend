// vue
import Vue from 'vue';
import App from './App.vue'
import Vuetify from 'vuetify'
import VueRouter from 'vue-router'

import {routes} from './router'
Vue.use(Vuetify);
Vue.use(VueRouter);

let router = new VueRouter({mode: 'history',  routes: routes});


/* eslint-disable no-new */
// new Vue({
//   el: '#djwebshiksha-root',
//   render: h => h(App),
// });
const app = new Vue({
  el:'#djwebshiksha-root',
  router,
  components: {
  'app-home' : App
  }
});