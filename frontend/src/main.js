import Vue from 'vue'
import App from './App.vue'

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import HouseDetail from './components/House/HouseDetail.vue' 
import HouseList   from './components/House/HouseList.vue'
import HouseDelete   from './components/House/HouseDelete.vue'
import HouseCreate   from './components/House/HouseCreate.vue'
import HouseEdit   from './components/House/HouseEdit.vue'
import Header   from './components/Header.vue'

import RegisterUser from './components/User/RegisterUser.vue'
import LoginUser from './components/User/LoginUser.vue'
import UserProfile from './components/User/UserProfile.vue'


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
		name: 'list', 
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
	{
		path: '/houses/edit/:id/',
		name: 'edit',
		component: HouseEdit,
		props: true
	},
	{
		path: '/register',
		name: 'register',
		component: RegisterUser,
		props: true
	},
	{
		path: '/login',
		name: 'login',
		component: LoginUser,
		props: true
	},
	{
		path: '/profile/:id',
		name: 'profile',
		component: UserProfile,
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
