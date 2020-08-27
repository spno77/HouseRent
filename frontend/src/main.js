import Vue from 'vue'
import App from './App.vue'

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import HouseDetail from './components/House/HouseDetail.vue' 
import HouseList   from './components/House/HouseList.vue'
import HouseDelete   from './components/House/HouseDelete.vue'
import HouseCreate   from './components/House/HouseCreate.vue'
import HouseEdit   from './components/House/HouseEdit.vue'
import HouseSearch   from './components/House/HouseSearch.vue'
import HouseSearchForm   from './components/House/HouseSearchForm.vue'
import AddHouseImages    from  './components/House/AddHouseImages.vue'

import Header   from './components/Header.vue'

import RegisterUser from './components/User/RegisterUser.vue'
import LoginUser from './components/User/LoginUser.vue'
import UserProfile from './components/User/UserProfile.vue'
import UserEdit from './components/User/UserEdit.vue'

import Reservation from './components/Reservation/Reservation.vue'
import ReservationDetail from './components/Reservation/ReservationDetail.vue'
import ReservationList from './components/Reservation/ReservationList.vue'

import ReviewAdd from './components/Review/ReviewAdd.vue'
import ReviewList from './components/Review/ReviewList.vue'

import store from './store/index.js'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import axios from 'axios'
import VueAxios from 'vue-axios'

import VueRouter from 'vue-router'
import Vuex from 'vuex'


import { LMap, LTileLayer, LMarker } from 'vue2-leaflet';
import 'leaflet/dist/leaflet.css';

import { Icon } from 'leaflet';

delete Icon.Default.prototype._getIconUrl;
Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
});

Vue.component('l-map', LMap);
Vue.component('l-tile-layer', LTileLayer);
Vue.component('l-marker', LMarker);


Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

Vue.config.productionTip = false

Vue.use(VueAxios,axios)

Vue.use(VueRouter)

Vue.use(Vuex)

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
		path: '/houses_search',
		name: 'house_search',
		component: HouseSearch,
		props: true
	},
	{
		path: '/houses/search/form',
		name: 'house_search_form',
		component: HouseSearchForm,
		props: true
	},
	{
		path: '/houses/addimages/:id',
		name: 'addimages',
		component: AddHouseImages,
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
	{
		path: '/profile/edit/:id',
		name: 'editprofile',
		component: UserEdit,
		props: true
	},
	{
		path: '/reservation',
		name: 'reservation',
		component: Reservation,
		props: true
	},
	{
		path: '/reservation/:id',
		name: 'reservationdetail',
		component: ReservationDetail,
		props: true
	},
	{
		path: '/reservation/list',
		name: 'reservationlist',
		component: ReservationList,
		props: true
	},
	{
		path: '/review/',
		name: 'review',
		component: ReviewAdd,
		props: true
	},
	{
		path: '/review/list',
		name: 'reviewlist',
		component: ReviewList,
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
  store
}).$mount('#app')
