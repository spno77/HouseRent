<template>
<div>
	<app />
		<h1> <b>{{ reservation.house }} </b></h1>
		<p>{{ reservation.days }} </p>
		<p> cost : {{ reservation.cost }} $ </p>
		
		
		<div class="imgButton">
      <div v-if="isLoggedIn===true && house.host === tuser.user.username">
        <router-link :to="{name: 'edit', params: { id: this.idd }}" class="btn btn-secondary">Edit</router-link>
        <router-link :to="{name: 'delete', params: { id: this.idd }}" class="btn btn-danger">Delete</router-link>
       </div>
			<router-link v-if="isLoggedIn===true && house.host !== tuser.user.username" :to="{name: 'reservation', params: { id: this.idd }}" class="btn btn-success">Reserve</router-link>
		</div>

	</div>	
</template>

<script>
import axios from 'axios';
import { mapGetters } from 'vuex';

export default {
  name: 'ReservationDetail',
  
  data(){
    return {
      reservation : {},
      idd : this.$route.params.id
    }
  },

   computed:{
      ...mapGetters([
        'tuser',
        'isLoggedIn'
      ]),
    },
  
  mounted(){
    axios
      .get(`http://127.0.0.1:8000/api/v1/reservations/${ this.idd }`)
      .then(response => (this.reservation = response.data))
  }


}
</script>

<style>
  .imgButton{
    text-align:center;
    margin-top:5px;
}
</style>
