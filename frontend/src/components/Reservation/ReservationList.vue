<template>
   <div>
<h1 class="ti"> My reservations </h1>
 <b-list-group v-for="reservation in reservations" :key="reservation.id">
   <b-list-group-item variant="info"> 
             <div class="test"> 
              <b>House:</b> {{ reservation.house }} <br>
              <b>Days: </b> {{ reservation.days }}
              <b>Cost: </b> {{ reservation.cost }} <b> $ </b>
              <router-link :to="{name: 'reservationdetail' ,params: { id: reservation.id }}" class="le btn btn-success">Details</router-link>
             </div>
              
   </b-list-group-item>
   
 </b-list-group>
</div>
</template>

<script>
import { mapGetters } from 'vuex';
import axios from 'axios';

export default { 
  name: 'ReservationList',
 
  data(){
    return {
      reservations: []
     }
   },

   computed:{
    ...mapGetters([
        'reservations',
        'tuser',
      ])
   },

   mounted(){
    axios
      .get('http://127.0.0.1:8000/api/v1/reservations/',
       {headers: {'Authorization': 'JWT ' + this.tuser.token}}  
      )
      .then(response => (this.reservations = response.data)),
    
     this.$store.dispatch('getReservations');    

    },
  

}


</script>







<style scoped>
  
.ti{

  color: lightblue;
  text-align: center;
}

.test{
  margin-left: 10px;
}

.le{
  margin-left: 10px;
}

</style>