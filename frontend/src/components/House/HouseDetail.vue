<template>
<div>
<h1> <b>{{ house.title }} </b></h1>

 <b-jumbotron header-level="4" >
  <div class="row">
    <div class="col-md-7" >
    
    <tr><b>Place:</b></tr> <br>
    
    <p> Number of beds:        {{ house.beds }}        </p>
    <p> Number of bedrooms:    {{ house.bedrooms }}    </p>
    <p> Number of bathrooms :  {{ house.bathrooms }}   </p>
    <p> House Type :           {{ house.house_type }}        </p>
    <p> Area:                  {{ house.area }}     <span>&#13217;</span>   </p>

   </div>

   <span class="col-md-5 imgContainer">
      <br>
      <img :src="house.image">
   </span> 

  </div>

  <div class="row">

    <div class="col-md-7">
     <tr><b>Description:</b></tr> <br>
    
     <p> Description:           {{ house.description }} </p>
     <p> Rules:                 {{ house.rules }} </p>
     <p> Number of people:      {{ house.people_num }} </p>
   
  
    </div>
    <div class="col-md-5"> 
    <tr>   </tr><br>
    <br>
     <p> Max number of people:  {{ house.people_max }} </p>
     <p> Cost :                 {{ house.cost }} $     </p>
     <p> Extra Cost:            {{ house.plus_cost }} $ </p>
    
    </div>


  </div>

    <div class="row">

    <div class="col-md-7">
     <tr><b>Amenities:</b></tr> <br>
    
     <p> WiFi:                        {{ house.wifi }} </p>
     <p> Aircondition:                {{ house.aircondition }} </p>
   
  
    </div>
    <div class="col-md-5"> 
    <tr>   </tr><br>
    <br>
     <p> Heat:                  {{ house.heat }} </p>
     <p> Garage :               {{ house.garage }}  </p>
    
    </div>


  </div>

  <div class="row">

    <div class="col-md-7">
     <tr><b>Availability:</b></tr> <br>
    
       <p>Available from: {{house.av_from }} </p>
    
  
    </div>
    <div class="col-md-5"> 
    <tr>   </tr><br>
    <br>
     <p>Available to :  {{house.av_to }} </p>
    
    </div>


  </div>


<div class="row">

    <div class="col-md-7">
     <tr><b>Address:</b></tr> <br>
    
       <p>Country: {{house.country }} </p>
      
    
  
    </div>
    <div class="col-md-5"> 
    <tr>   </tr><br>
    <br>
     <p> City :  {{house.city }} </p>
    
    </div>

  </div>
  <div>
     <tr> <b>Transport description : </b>  </tr><br>
      {{ house.transport_desc }} <br>
      <br>
   </div> 



        <b-container>
          <div id="map"  class="map">
          </div>
        </b-container> 

<br>

<div class="row">
    <div class="col-md-7" >
    
    <tr><b>Host: </b></tr> <br>
    
    <p> Username:        {{ house.host.username }}        </p>
    <div v-if="isLoggedIn===true && house.host.username !== tuser.user.username">
      <router-link :to="{name: 'send_message', params: { id: this.idd }}" 
        class="btn btn-success">Send Message
      </router-link>
     </div> 
   </div>

   <span class="col-md-5 imgContainer">
      <br>
      <img :src="house.host.image">
   </span> 

  </div>



</b-jumbotron>

		<div class="imgButton">
      <router-link :to="{name: 'reviewlist', params: { id: this.idd }}" class="btn btn-warning">Show Reviews</router-link>
      <div v-if="isLoggedIn===true && house.host.username === tuser.user.username">
        <router-link :to="{name: 'edit', params: { id: this.idd }}" class="btn btn-secondary">Edit</router-link>
        <router-link :to="{name: 'delete', params: { id: this.idd }}" class="btn btn-danger">Delete</router-link>
       </div>
			<router-link v-if="isLoggedIn===true && house.host.username !== tuser.user.username" :to="{name: 'reservation', params: { id: this.idd }}" class="btn btn-success">Reserve</router-link>
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
        .get(`https://127.0.0.1:8000/api/v1/houses/${ this.idd }`)
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

    datediff(first, second) {
       var date1 = new Date(first)
       var date2 = new Date(second)

       return Math.round((date2-date1)/(1000*60*60*24));
    }


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
