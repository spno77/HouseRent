<template>
  <div>
   <app /> 
   <b-container>

    <h1 class="ti"> Houses Info </h1>
     <b-row  align-v="center">
  
       
        <b-col md="3" v-for="house in houses" :key="house.id">
          <b-card
            bg-variant="dark" text-variant="white"
            :title="house.title"
            :img-src ="house.image" 
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 20rem;"
            class="mb-2"
           >
              <b-card-text>
              <b>cost: {{ house.cost }} $ </b> <br>
              <b>Reviews :{{ house.reviews.length }} </b><br>
              <div v-show="house.reviews.length > 0">
              <b>Avg rating : {{ avg_rating(house) }} </b>
              </div>
              
            </b-card-text>

            <router-link :to="{name: 'houses', params: { id: house.id }}" class="btn btn-primary">Info</router-link>
          </b-card>
        </b-col> 
     
    </b-row>
     
  </b-container>
  </div>
</template>



<script>
//import axios from 'axios';
import { mapGetters } from 'vuex';

export default {
  name: 'HouseSearch',
 
  data(){
   return {
     idd : this.$route.params.id,
     
    
    }

  },

  computed:{
    ...mapGetters([
        'houses',
        'search_term'
      ])
  },

  mounted(){
    this.$store.dispatch('searchHouses',this.search_term);
     
  },

   methods:{

    avg_rating(house){
      var total = 0;

      for(var i = 0; i < house.reviews.length; i++) {
        total += house.reviews[i].rating; 
      }

      var avg = total / house.reviews.length;
      return avg;
    },

  }
 
 } 


</script>

<style scoped>
  
.ti{

  color: lightblue;
  text-align: center;

}

.ll {
  max-width: 100%;
  max-height: 80%;
  width: auto;

  display: block;
  margin: 0 auto
}


.img {
    float: left;
    width:  300px;
    height: 300px;
    background-size: cover;
}

</style>