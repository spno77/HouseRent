<template>
  <div>
   <app /> 
   <b-container>

    <h1 class="ti"> Houses Info </h1>
   
    <b-row>
       <b-card-group> 
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
              {{house.id}}
             
              
            </b-card-text>

            <router-link :to="{name: 'houses', params: { id: house.id }}" class="btn btn-primary">Info</router-link>
          </b-card>
        </b-col> 
        </b-card-group> 
    </b-row>
     
  </b-container>
  </div>
</template>



<script>
//import axios from 'axios';
import { mapGetters } from 'vuex';

export default {
  name: 'HouseList',
 
  computed:{
    ...mapGetters([
        'houses'
      ])
  },

  mounted(){
    this.$store.dispatch('getHouses'); 
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