import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'

Vue.use(Vuex)

const state = {
	houses: []
}

const mutations = {
	UPDATE_HOUSES (state,payload) {
		state.houses = payload
	}
}

const actions = {
	getHouses ({ commit }) {
		axios.get('http://127.0.0.1:8000/api/v1/houses/?ordering=cost').then((response) => {
		commit('UPDATE_HOUSES', response.data)
		});
	}
}

const getters = {
	houses: state => state.houses
}


const store = new Vuex.Store({
	state,
	mutations,
	actions,
	getters
})

export default store