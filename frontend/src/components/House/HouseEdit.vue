<template>
  <div>
    <h1 class="ti">   Edit House  </h1>           
      <b-container>
        <b-form v-if="show">
          <div class="row">
            <div class="col-md-6">
      
              <b-form-group id="input-group-1" label="Title:" label-for="input-1">
              <b-form-input
                id="input-1"
                v-model="house.title"
                required
                placeholder="Enter title"
              ></b-form-input>
              </b-form-group>

              <b-form-group id="input-group-2" label="House Rules:" label-for="input-2">
              <b-form-input
                id="input-2"
                v-model="house.rules"
                required
                placeholder="Enter house rules"
              ></b-form-input>
              </b-form-group>

              <b-form-group id="input-group-2" label="Max number of people:" label-for="input-2">
              <b-form-input
                id="input-2"
                type="number"
                v-model="house.people_max"
                required
                placeholder="Enter max number of people"
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
     
              <b-form-group id="input-group-2" label="Bedrooms:" label-for="input-2">
                <b-form-input
                  id="input-2"
                  type="number"
                  v-model="house.bedrooms"
                  required
                  placeholder="Enter bedroom number"
                ></b-form-input>
              </b-form-group>

              <b-form-group id="input-group-2" label="Beds:" label-for="input-2">
                <b-form-input
                  id="input-2"
                  type="number"
                  v-model="house.beds"
                  required
                  placeholder="Enter beds number"
                ></b-form-input>
              </b-form-group>

              <b-form-group label="Garage:">
                <b-form-radio-group class="pt-2">
                  <b-form-radio v-model="house.garage" value = "true">True</b-form-radio>
                  <b-form-radio v-model="house.garage" value = "false">False</b-form-radio>
                </b-form-radio-group>
              </b-form-group>
    
              <b-form-group label="Heat:">
                <b-form-radio-group class="pt-2">
                  <b-form-radio v-model="house.heat" value = "true">True</b-form-radio>
                  <b-form-radio v-model="house.heat" value = "false">False</b-form-radio>
                </b-form-radio-group>
              </b-form-group>

              <b-form-group id="input-group-1" label="Country:" label-for="input-1">
                <b-form-input
                  id="input-1"
                  v-model="house.country"
                  required
                  placeholder="Enter country"
                ></b-form-input>
              </b-form-group>

              <div>
                <label for="example-datepicker">Available From:</label>
                <b-form-datepicker id="example-datepicker" v-model="house.av_from" class="mb-2">
                </b-form-datepicker>
              </div>

              <b-form-group id="input-group-2" label="Transport Description:" label-for="input-2">
                <b-form-input
                  id="input-2"
                  v-model="house.transport_desc"
                  required
                  placeholder="Enter transport description"
                ></b-form-input>
              </b-form-group>
        </div>

            <div class="col-md-6">

              <b-form-group id="input-group-2" label="Description:" label-for="input-2">
                <b-form-input
                id="input-2"
                v-model="house.description"
                required
                placeholder="Enter description"
                ></b-form-input>
              </b-form-group>

              <b-form-group id="input-group-2" label="Number of people:" label-for="input-2">
                 <b-form-input
                   id="input-2"
                   type="number"
                   v-model="house.people_num"
                   required
                   placeholder="Enter number of people"
                 ></b-form-input>
               </b-form-group>
               
                <b-form-group id="input-group-2" label="House Type:" label-for="input-2">
                <b-form-select v-model="house.house_type" :options="options"> </b-form-select> 
              </b-form-group>   
             
              <b-form-group id="input-group-2" label="Extra Cost:" label-for="input-2">
                <b-form-input
                  id="input-2"
                  type="number"
                  v-model="house.plus_cost"
                  required
                  placeholder="Enter extra cost"
                ></b-form-input>
              </b-form-group>

              <b-form-group id="input-group-2" label="Bathrooms:" label-for="input-2">
                <b-form-input
                  id="input-2"
                  type="number"
                  v-model="house.bathrooms"
                  required
                  placeholder="Enter bathroom number"
                ></b-form-input>
              </b-form-group>

              <b-form-group id="input-group-2" label="Area:" label-for="input-2">
                <b-form-input
                  id="input-2"
                  type="number"
                  v-model="house.area"
                  required
                  placeholder="Enter area"
                ></b-form-input>
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

            <b-form-group id="input-group-1" label="City:" label-for="input-1">
                <b-form-input
                  id="input-1"
                  v-model="house.city"
                  required
                  placeholder="Enter city"
                ></b-form-input>
              </b-form-group>

            <div>
              <label for="example-datepicker2">Available To:</label>
              <b-form-datepicker id="example-datepicker2" v-model="house.av_to" class="mb-2"> 
              </b-form-datepicker>
            </div>
            <br>

            <b-form-file
              @change="onFileSelected"
              v-model="house.image"
              placeholder="Choose an image or drop it here..."
              drop-placeholder="Drop image here..."
            ></b-form-file>
          
          </div> 
        </div>
        </b-form>
     </b-container>

      <b-container>
        <div id="map" class="map">
        </div>
      </b-container> 
       
      <b-button  v-on:click="editHouse" variant="primary">Edit </b-button>
    
  </div>
</template>


<script>
 import axios from 'axios';
 import { mapGetters } from 'vuex';

 import L from 'leaflet';
 import { LMap, LTileLayer, LMarker } from 'vue2-leaflet';

 export default{
    data(){
      
      return {
        idd : this.$route.params.id,
        house:{  
         
        },
        options: [
          { value: null, text: 'Please select a house type' },
          { value: 'entire_place', text: 'Entire  Place' },
          { value: 'private_room', text: 'Private Room' },
          { value: 'shared_room',  text: 'Shared  Room' },
         ],
        plus_cost: '',
        rules:'',

        map: null,
        tileLayer: null,
        //marker: null,
        markers: [],

        show: true
        
     }
    },

    computed:{
      ...mapGetters([
        'tuser'
      ])
    },

    mounted(){
      axios
        .get('https://127.0.0.1:8000/api/v1/houses/'+ this.idd)
        .then( response => {
           this.house = response.data
        })
         .catch((err) => {
           console.log(err.response.data);
           });

         this.initMap();
     }, 

    methods:{

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
        
     editHouse() {
        axios
          .put('https://127.0.0.1:8000/api/v1/houses/'+ this.idd+ '/',{
            title :       this.house.title,
            description:  this.house.description,
            rooms:        this.house.rooms,
            cost:         this.house.cost,
            garage:       this.house.garage,
            wifi:         this.house.wifi,
            aircondition: this.house.aircondition,
            city:         this.house.city,
            country:      this.house.country,
            host:         this.tuser.user.id,
            
            lon:            this.house.lon,
            lat:            this.house.lat,

            av_from:        this.house.av_from,
            av_to:          this.house.av_to,

            heat:           this.house.heat,
            area:           this.house.area,
            bedrooms:       this.house.bedrooms,
            bathrooms:      this.house.bathrooms,
            beds:           this.house.beds,
            transport_desc: this.house.transport_desc, 
            house_type:     this.house.house_type,
            people_num:     this.house.people_num ,
            people_max:     this.house.people_max ,
            plus_cost:      this.house.plus_cost, 
            rules:          this.house.rules ,
          
          },
          {headers: {'Authorization': 'JWT ' + this.tuser.token}})
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

 .imgButton{
    text-align:center;
    margin-top:5px;
}

</style>

 