<template>
<div>
	<app />
		<h1> <b>{{ house.title }} </b></h1>
		<p> {{ house.description }} </p>
    <p> Country: {{ house.country }} </p>
    <p> City:    {{ house.city }} </p>
		<p> cost : {{ house.cost }} $ </p>
		<p> Garage:{{ house.garage }} </p>
		<p> wifi:{{ house.wifi }} </p>
		<p> Aircondition:{{ house.aircondition }} </p>

    <div class="row">
      <div  class="column" v-for="house in house.house_img" :key="house.id">
      <div class="imgContainer">
       <div>
        <img class ="img" :src="house.image" style="width:95%">
      </div>
    </div>
     </div>
 </div>

		<div class="imgButton">
      <router-link :to="{name: 'reviewlist', params: { id: this.idd }}" class="btn btn-warning">Show Reviews</router-link>
      <div v-if="isLoggedIn===true && house.host === tuser.user.username">
        <router-link :to="{name: 'edit', params: { id: this.idd }}" class="btn btn-secondary">Edit</router-link>
        <router-link :to="{name: 'delete', params: { id: this.idd }}" class="btn btn-danger">Delete</router-link>
       </div>
			<router-link v-if="isLoggedIn===true && house.host !== tuser.user.username" :to="{name: 'reservation', params: { id: this.idd }}" class="btn btn-success">Reserve</router-link>
		</div>
 
	</div>	

</template>

<script>
import axios from 'axios';
import { mapGetters } from 'vuex';

export default {
  name: 'HouseDetail',
  
  data(){
    return {
      house : {},
      idd : this.$route.params.id
    }
  },

   computed:{
      ...mapGetters([
        'tuser',
        'isLoggedIn'
      ]),
    },
  
  mounted(){
    axios
      .get(`http://127.0.0.1:8000/api/v1/houses/${ this.idd }`)
      .then(response => (this.house = response.data))
  },


}
</script>

<style scoped>
  .imgButton{
    text-align:center;
    margin-top:5px;
}

.row {
  display: flex;
}

.column {
  flex: 20.33%;
}

.img {
    float: left;
    width:  200px;
    height: 200px;
    object-fit: cover;
}

</style>
