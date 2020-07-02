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
        
        username: '',
        email: '',
        password1: '',
        password2: '',
        
        
        show: true
      }
    },
    methods: {
      onSubmit() {
        axios
          .post('http://127.0.0.1:8000/api/v1/rest-auth/registration/',{
            username : this.username,
            email: this.email,
            password1: this.password1,
            password2: this.password2,
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