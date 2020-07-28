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
          v-model="username"
          required
          placeholder="Enter Username"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Email:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="email"
          type="email"
          required
          placeholder="Enter Email"
        ></b-form-input>
      </b-form-group>

       <b-form-group id="input-group-1" label="Firstname:" label-for="input-1">
        <b-form-input
          id="input-1"
          v-model="firstname"
          required
          placeholder="Enter Firstname"
        ></b-form-input>
      </b-form-group>

       <b-form-group id="input-group-1" label="Lastname:" label-for="input-1">
        <b-form-input
          id="input-1"
          v-model="lastname"
          required
          placeholder="Enter Lastname"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-1" label="Phone:" label-for="input-1">
        <b-form-input
          id="input-1"
          v-model="phone"
          required
          placeholder="Enter Phone"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Role:" label-for="input-2">
          <b-form-select v-model="role" :options="options"> </b-form-select> 
      </b-form-group>     

      <b-form-group id="input-group-2" label="Password:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="password1"
          type="password"
          required
          placeholder="Enter password"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Password:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="password2"
          type="password"
          required
          placeholder="Re-enter password"
        ></b-form-input>
      </b-form-group>


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
        
        
        show: true
      }
    },
    methods: {

      onSubmit() {
        axios
          .post('http://127.0.0.1:8000/api/v1/rest-auth/registration/',{
            username:   this.username,
            firstname:  this.firstname,
            lastname:   this.lastname,
            phone:      this.phone,
            email:      this.email,
            password1:  this.password1,
            password2:  this.password2,
            role:       this.role
          })
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