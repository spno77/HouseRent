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

           <div class="row">
      <div class="col-md-6">
        <label for="example-datepicker">Reserve From:</label>
        <b-form-datepicker id="example-datepicker" v-model="reservation.reserve_in" class="mb-2"></b-form-datepicker>
      </div>

      <div class="col-md-6">
        <label for="example-datepicker2">Reserve To:</label>
        <b-form-datepicker id="example-datepicker2" v-model="reservation.reserve_out" class="mb-2"></b-form-datepicker>
      </div>
  </div>

          <b-button  v-on:click="onSubmit" variant="success">Submit</b-button>
        
          </b-form>
            <h1 v-show="reservation.reserve_in !== '' && reservation.reserve_out !=='' && this.finalCost > 0"> The total cost is : {{ this.calculateFinalCost() }} $ </h1>
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
        idd: this.$route.params.id,
        showCost: false, 
        reservation:{
          reserve_in: '',
          reserve_out: '',
        },
        house:{
          title: '',
          cost: '',
        },
        show: true,
        finalCost: 0,
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
        if(this.compareDates() === true){
          if(this.finalCost > 0){
            axios
              .post('http://127.0.0.1:8000/api/v1/reservations/',{
                house:        this.house.id,
                cost:         this.finalCost,
                reserve_in:   this.reservation.reserve_in,
                reserve_out:  this.reservation.reserve_out,
                tenant:       this.tuser.user.id
              },
               {headers: {'Authorization': 'JWT ' + this.tuser.token}}  
              )
              .catch((err) => {
                 console.log(err.response.data);
              });
            this.$router.push('/')  
          }
        }
        else{
          console.log("Wrong dates")
        }
      
      },

      datediff(first, second) {
        var date1 = new Date(first)
        var date2 = new Date(second)

        return Math.round((date2-date1)/(1000*60*60*24));
      },

    
      changeCost(){
        this.showCost = true
      },

      calculateFinalCost(){
        
        var days = this.datediff(this.reservation.reserve_in, this.reservation.reserve_out) 
        
        this.finalCost = this.house.cost * days
        
        return this.finalCost
      },

      compareDates(){
        var house_from = new Date(this.house.av_from)
        var house_to   = new Date(this.house.av_to)
        var res_from   = new Date(this.reservation.reserve_in)
        var res_to     = new Date(this.reservation.reserve_out)
       if( (house_from <= res_from)  && house_to >= house_from){
        return true
       }
       else{
        alert("Wrong dates !")
        return false
       }
      }

    },
  
}
</script>

<style scoped>
  
.ti{

  color: lightblue;
  text-align: center;

}

</style>
