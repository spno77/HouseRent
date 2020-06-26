<template>
<div>
	<app />
		<h1> <b>{{ houses[idd].title }} </b></h1>
		<p>{{ houses[idd].description }} </p>
		<p> cost : {{ houses[idd].cost }} $ </p>
		<p> Garage:{{ houses[idd].garage }} </p>
	<div class="imgContainer">
		<div>
			<img :src="houses[idd].image">
		</div>
		<div class="imgButton">
			<button type="button" class="btn btn-secondary mr-1">Edit</button>
			<router-link :to="{name: 'delete', params: { id: this.idd }}" class="btn btn-danger">Delete</router-link>

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
      houses : [],
      idd : this.$route.params.id
    }
  },

 
  mounted(){
    axios
      .get('http://127.0.0.1:8000/api/v1/houses/?ordering=cost')
      .then(response => (this.houses = response.data))
  }


}
</script>

<style>
  .imgButton{
    text-align:center;
    margin-top:5px;
}
</style>
