<template>
 
 <div>
 <app />	
  <b-jumbotron header="Profile:" header-level="4">
    
   <div>
    <p> <b>Username:</b>    {{ user.username }} </p>
   
    <p> <b>Email:</b>        {{ user.email }}     </p>
    <p> <b>Firstname:</b>    {{ user.firstname }} </p>
    <p> <b>Lastname:</b>     {{ user.lastname }}  </p>
    <p> <b>Phone:</b>        {{ user.phone }}     </p>
    <p> <b>Role:</b>         {{ user.role }}     </p>
    
     <span>
			<img :src="user.image">
	</span>
   </div>

   <router-link :to="{name: 'editprofile', params: { id: this.id }}" class="btn btn-secondary">Edit</router-link>
    

  </b-jumbotron>
</div>

</template>


<script>
 import axios from 'axios';

 export default{
    data(){
      
      return {
        id:  this.$route.params.id,
        user: {} 
      }        
    },
    mounted(){
      axios
        .get(`http://127.0.0.1:8000/api/v1/users/${ this.id }`)
        .then(response => (this.user = response.data))
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

