<template>
	<div>
		<app />
			<h1> <b>{{ houses[idd].title }} </b></h1>
			<p>{{ houses[idd].description }} </p>
			<p> cost : {{ houses[idd].cost }} $ </p>
			<img :src="houses[idd].image">
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