<template>
    <div>
      <app />
        <div>
          <h1 class="ti">   Reserve House  </h1>
          <b-container>   
          <b-form  v-if="show">
          
           <b-form-group
        id="input-group-1"
        label="House Title:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="house.title"
          required
          placeholder="Enter title"
        ></b-form-input>
      </b-form-group>

          <b-form-group
            id="input-group-1"
            label="Cost:"
            label-for="input-1"
          >
            <b-form-input
              id="input-1"
              type="number"
              v-model="house.cost"
              required
              placeholder="Enter cost"
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-2" label="Days:" label-for="input-2">
            <b-form-input
              id="input-2"
              type="number"
              v-model="reservation.days"
              required
              placeholder="Enter days"
            ></b-form-input>
          </b-form-group>

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
    
    data() {
      return {
        idd : this.$route.params.id,
        reservation:{
          days: '',
        },
        house:{
          title: '',
          cost: '',
        },
        show: true
      }
    },
    computed:{
      ...mapGetters([
        'tuser'
      ])
     },

    mounted(){
      axios
        .get('http://127.0.0.1:8000/api/v1/houses/'+ this.idd)
        .then( response => {
           this.house = response.data
        })
         .catch((err) => {
           console.log(err.response.data);
           });
     }, 

    methods: {
      ...mapActions(['loginUser']),
      
      onSubmit() {
        axios
          .post('http://127.0.0.1:8000/api/v1/reservations/',{
            house:        this.house.id,
            cost:         this.house.cost,
            days:         this.reservation.days,
            tenant:       this.tuser.user.id
          },
           {headers: {'Authorization': 'JWT ' + this.tuser.token}}  
          )
          .catch((err) => {
             console.log(err.response.data);
           });
        
        this.$router.push('/')

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
