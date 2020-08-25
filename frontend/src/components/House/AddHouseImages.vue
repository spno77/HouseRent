<template>
    <div>
        <app />
        <div>
             <h1 class="ti">   Add Images  </h1>
         <b-container>	
          <b-form  v-if="show">
      

     <b-form-file
     @change="onFileSelected"
      v-model="house.file"
      placeholder="Choose a file or drop it here..."
      drop-placeholder="Drop file here..."
    ></b-form-file>
    


      <b-button  v-on:click="onUpload" variant="primary">Submit</b-button>
    </b-form>
         
     </b-container>
      </div>
    </div>
</template>


<script>
 import axios from 'axios';
 import { mapGetters } from 'vuex';
  
  export default {
    data() {
      return {
        house_id : this.$route.params.id,
        house:{  
         
          file: null,
        },

        show: true
      }
    },

    computed:{
      ...mapGetters([
        'tuser'
      ])
    },

    methods: {
      onFileSelected(event){
        this.file = event.target.files[0]
      },
     
      onUpload(){
        const fd = new FormData();
        fd.append('image',this.house.file,this.house.file.name)
        fd.append('house',this.house_id)
        axios
          .post('http://127.0.0.1:8000/api/v1/houses/images',
            fd
            )
          .catch((err) => {
             console.log(err.response.data);
           });
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