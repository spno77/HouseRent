<template>
    <div>
        <div>
          <h1 class="ti">   Add a review  </h1>
          <b-container>   
          <b-form  v-if="show">
          
           <b-form-group
        id="input-group-1"
        label="house name:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="reservation.house"
          required
          placeholder="review title"
        ></b-form-input>
      </b-form-group>

      <b-form-textarea
      id="textarea"
      v-model="review.content"
      placeholder="Write your review "
      rows="3"
      max-rows="6"
    ></b-form-textarea>
       
         Rating :
      <b-form-rating v-model="review.rating"></b-form-rating> 
        

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
    name: 'ReviewAdd',
    
    data() {
      return {
        idd: this.$route.params.id,
        reservation: {},
        show: true,
        review: {
          content: '',
          rating :  null,
        }
      }
    },
    computed:{
      ...mapGetters([
        'tuser'
      ])
     },

    mounted() {
        axios
          .get('http://127.0.0.1:8000/api/v1/reservations/'+ this.idd,
          {headers: {'Authorization': 'JWT ' + this.tuser.token}}  
          )
          .then( response => {
            this.reservation = response.data
           })
          .catch((err) => {
             console.log(err.response.data);
           });
    }, 

    methods: {
      
      onSubmit(){
        axios
          .post('http://127.0.0.1:8000/api/v1/reviews/',{
            content:      this.review.content,
            rating:       this.review.rating,
            reviewer:     this.tuser.user.id,
            reservation:  this.reservation.id,
            house:        this.reservation.house,  
          },
           {headers: {'Authorization': 'JWT ' + this.tuser.token}}  
          )
          .then( response => {
             alert("Your Review has been added successfully !")
             this.$router.push('/')
          })
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
