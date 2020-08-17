<template>
    <div>
      <app />
        <div>
          <h1 class="ti">   Reserve House  </h1>
          <b-container>   
          <b-form  v-if="show">
          
           <b-form-group
        id="input-group-1"
        label="House Title:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="house.title"
          required
          placeholder="Enter title"
        ></b-form-input>
      </b-form-group>

          <b-form-group
            id="input-group-1"
            label="Cost:"
            label-for="input-1"
          >
            <b-form-input
              id="input-1"
              type="number"
              v-model="house.cost"
              required
              placeholder="Enter cost"
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-2" label="Days:" label-for="input-2">
            <b-form-input
              id="input-2"
              type="number"
              v-model="reservation.days"
              required
              placeholder="Enter days"
            ></b-form-input>
          </b-form-group>

          <b-button  v-on:click="onSubmit" variant="success">Submit</b-button>
        
          </b-form>
            <h1> Cost is : {{this.house.cost * this.reservation.days}} $ </h1>
          </b-container>
        </div>
    </div>


</template>


<script>


</script>


<style scoped>
  
.ti{

  color: lightblue;
  text-align: center;

}

</style>
