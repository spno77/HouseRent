import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'

Vue.use(Vuex)

const state = {
	houses: [],
	host_houses: [],
	user: {
		username: '',
		password: '',
		is_staff: null
	},
	isLoggedIn: false,
	reservations: [],
	token: '',
	
	search_term: {
		country: '',
		city: '',
		book_from: '',
		book_to: '',
		people_num: '',
		type: '',
        heat: '',
        garage: '',
        wifi: '',
        aircondition: '',
        clicked: ''
	},

	images:[] , 
}

const mutations = {
	UPDATE_HOUSES (state,payload) {
		state.houses = payload
	},

	UPDATE_HOST_HOUSES (state,payload) {
		state.host_houses = payload
	},

	UPDATE_HOUSE_IMAGES (state,payload) {
		state.images = payload
	},
	
	LOGIN_USER(state,payload) {
		state.user = payload
	},

	iS_LOGGED_IN(state) {
		state.isLoggedIn = true
	},

	iS_NOT_LOGGED_IN(state) {
		state.isLoggedIn = false
	},
	UPDATE_RESERVATIONS(state,payload) {
		state.reservations = payload
	},
	UPDATE_TOKEN(state,payload) {
		state.token = payload
	},
	UPDATE_SEARCH_TERM(state,payload) {
		state.search_term = payload
	},
	UPDATE_IS_STAFF(state,payload){
		state.user.is_staff = payload
	}

}

const actions = {
	getHouses ({ commit }) {
		axios.get('https://127.0.0.1:8000/api/v1/houses/?ordering=cost').then((response) => {
		commit('UPDATE_HOUSES', response.data)
		});
	},
	getHostHouses({ commit }){
		axios.get('https://127.0.0.1:8000/api/v1/host/houses/?ordering=cost/',
		{headers: {'Authorization': 'JWT ' + state.tuser.token}} )
		.then((response) => {
			commit('UPDATE_HOST_HOUSES', response.data)
		});
	},
	getHousesImages ({ commit }) {
		axios.get('https://127.0.0.1:8000/api/v1/houses/images'
			).then((response) => {
		commit('UPDATE_HOUSE_IMAGES', response.data)
		});
	},
	searchHouses({ commit },search_term) {
		if(state.search_term.clicked===true){
			axios.get('https://127.0.0.1:8000/api/v1/houses/?country='+ search_term.country 
					+'&city='+search_term.city+'&people_num='+search_term.people_num
					+'&book_from='+search_term.book_from
					+'&book_to='+search_term.book_to
					+'&house_type='+search_term.type
					+'&heat='+search_term.heat
					+'&garage='+search_term.garage
					+'&wifi='+search_term.wifi
					+'&aircondition='+search_term.aircondition
					+ '&ordering=cost')
			.then((response) => {
			commit('UPDATE_HOUSES', response.data)
			});
		}else{
			axios.get('https://127.0.0.1:8000/api/v1/houses/?country='+ search_term.country 
					+'&city='+search_term.city+'&people_num='+search_term.people_num
					+'&book_from='+search_term.book_from
					+'&book_to='+search_term.book_to+ '&ordering=cost')
		.then((response) => {
			commit('UPDATE_HOUSES', response.data)
		});
			
		}  
	},
	loginUser ({ commit }, user) {
		axios.post('https://127.0.0.1:8000/api/v1/rest-auth/login/',user)
		.then((response) => {
			if(response.data.user.is_approved){
				commit('LOGIN_USER', response.data)
				commit('iS_LOGGED_IN')
			}else{
				alert("Your approvement is pending")
			}
		});	
	},
	logoutUser({ commit }){
		axios.post('https://127.0.0.1:8000/api/v1/rest-auth/logout/').then((response) => {
		commit('LOGIN_USER',null)
		});
		commit('iS_NOT_LOGGED_IN')
	},
	getReservations ({ commit }) {
		axios
			.get('https://127.0.0.1:8000/api/v1/reservations/',
			{headers: {'Authorization': 'JWT ' + state.tuser.token}}  
		)
			.then((response) => {commit('UPDATE_RESERVATIONS',response.data)
		});
	},
	updateSearchTerm({ commit },search_term) {
		commit('UPDATE_SEARCH_TERM',search_term);
	},
}
	

const getters = {
	houses: 	  state => state.houses,
	host_houses:  state => state.host_houses,
	house_images: state => state.images,
	tuser:  	  state => state.user,
	isLoggedIn:   state => state.isLoggedIn,
	reservations: state => state.reservations,
	search_term:  state => state.search_term,
	is_staff:     state => state.user.username
}


const store = new Vuex.Store({
	state,
	mutations,
	actions,
	getters
})

export default store