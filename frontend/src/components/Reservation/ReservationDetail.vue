<template>
<div>
		<h1> <b>House name: {{ reservation.house }} </b></h1>
		<b>Reservation from: </b> {{ reservation.reserve_in }}
    <b>To: </b> {{ reservation.reserve_out }} <br>
    <p> Total cost is: {{ reservation.cost }} $ </p>
		
	
    <router-link :to="{name: 'review',params: { id: this.idd }}" class="btn btn-success">Add Review</router-link>

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
      .get(`https://127.0.0.1:8000/api/v1/reservations/${ this.idd }`)
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
