<template>
  <div>
      <h1 class="ti"> Reviews </h1>
       <b-list-group v-for="review in reviews" :key="review.id">
          <b-list-group-item variant="secondary">
           <td><b> {{ review.reviewer }}:   </b> </td> 
           {{ review.content }} <br>
            Rating: <b>{{ review.rating }}</b><br>
            <i> Created: {{ review.date_created }} </i>

          </b-list-group-item>
            

       </b-list-group>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import axios from 'axios';

export default { 
  name: 'ReviewList',
 
  data(){
    return {
      idd : this.$route.params.id,
      reviews: [],
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
        .get('http://127.0.0.1:8000/api/v1/houses/'+ this.idd)
        .then( response => {
           this.reviews = response.data.reviews
        })
         .catch((err) => {
           console.log(err.response.data);
           });
     }, 

}


</script>





<style scoped>
  
.ti{

  color: lightblue;
  text-align: center;
}



</style>