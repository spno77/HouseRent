<template>
  <div>
   <b-container>
    <h1 class="ti"> My Houses </h1>
    <div class="overflow-auto">
    <b-pagination v-model="currentPage" :total-rows="rows" :per-page="perPage"> 
    </b-pagination>
      <b-row  align-v="center">

        <b-col md="3" v-for="(house, index) in houses.slice(this.perPage*(currentPage-1),this.perPage*(currentPage))" :key="index">

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
              <b>Cost: {{ house.cost }} $ </b> <br>
              <b>Type: {{ house.house_type }} </b><br>
              <b>Beds number :{{ house.beds }} </b><br>
              <b>Reviews :{{ house.reviews.length }} </b><br>

              <div v-show="house.reviews.length > 0">
              <b>Avg rating : {{ avg_rating(house) }} </b>
              </div>
              
            </b-card-text>

            <router-link :to="{name: 'houses', params: { id: house.id }}" class="btn btn-primary">Info</router-link>
          </b-card>
        </b-col> 
     
    </b-row>

    <b-pagination v-model="currentPage" :total-rows="rows" :per-page="perPage"> 
    </b-pagination>

    </div>
  </b-container>
  </div>
</template>



<script>
import axios from 'axios';
import { mapGetters } from 'vuex';

export default {
  name: 'HostHouses',
 
  data(){
    return {
      perPage: 12,
      currentPage: 1,
      houses:[],
    }
  },
  computed:{
    ...mapGetters([
        'tuser',
      ]),
    rows() {
        return this.houses.length
      }
  },

  mounted(){
    axios
      .get('http://127.0.0.1:8000/api/v1/host/houses/?ordering=cost',
       {headers: {'Authorization': 'JWT ' + this.tuser.token}}  
      )
      .then(response => (this.houses = response.data))
        
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
    object-fit: cover;
}

</style>