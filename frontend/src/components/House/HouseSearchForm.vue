<template>  
  <div>
  <b-container>	
  <b-form  v-if="show">
   <b-form-group id="input-group-2" label="Country name:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="search.country"
          required
          placeholder="Enter country name"
        ></b-form-input>
      </b-form-group>

     <b-form-group id="input-group-2" label="City name:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="search.city"
          required
          placeholder="Enter city name"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Number of people:" label-for="input-2">
          <b-form-input
            id="input-2"
            type="number"
            v-model="search.people_num"
            required
            placeholder="Enter number of people"
            ></b-form-input>
          </b-form-group>


  <div class="row">
      <div class="col-md-6">
        <label for="example-datepicker">Available From:</label>
        <b-form-datepicker id="example-datepicker" v-model="search.book_from" class="mb-2"></b-form-datepicker>
      </div>

      <div class="col-md-6">
        <label for="example-datepicker2">Available To:</label>
        <b-form-datepicker id="example-datepicker2" v-model="search.book_to" class="mb-2"></b-form-datepicker>
      </div>
  </div>

    </b-form>

 <b-button v-if="show2===false" v-on:click="onSubmit()" variant="success">Search</b-button>
  <b-button v-if="show2===false" v-on:click="changeShow()" variant="dark">More Filters</b-button>
   
 <b-form v-if="show2">
   
    <b-form-group id="input-group-2" label="House Type:" label-for="input-2">
      <b-form-select v-model="search.type" :options="search.options"> </b-form-select> 
    </b-form-group>
  
   <div class="row">

    <div class="col-md-6">

    <b-form-group label="Garage:">
      <b-form-radio-group class="pt-2">
        <b-form-radio v-model="search.garage" value = "true">True</b-form-radio>
        <b-form-radio v-model="search.garage" value = "false">False</b-form-radio>
      </b-form-radio-group>
    </b-form-group>
    
    <b-form-group label="Heat:">
      <b-form-radio-group class="pt-2">
          <b-form-radio v-model="search.heat" value = "true">True</b-form-radio>
          <b-form-radio v-model="search.heat" value = "false">False</b-form-radio>
      </b-form-radio-group>
    </b-form-group>

  </div>

   <div class="col-md-6">
    <b-form-group label="Wifi:">
      <b-form-radio-group class="pt-2">
        <b-form-radio v-model="search.wifi" value = "true">True</b-form-radio>
        <b-form-radio v-model="search.wifi" value = "false">False</b-form-radio>
      </b-form-radio-group>
    </b-form-group>

    <b-form-group label="Aircondition:">
      <b-form-radio-group class="pt-2">
        <b-form-radio v-model="search.aircondition" value = "true">True</b-form-radio>
        <b-form-radio v-model="search.aircondition" value = "false">False</b-form-radio>
      </b-form-radio-group>
     </b-form-group>
    </div> 

    </div>

     <b-button  v-on:click="onSubmit()" variant="success">Search</b-button>

    </b-form>



    </b-container>
    </div>  
</template>


<script>
  import axios from 'axios';
  import { mapGetters } from 'vuex';
  import { mapActions } from 'vuex';
  
  export default {
   
    data() {
      return {
        
        search :{  
          country: '',
          city: '',
          book_from: '',
          book_to: '',
          people_num: '',
          type: '',
          heat: '',
          garage: '',
          wifi: '',
          aircondition: '',
          options: [
          { value: null, text: 'Please select a house type' },
          { value: 'entire_place', text: 'Entire  Place' },
          { value: 'private_room', text: 'Private Room' },
          { value: 'shared_room',  text: 'Shared  Room' },
          ],
          clicked: false,
        },

        show: true,
        show2: false,
        
      }
    },

    computed:{
      ...mapGetters(['tuser']),
    },

    methods: {
      
      ...mapActions(['updateSearchTerm']),

    onSubmit() {
      if(this.compareDates() === true) {
        this.$store.dispatch('updateSearchTerm',this.search)
        this.$router.push('/houses_search')
      }
      else{
        alert("Wrong Dates")
      }
    },

    changeShow(){
      this.show2 = true
      this.search.clicked = true
    },

    onFileChanged(event){
      this.file = event.target.files[0]
    },
  
    compareDates(){
       var book_from = new Date(this.search.book_from)
       var book_to   = new Date(this.search.book_to)
       if (book_from < book_to){
        return true
       }
       else{
        return false
       }
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


