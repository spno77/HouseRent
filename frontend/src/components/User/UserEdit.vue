<template>
    <div>
        <div>
             <h1 class="ti">   Edit Profile </h1>
         <b-container>   
          <b-form  v-if="show">
      <b-form-group
        id="input-group-1"
        label="Username:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="user.username"
          required
         
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Email:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="user.email"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Firstname:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="user.firstname"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Lastname:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="user.lastname"
          required
        ></b-form-input>
      </b-form-group>

     
      <b-form-group id="input-group-2" label="Phone:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="user.phone"
          required
        ></b-form-input>
      </b-form-group>
      

      <b-button  v-on:click="editUser" variant="primary"> Edit </b-button>
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
        id : this.$route.params.id,
        
        user: {
          username: '',
          email: '',
          firstname: '',
          lastname: '',
          phone: '',
        },

        show: true
     }
    },

    mounted(){
      axios
        .get('http://127.0.0.1:8000/api/v1/users/'+ this.id)
        .then( response => {
           this.user = response.data
        })
     }, 

    methods:{
        
      editUser() {
        axios
          .put('http://127.0.0.1:8000/api/v1/users/'+ this.id + '/',{
            username :  this.user.username,
            email:      this.user.email,
            firstname:  this.user.firstname,
            lastname:   this.user.lastname,
            phone:      this.user.phone,

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

 