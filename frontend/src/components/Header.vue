<template>
 <div>
  
  <b-navbar class="fixed-top" toggleable="lg" type="dark" variant="dark">
    <b-navbar-brand :to="{name: 'list'}">HouseRent</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav v-if="isLoggedIn === true && tuser.user.role === 'host' ">
        
        <b-nav-item  :to="{name: 'create'}">   Create </b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
        <b-nav-form>
       
          <b-button size="sm" :to="{name: 'house_search_form'}" class="my-2 my-sm-0" type="submit">Search</b-button>
        </b-nav-form>
 

       <b-nav-item-dropdown right >
          <!-- Using 'button-content' slot -->
          <template v-slot:button-content>
            <em v-if="isLoggedIn===true">{{tuser.user.username}}</em>
            <em v-else>User</em>
          </template>
         
          <b-dropdown-item v-if="isLoggedIn===false"
          :to="{name: 'register'}"> Register </b-dropdown-item>

          <b-dropdown-item v-if="isLoggedIn===false" 
          :to="{name: 'login'}"> Login </b-dropdown-item>
          
            <b-dropdown-item  v-if="isLoggedIn===true"
            :to="{name: 'reservationlist'}"> My Reservations
            </b-dropdown-item>

            <b-dropdown-item  v-if="isLoggedIn===true"
            :to="{name: 'my_messages'}"> My Messages
            </b-dropdown-item>  

            <b-dropdown-item  v-if="isLoggedIn===true && tuser.user.role === 'host'"
            :to="{name: 'host_houses'}"> My Listings
            </b-dropdown-item>  

            <b-dropdown-item  v-if="isLoggedIn===true"
            :to="{name: 'profile', params: { id: tuser.user.id }}"> Profile
            </b-dropdown-item> 
         
            
             <b-dropdown-divider v-if="isLoggedIn===true"></b-dropdown-divider>

          <b-dropdown-item v-if="isLoggedIn===true" 
          @click="logoutUser"> Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
       
      </b-navbar-nav>


    </b-collapse>
  </b-navbar>
</div>
</template>


<script>
  import axios from 'axios';
  import { mapGetters } from 'vuex';
  import { mapActions } from 'vuex';
  export default {
  name: 'Header',
   
   data(){
    return {
      search_term: '',
    }
   },
   
   computed:{
      ...mapGetters([
        'tuser',
        'isLoggedIn',
      ]),
    },
  
 
   methods:{
   
    ...mapActions(['logoutUser','getReservations']),
    searchHouse: function(){
      this.$store.dispatch('searchHouses'); 
    },
    
  }
  
}
</script>