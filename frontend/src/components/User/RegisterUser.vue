<template>
    <div>
        <app />
        <div>
        <h1 class="ti">  Register User </h1>
        
         <b-container>	
          <b-form  v-if="show">
      <b-form-group id="input-group-1" label="Username:" label-for="input-1">
        <b-form-input
          id="input-1"
          v-model="user.username"
          required
          placeholder="Enter Username"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Email:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="user.email"
          type="email"
          required
          placeholder="Enter Email"
        ></b-form-input>
      </b-form-group>

       <b-form-group id="input-group-1" label="Firstname:" label-for="input-1">
        <b-form-input
          id="input-1"
          v-model="user.firstname"
          required
          placeholder="Enter Firstname"
        ></b-form-input>
      </b-form-group>

       <b-form-group id="input-group-1" label="Lastname:" label-for="input-1">
        <b-form-input
          id="input-1"
          v-model="user.lastname"
          required
          placeholder="Enter Lastname"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-1" label="Phone:" label-for="input-1">
        <b-form-input
          id="input-1"
          v-model="user.phone"
          required
          placeholder="Enter Phone"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Role:" label-for="input-2">
          <b-form-select v-model="user.role" :options="user.options"> </b-form-select> 
      </b-form-group>     

      <b-form-group id="input-group-2" label="Password:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="user.password1"
          type="password"
          required
          placeholder="Enter password"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Password:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="user.password2"
          type="password"
          required
          placeholder="Re-enter password"
        ></b-form-input>
      </b-form-group>

       <b-form-file @change="onFileSelected" v-model="user.image"
       placeholder="Choose an image or drop it here..."
       drop-placeholder="Drop image here..."
       ></b-form-file>


      <b-button  v-on:click="onSubmit" variant="primary"> Register </b-button>
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
      user: {
        role: null,
        options: [
          { value: null, text: 'Please select a role' },
          { value: 'host', text: 'Host' },
          { value: 'tenant', text: 'Tenant' },
        ],

        username: '',
        email: '',
        password1: '',
        password2: '',
        firstname: '',
        lastname: '',
        phone: '',
        image: '',
      }, 
      show: true
      
      }
    },

    methods: {

      onFileSelected(event){
       this.user.image = event.target.files[0]     
      },

      onSubmit() {
        const fd = new FormData()

        fd.append('username' ,this.user.username)
        fd.append('firstname',this.user.firstname)
        fd.append('lastname' ,this.user.lastname)
        fd.append('phone'    ,this.user.phone)
        fd.append('email'    ,this.user.email)
        fd.append('password1',this.user.password1)
        fd.append('password2',this.user.password2)
        fd.append('role'     ,this.user.role)
        fd.append('image'    ,this.user.image,this.user.image.name)

        axios
          .post('http://127.0.0.1:8000/api/v1/rest-auth/registration/',fd)
          .catch((err) => {
             console.log(err.response.data);
           });
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