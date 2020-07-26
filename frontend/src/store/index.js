import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'

Vue.use(Vuex)

const state = {
	houses: [],
	user: {
		username: '',
		password: '',
	},
	isLoggedIn: false
}

const mutations = {
	UPDATE_HOUSES (state,payload) {
		state.houses = payload
	},

	LOGIN_USER(state,payload){
		state.user = payload
	},

	iS_LOGGED_IN(state){
		state.isLoggedIn = true
	}

}

const actions = {
	getHouses ({ commit }) {
		axios.get('http://127.0.0.1:8000/api/v1/houses/?ordering=cost').then((response) => {
		commit('UPDATE_HOUSES', response.data)
		});
	},
	loginUser ({ commit }, user) {
		axios.post('http://127.0.0.1:8000/api/v1/rest-auth/login/',user).then((response) => {
		commit('LOGIN_USER', response.data)
		});
		commit('iS_LOGGED_IN')
	},
}

const getters = {
	houses: 	state => state.houses,
	tuser:  	state => state.user,
	isLoggedIn: store => state.isLoggedIn
}


const store = new Vuex.Store({
	state,
	mutations,
	actions,
	getters
})

export default store