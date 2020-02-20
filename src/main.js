// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'

Vue.prototype.$axios = axios

import Vant from 'vant'
import 'vant/lib/index.css'
Vue.use(Vant);

import '@vant/touch-emulator';

import areaList from './api/areaList'
Vue.prototype.$area = areaList

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
