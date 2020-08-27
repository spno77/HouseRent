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
     @change="onFileSelected"
      v-model="house.image"
      placeholder="Choose an image or drop it here..."
      drop-placeholder="Drop image here..."
    ></b-form-file>
    


      <b-button  v-on:click="onSubmit" variant="primary">Submit</b-button>
     
    </b-form>
         
     </b-container>
      </div>
    </div>
</template>


<script>
 import axios from 'axios';
 import { mapGetters } from 'vuex';
  
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
        },

        show: true
      }
    },

    computed:{
      ...mapGetters([
        'tuser'
      ])
    },

    methods: {
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



</style>