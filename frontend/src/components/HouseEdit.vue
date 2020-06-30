<template>
    <div>
        <app />
        <div>
             <h1 class="ti">   Edit House  </h1>
         <b-container>   
          <b-form  v-if="show">
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
          v-model="house.rooms"
          required
          placeholder="Enter room number"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Cost:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="house.cost"
          required
          placeholder="Enter cost"
        ></b-form-input>
      </b-form-group>

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

     <b-form-file
      v-model="file"
      :state="Boolean(file)"
      placeholder="Choose a file or drop it here..."
      drop-placeholder="Drop file here..."
    ></b-form-file>
   

      <b-button  v-on:click="editHouse" variant="primary"> Edit </b-button>
    </b-form>
   
     </b-container>
      </div>
    </div>
</template>


<script>
 import axios from 'axios';

 export default{
    data(){
      
      return {
        idd : this.$route.params.id,
        
        house: {
          title: '',
          description: '',
          cost: '',
          rooms: '',
          garage: true,
          wifi: true,
          aircondition: true,
          file: null,
        },
        show: true
     }
    },

    mounted(){
      axios
        .get('http://127.0.0.1:8000/api/v1/houses/'+ this.idd)
        .then( response => {
           this.house = response.data
        })
     }, 

    methods:{
        
      editHouse() {
        axios
          .put('http://127.0.0.1:8000/api/v1/houses/'+ this.idd+ '/',{
            title : this.house.title,
            description: this.house.description,
            rooms: this.house.rooms,
            cost: this.house.cost,
            garage: this.house.garage,
            wifi:   this.house.wifi,
            aircondition: this.house.aircondition,
            
          })
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

 