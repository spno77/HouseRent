<template>
   <div>
<h1 class="ti"> My messages </h1>
<div class="overflow-auto">
 <b-pagination v-model="currentPage" :total-rows="rows" :per-page="perPage"> 
  </b-pagination>

  <b-list-group v-for="(mess, index) in messages.slice(this.perPage*(currentPage-1),this.perPage*(currentPage))" :key="index">

   <b-list-group-item variant="info"> 
          <div class = "row">
             <div class="col-md-6">
                <b>Message:   </b> {{ mess.message }} <br>
                <b>Send Date: </b> {{ mess.send_date }}
              </div>
              <div class="col-md-6 pt-3">
                  <router-link :to="{name: 'reply_message',params: { house_id: mess.house,
                    sender_id: mess.sender }}" class="btn btn-success">Reply</router-link>
            </div>
          </div>    
   </b-list-group-item>
 </b-list-group>
</div>
</div>
</template>

<script>
import { mapGetters } from 'vuex';
import axios from 'axios';

export default { 
  name: 'MessageList',
    
  data(){
    return {
      messages: [],
      idd: this.$route.params.id,
      perPage: 6,
      currentPage: 1,
     }
   },

   computed:{
    ...mapGetters([
        'tuser',
      ]),
    rows() {
        return this.messages.length
      }
   },

   mounted(){
    axios
      .get('https://127.0.0.1:8000/api/v1/messages/',
       {headers: {'Authorization': 'JWT ' + this.tuser.token}}  
      )
      .then(response => (this.messages = response.data))
    
    },
  

}


</script>







<style scoped>
  
.ti{

  color: lightblue;
  text-align: center;
}

.test{
  margin-left: 10px;
}

.le{
  margin-left: 10px;
}

</style>