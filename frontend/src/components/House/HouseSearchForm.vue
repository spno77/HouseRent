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

     <b-form-group id="input-group-2" label="Cost per day:" label-for="input-2">
        <b-form-input
          id="input-2"
          type="number"
          v-model="search.cost"
          required
          placeholder="Enter cost per day"
        ></b-form-input>
      </b-form-group>

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
          cost: null,
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
      this.$store.dispatch('updateSearchTerm',this.search)
      this.$router.push('/houses_search')
    },

    onFileChanged(event){
      this.file = event.target.files[0]
    },

      
    }
  }
</script>


<style scoped>
  
.ti{

  color: lightblue;
  text-align: center;

}

</style>