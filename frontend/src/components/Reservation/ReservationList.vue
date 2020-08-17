<template>
   <div>
<h1 class="ti"> My reservations </h1>
 <b-list-group v-for="reservation in reservations" :key="reservation.id">
   <b-list-group-item> 
              cost :{{ reservation.cost }}
              days: {{ reservation.days}}
              house: {{ reservation.house }}
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
      .then(response => (this.reservations = response.data))
  },
  

}


</script>







<style scoped>
  
.ti{

  color: lightblue;
  text-align: center;

}

</style>