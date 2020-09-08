<template>
    <div>
      <div>
         <h1 class="ti"> Admin Panel </h1>
         
         <b-container>
         <button @click="getUsers()" class="btn btn-success">Show Users</button>
         <button @click="export2txt()" class="btn btn-primary">Export data to local txt file</button>
	
          <div>
           <b-table striped hover :items="users"></b-table>
          
          </div>
         </b-container>
  
       
      </div>
    </div>
</template>


<script>
  import axios from 'axios';
  import { mapGetters } from 'vuex';
  import { mapActions } from 'vuex';


  export default {
    
    data() {
      return {
        users:  [],
        houses: [],
        show: true,
      }
    },
    computed:{
      ...mapGetters([
        'tuser',
      ])
     },

     mounted() {
       axios
         .get('http://127.0.0.1:8000/api/v1/houses/')
         .then(response=>(this.houses = response.data))       
    },

     methods:{

      getUsers(){
         axios
           .get('http://127.0.0.1:8000/api/v1/users/')
           .then(response=>(this.users = response.data))  
       },


       export2txt() {
         const a = document.createElement("a");
         a.href = URL.createObjectURL(new Blob([JSON.stringify(this.houses, null, 2)], {
         type: "text/plain"
         }));
         a.setAttribute("download", "data.txt");
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a); 
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