<template>
    <div>
        <app />
        <div>
             <h1 class="ti">  Login </h1>
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

      <b-form-group id="input-group-2" label="Password:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="user.password"
          type="password"
          required
          placeholder="Enter password"
        ></b-form-input>
      </b-form-group>

      <b-button  @click="loginUser(user)" variant="primary"> Login </b-button>
       
    </b-form>
     
     </b-container>
  
       


      </div>
    </div>
</template>


<script>
 //import axios from 'axios';
  import { mapGetters } from 'vuex';
  import { mapActions } from 'vuex';

  export default {
    
    data() {
      return {
        user:{
          username: '',
          password: '',
        },
        id: '',
        show: true
      }
    },
    computed:{
      ...mapGetters([
        'tuser'
      ])
     },

    methods: {
      ...mapActions(['loginUser']),
      
      findId(){
        this.id = this.tuser.user.id
        return this.id 
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