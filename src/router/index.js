import Vue from 'vue'
import Router from 'vue-router'
import index from '@/components/index'
import home from '@/components/home'
import my from '@/components/my'
import detail from '@/components/detail'

import bilibili from '@/components/bilibili'

import cp from '@/components/cp'

import play from '@/components/play'

import setup from '@/components/setup'
import shop from '@/components/shop'
import address from '@/components/address'
import address2 from '@/components/address2'
import b2 from '@/components/b2'
import login from '@/components/login'
import logon from '@/components/logon'
Vue.use(Router)

export default new Router({
  routes: [{
      path: '/',
      name: 'index',
      component: home
    },
    {
      path: '/home',
      name: 'home',
      component: home
    }, {
      path: '/my',
      name: 'my',
      component: my
    }, {
      path: '/detail/:mid/:gid',
      name: 'detail',
      component: detail
    }, {
      path: '/play/:aid/:img/:play/:video_review/:title/:author',
      name: 'play',
      component: play
    }, {
      path: '/bilibili',
      name: 'bilibili',
      component: bilibili
    }, {
      path: '/setup',
      name: 'setup',
      component: setup
    }, {
      path: '/shop',
      name: 'shop',
      component: shop
    }, {
      path: '/address',
      name: 'address',
      component: address
    },
    {
      path: '/address2',
      name: 'address2',
      component: address2
    },
    {
      path: '/b2',
      name: 'b2',
      component: b2
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/logon',
      name: 'logon',
      component: logon
    },
    {
      path: '/cp/:img/:goods_name/:group_price',
      name: 'cp',
      component: cp
    },

  ]
})
