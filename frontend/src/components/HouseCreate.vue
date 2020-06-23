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
            cost: this.cost
          })
      },
    }
  }
</script>


<style scoped>
  
.ti{

  color: lightblue;
  text-align: center;

}

</style>