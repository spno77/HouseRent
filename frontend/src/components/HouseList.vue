<template>
  <div>
   <app /> 
   <b-container>
    <h1 class="ti"> Houses Info </h1>
    <b-row align-v="center">
        <b-col md="3" v-for="house in houses" :key="house.id">
          <b-card
           
            :title="house.title"
            :img-src ="house.image" 
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 20rem;"
            class="mb-2"
           >
            <b-card-text>
              {{ house.description}}
            </b-card-text>

            <b-button href="#" variant="primary"> Info </b-button>
          </b-card>
        </b-col>  
    </b-row>
  </b-container>
  </div>
</template>



<script>
import axios from 'axios';

export default {
  name: 'HouseList',
  
  data(){
    return {
      houses: []
    }
  },

  mounted(){
    axios
      .get('http://127.0.0.1:8000/api/v1/houses/')
      .then(response => (this.houses = response.data))
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

</style>