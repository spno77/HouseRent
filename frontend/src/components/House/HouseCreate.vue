<template>
    <div>
        <app />
        <div>
             <h1 class="ti">   Create House  </h1>
         <b-container>	
          <b-form  v-if="show">
      <b-form-group
        id="input-group-1"
        label="Title:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="title"
          required
          placeholder="Enter title"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Description:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="description"
          required
          placeholder="Enter description"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Rooms:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="rooms"
          required
          placeholder="Enter room number"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Cost:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="cost"
          required
          placeholder="Enter cost"
        ></b-form-input>
      </b-form-group>

     <b-form-group label="Garage:">
      <b-form-radio-group class="pt-2">
        <b-form-radio v-model="garage" value = "true">True</b-form-radio>
        <b-form-radio v-model="garage" value = "false">False</b-form-radio>
      </b-form-radio-group>
    </b-form-group>

    <b-form-group label="Wifi:">
      <b-form-radio-group class="pt-2">
        <b-form-radio v-model="wifi" value = "true">True</b-form-radio>
        <b-form-radio v-model="wifi" value = "false">False</b-form-radio>
      </b-form-radio-group>
    </b-form-group>

    <b-form-group label="Aircondition:">
      <b-form-radio-group class="pt-2">
        <b-form-radio v-model="aircondition" value = "true">True</b-form-radio>
        <b-form-radio v-model="aircondition" value = "false">False</b-form-radio>
      </b-form-radio-group>
    </b-form-group>

     <b-form-file
      v-model="file"
      :state="Boolean(file)"
      placeholder="Choose a file or drop it here..."
      drop-placeholder="Drop file here..."
    ></b-form-file>
    <div class="mt-3">Selected file: {{ file ? file.name : '' }}</div>


      <b-button  v-on:click="onSubmit" variant="primary">Submit</b-button>
    </b-form>
   
     </b-container>
      </div>
    </div>
</template>


<script>
 import axios from 'axios';

  export default {
    data() {
      return {
        
        title: '',
        description: '',
        cost: '',
        rooms: '',
        garage: true,
        wifi: true,
        aircondition: true,
        file: null,
        
        show: true
      }
    },
    methods: {
      onSubmit() {
        axios
          .post('http://127.0.0.1:8000/api/v1/houses/',{
            title : this.title,
            description: this.description,
            rooms: this.rooms,
            cost: this.cost,
            garage: this.garage,
            wifi:   this.wifi,
            aircondition: this.aircondition,
          
          })
        this.$router.push('/')

      },

      onFileChanged(event){
        this.file = event.target.files[0]
      },

      onUpload(){

      }
      
    }
  }
</script>


<style scoped>
  
.ti{

  color: lightblue;
  text-align: center;

}

</style>