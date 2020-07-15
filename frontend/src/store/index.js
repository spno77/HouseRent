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
}

const mutations = {
	UPDATE_HOUSES (state,payload) {
		state.houses = payload
	},

	LOGIN_USER(state,payload){
		state.user = payload
	},

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
	},
}

const getters = {
	houses: state => state.houses,
	tuser:  state => state.user,
}


const store = new Vuex.Store({
	state,
	mutations,
	actions,
	getters
})

export default store