<template>
    <div>
      <div>
        <h1 class="ti">  Send Message  </h1>
        <b-container>   
        <b-form  v-if="show">
          
          <b-form-textarea id="textarea" v-model="message.body" 
            placeholder="Write your message "
            rows="3"
            max-rows="6"
          ></b-form-textarea>
       
          <b-button  v-on:click="onSubmit" variant="success">Submit</b-button>
        
        </b-form>
        </b-container>
        </div>
    </div>
</template>


<script>
 import axios from 'axios';
  import { mapGetters } from 'vuex';
  import { mapActions } from 'vuex';


  export default {
    name: 'ReplyMessage',
   
    
    data() {
      return {
        idd: this.$route.params.house_id,
        receiver: this.$route.params.sender_id,
        house: {},
        show: true,
        message: {},
      }
    },
    computed:{
      ...mapGetters([
        'tuser'
      ])
     },

    mounted() {
        axios
          .get('https://127.0.0.1:8000/api/v1/houses/'+ this.idd,
          {headers: {'Authorization': 'JWT ' + this.tuser.token}}  
          )
          .then( response => {
            this.house = response.data
           })
          .catch((err) => {
             console.log(err.response.data);
           });
        
       
    },


    methods: {
      
      onSubmit(){
        axios
          .post('https://127.0.0.1:8000/api/v1/messages/',{
            house:        this.house.id,
            sender:       this.tuser.user.id,
            receiver:     this.receiver,
            message:      this.message.body,  
          },
           {headers: {'Authorization': 'JWT ' + this.tuser.token}}  
          )
          .catch((err) => {
             console.log(err.response.data);
           });
      },
      
    },
  
}

</script>


<style scoped>
  
.ti{

  color: lightblue;
  text-align: center;

}

</style>
