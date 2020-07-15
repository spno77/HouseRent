<template>
 <div>
  <app />
  <b-navbar class="fixed-top" toggleable="lg" type="dark" variant="info">
    <b-navbar-brand :to="{name: 'list'}">HouseRent</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item  :to="{name: 'register'}"> Register </b-nav-item>
        <b-nav-item  :to="{name: 'create'}">   Create </b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <b-form-input size="sm" v-model="search_term" v-on:keyup.enter="searchHouse" class="mr-sm-2" placeholder="Search"></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
        </b-nav-form>


        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <template v-slot:button-content>
            <em>{{ tuser.user.username}}</em>
          </template>
          <b-dropdown-item :to="{name: 'login'}"> Login </b-dropdown-item>

          <div v-if="tuser.user.id !==''">
            <b-dropdown-item  
            :to="{name: 'profile', params: { id: tuser.user.id }}"> Profile
            </b-dropdown-item>
          </div>

          <b-dropdown-item @click="logout"> Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>
</template>

<script>
  import axios from 'axios';
  import { mapGetters } from 'vuex';

  export default {
  name: 'Header',

   data(){
    return {
      //houses : [],
      search_term: '',
      //id: this.tuser.user.id
    }
   },
   
   computed:{
      ...mapGetters([
        'tuser',
      ]),
     },
  
 
   methods:{
    searchHouse: function(){
      this.$store.dispatch('searchHouses'); 
    },

    logout: function(){
      axios
        .post('http://127.0.0.1:8000/api/v1/rest-auth/logout/')
    },

    get_id(){
        this.id = this.tuser.user.id
        return this.id
      }
    
   }
  
}

</script>>