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
        },

        show: true
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


