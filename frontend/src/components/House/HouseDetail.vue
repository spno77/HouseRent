<template>
<div>
	<app />
		<h1> <b>{{ house.title }} </b></h1>
		<p>{{ house.description }} </p>
		<p> cost : {{ house.cost }} $ </p>
		<p> Garage:{{ house.garage }} </p>
		<p> wifi:{{ house.wifi }} </p>
		<p> Aircondition:{{ house.aircondition }} </p>

	<div class="imgContainer">
		<div>
			<img :src="house.image">
		</div>
		
		<div class="imgButton">
			<router-link :to="{name: 'edit', params: { id: this.idd }}" class="btn btn-secondary">Edit</router-link>
			<router-link :to="{name: 'delete', params: { id: this.idd }}" class="btn btn-danger">Delete</router-link>
			<router-link :to="{name: 'reservation', params: { id: this.idd }}" class="btn btn-success">Reserve</router-link>
		</div>

	</div>	
</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HouseDetail',
  
  data(){
    return {
      house : {},
      idd : this.$route.params.id
    }
  },

 
  mounted(){
    axios
      .get(`http://127.0.0.1:8000/api/v1/houses/${ this.idd }`)
      .then(response => (this.house = response.data))
  }


}
</script>

<style>
  .imgButton{
    text-align:center;
    margin-top:5px;
}
</style>
