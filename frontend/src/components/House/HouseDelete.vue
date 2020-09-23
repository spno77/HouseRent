
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
 import { mapGetters } from 'vuex';

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
      .get('https://127.0.0.1:8000/api/v1/houses/?ordering=cost')
      .then(response => (this.houses = response.data))
  },
  
  computed:{
      ...mapGetters([
        'tuser'
      ])
  },

   methods:{

    deleteHouse: function(){
      axios
       .delete('https://127.0.0.1:8000/api/v1/houses/'+ this.idd,
       {headers: {'Authorization': 'JWT ' + this.tuser.token}}
       )
      },

    goIndex: function(){
       this.$router.push('/')
    }
  }
}

</script>

