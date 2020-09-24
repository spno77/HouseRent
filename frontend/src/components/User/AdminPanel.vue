<template>
    <div>
      <div>
         <h1 class="ti"> Admin Panel </h1>
         
         <b-container>
         <button @click="getUsers()" class="btn btn-success">Show Users</button>
         
         <button @click="export2txt()" class="btn btn-primary">Export data to local txt file</button>
  
          <div v-if="this.show===true">
            <b-table striped hover :items="users" :fields="fields">
               <template v-slot:cell(is_approved)="row">
                 <b-form-group>
                   <input type="checkbox" v-model="row.item.is_approved" />
                 </b-form-group>
               </template>
              <template v-slot:cell(approve)="row">
                <button size="sm" @click="editUser(row.item.id)" class="btn btn-primary">
                  Approve
                </button>
              </template>

            </b-table>          
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
        show: false,
        fields: ['id','username','email','firstname','lastname',
    'is_staff','phone','role','is_approved','approve']
      }
    },
    computed:{
      ...mapGetters([
        'tuser',
      ])
     },

     mounted() {
       axios
         .get('https://127.0.0.1:8000/api/v1/houses/')
         .then(response=>(this.houses = response.data))       
    },

     methods:{

      getUsers(){
         axios
           .get('https://127.0.0.1:8000/api/v1/users/',
            {headers: {'Authorization': 'JWT ' + this.tuser.token}}
            )
           .then(response=>(this.users = response.data))
           this.show = true  
       },

       editUser(id) {
        id -= 1
        alert("user "+ this.users[id].username +" is approved")
        axios
          .put('https://127.0.0.1:8000/api/v1/users/'+ this.users[id].id + '/',{
            is_approved :  this.users[id].is_approved,
            username :    this.users[id].username,
            email:       this.users[id].email,
            firstname:   this.users[id].firstname,
            lastname:    this.users[id].lastname,
            phone:       this.users[id].phone,
          },
            {headers: {'Authorization': 'JWT ' + this.tuser.token}} 
          )
          .catch((err) => {
           console.log(err.response.data);
           });

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