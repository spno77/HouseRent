import Vue from 'vue'
import App from './App.vue'

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import HouseDetail from './components/HouseDetail.vue' 
import HouseList   from './components/HouseList.vue'
import HouseDelete   from './components/HouseDelete.vue'
import HouseCreate   from './components/HouseCreate.vue'
import Header   from './components/Header.vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import axios from 'axios'
import VueAxios from 'vue-axios'

import VueRouter from 'vue-router'

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

Vue.config.productionTip = false

Vue.use(VueAxios,axios)

Vue.use(VueRouter)

Vue.use(Header)

const routes = [
	{
		path: '/' ,
		component:HouseList, 
		props: true
	},
	{
		path: '/houses/:id',
		name: 'houses',
		component:HouseDetail,
		props: true 
	},
	{
		path: '/houses/:id/delete',
		name: 'delete',
		component: HouseDelete,
		props: true
	},
	{
		path: '/houses/create',
		name: 'create',
		component: HouseCreate,
		props: true
	},

]

const router = new VueRouter({
	routes,
	mode: 'history'
})

new Vue({
  render: h => h(App),
  router,
}).$mount('#app')
