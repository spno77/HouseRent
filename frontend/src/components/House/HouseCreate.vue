<template>
    <div>
        <app />
        <h1 class="ti">   Create House  </h1>
        
             
        <b-container>
           <b-form v-if="show">
            <div class="row">
        
         
            <div class="col-md-6">
      <b-form-group
        id="input-group-1"
        label="Title:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="house.title"
          required
          placeholder="Enter title"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Description:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="house.description"
          required
          placeholder="Enter description"
        ></b-form-input>
      </b-form-group>

    

      <b-form-group id="input-group-2" label="Rooms:" label-for="input-2">
        <b-form-input
          id="input-2"
          type="number"
          v-model="house.rooms"
          required
          placeholder="Enter room number"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Cost:" label-for="input-2">
        <b-form-input
          id="input-2"
          type="number"
          v-model="house.cost"
          required
          placeholder="Enter cost"
        ></b-form-input>
      </b-form-group>
</div>
<div class="col-md-6">


     <b-form-group
        id="input-group-1"
        label="Country:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="house.country"
          required
          placeholder="Enter country"
        ></b-form-input>
      </b-form-group>

      <div>
        <label for="example-datepicker">Available From:</label>
        <b-form-datepicker id="example-datepicker" v-model="house.av_from" class="mb-2"></b-form-datepicker>
      </div>


      <div>
        <label for="example-datepicker2">Available To:</label>
        <b-form-datepicker id="example-datepicker2" v-model="house.av_to" class="mb-2"></b-form-datepicker>
      </div>


       <b-form-group
        id="input-group-1"
        label="City:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="house.city"
          required
          placeholder="Enter city"
        ></b-form-input>
      </b-form-group>

 <b-form-file
     @change="onFileSelected"
      v-model="house.image"
      placeholder="Choose an image or drop it here..."
      drop-placeholder="Drop image here..."
    ></b-form-file>
    

     <b-form-group label="Garage:">
      <b-form-radio-group class="pt-2">
        <b-form-radio v-model="house.garage" value = "true">True</b-form-radio>
        <b-form-radio v-model="house.garage" value = "false">False</b-form-radio>
      </b-form-radio-group>
    </b-form-group>




    <b-form-group label="Wifi:">
      <b-form-radio-group class="pt-2">
        <b-form-radio v-model="house.wifi" value = "true">True</b-form-radio>
        <b-form-radio v-model="house.wifi" value = "false">False</b-form-radio>
      </b-form-radio-group>
    </b-form-group>

    <b-form-group label="Aircondition:">
      <b-form-radio-group class="pt-2">
        <b-form-radio v-model="house.aircondition" value = "true">True</b-form-radio>
        <b-form-radio v-model="house.aircondition" value = "false">False</b-form-radio>
      </b-form-radio-group>
    </b-form-group>

    
</div>
   
 
</div>

     </b-form>
         
     </b-container>


              <b-container>

               <div id="map" class="map">
                
               </div>
             </b-container> 
       
      <b-button  v-on:click="onSubmit" variant="primary">Submit</b-button>
    

    </div>
</template>


<script>
 import axios from 'axios';
 import { mapGetters } from 'vuex';

 import L from 'leaflet';
 import { LMap, LTileLayer, LMarker } from 'vue2-leaflet';
  
  export default {

    data() {
      return {
        
        house:{  
          title: '',
          description: '',
          cost: '',
          rooms: '',
          garage: true,
          wifi: true,
          aircondition: true,
          country: '',
          city: '',
          image: '',
          lon: '',
          lat: '',
          av_from: '',
          av_to: '',
        },

        map: null,
        tileLayer: null,
        //marker: null,
        markers: [],

        show: true
      }
    },

    mounted() {
      this.initMap();

    },

    computed:{
      ...mapGetters([
        'tuser'
      ])
    },

    methods: {


      initMap() {
        this.map = L.map('map').setView([38.63, -90.23], 12);

        //this.markers = L.marker([38.63,-90.23]).addTo(this.map)

        this.tileLayer =  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
         attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(this.map);

        this.map.on('click', function(e) {

          console.log("Lat, Lon : " + e.latlng.lat + ", " + e.latlng.lng)
          console.log(e.latlng)
          this.house.lon = e.latlng.lng
          this.house.lat = e.latlng.lat

          L.marker([e.latlng.lat, e.latlng.lng]).addTo(this.map)
          .bindPopup('<b> My home location </b>')
          .openPopup();
      },this)

      
    },

   
      onFileSelected(event){
        this.image = event.target.files[0]
      },
     
      onSubmit() {
        const fd = new FormData()

        fd.append('title'       ,this.house.title)
        fd.append('description' ,this.house.description)
        fd.append('cost'        ,this.house.cost)
        fd.append('rooms'       ,this.house.rooms)
        fd.append('garage'      ,this.house.garage)
        fd.append('wifi'        ,this.house.wifi)
        fd.append('aircondition',this.house.aircondition)
        fd.append('country'     ,this.house.country)
        fd.append('city'        ,this.house.city)
        fd.append('host'        ,this.tuser.user.id)
        fd.append('image'       ,this.house.image,this.house.image.name)

        fd.append('lon'         ,this.house.lon)
        fd.append('lat'         ,this.house.lat)

        fd.append('av_from'     ,this.house.av_from)
        fd.append('av_to'       ,this.house.av_to)
        

        axios
          .post('http://127.0.0.1:8000/api/v1/houses/',fd,
           {headers: {'Authorization': 'JWT ' + this.tuser.token}}  
          )
          .catch((err) => {
             console.log(err.response.data);
           });
        this.$router.push('/')
       
      },
       
    }
  }

</script>


<style scoped>
  
.ti{

  color: lightblue;
  text-align: center;

}

.map { 
  height: 300px;
}



</style>