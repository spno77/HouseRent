<template>
<div>
<h1> <b>{{ house.title }} </b></h1>
 <b-jumbotron header-level="4" >
  <div class="row">
    <div class="col-md-7" >
		
		<p> {{ house.description }} </p>
    <p> Country: {{ house.country }} </p>
    <p> City:    {{ house.city }} </p>
		<p> cost : {{ house.cost }} $ </p>
		<p> Garage:{{ house.garage }} </p>
		<p> wifi:{{ house.wifi }} </p>
		<p> Aircondition:{{ house.aircondition }} </p>
   </div>

   <span class="col-md-5 imgContainer">
      <img :src="house.image">
   </span> 

  </div> 
        <b-container>
          <div id="map"  class="map">
          </div>
        </b-container> 

</b-jumbotron>

		<div class="imgButton">
      <router-link :to="{name: 'reviewlist', params: { id: this.idd }}" class="btn btn-warning">Show Reviews</router-link>
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
 
import L from 'leaflet';
import { LMap, LTileLayer, LMarker } from 'vue2-leaflet';

export default {
  name: 'HouseDetail',
  
  data(){
    return {
      house:{
        
      },
      idd:       this.$route.params.id,
      map:       null,
      tileLayer: null,
      markers:   [],
      latt:  null,
    }
  },

  computed:{
      ...mapGetters([
        'tuser',
        'isLoggedIn'
      ]),
    },


   created(){
    this.getHouse();
  },

  methods:{
    getHouse(){
     axios
        .get(`http://127.0.0.1:8000/api/v1/houses/${ this.idd }`)
        .then(response =>{ (this.house = response.data)
           this.$nextTick(() => this.initMap());
        })

    },

    initMap() { 
        
          this.map = L.map('map').setView([this.house.lat,this.house.lon], 16);
 
          this.markers = L.marker([this.house.lat,this.house.lon]).addTo(this.map)

          this.tileLayer =  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          }).addTo(this.map);

    },


  }


}
</script>

<style scoped>
  .imgButton{
    text-align:center;
    margin-top:5px;
}

.row {
  display: flex;
}

.column {
  flex: 20.33%;
}

.img {
    float: left;
    width:  200px;
    height: 200px;
    object-fit: cover;
}

.map { 
  height: 300px;
}



</style>
