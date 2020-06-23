
<template>
	<div>
		<app/>
		<h1>
			Confirm delete:
			<button type="button" v-on:click="deleteHouse" class="btn btn-danger">Delete</button>
         

		</h1>

	</div>
</template>

<script>
 import axios from 'axios';

 export default {
  name: 'HouseDelete',
  
  data(){
    return {
      houses : [],
      idd : this.$route.params.id,
    }
  },
  mounted(){
    axios
      .get('http://127.0.0.1:8000/api/v1/houses/?ordering=cost')
      .then(response => (this.houses = response.data))
  },

   methods:{

    deleteHouse: function(){
      axios
       .delete('http://127.0.0.1:8000/api/v1/houses/'+ this.houses[this.idd].id) 
      },

    goIndex: function(){
       this.$router.push('/')
    }
  }
}

</script>

