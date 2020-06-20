<template>
  <div id="app">
    <p> HI my friend </p>
    <HouseList />
    <HouseDetail>
    </HouseDetail>
  </div>
</template>

<script>
import HouseList from './components/HouseList.vue'
import HouseDetail from './components/HouseDetail.vue'


export default {
  name: 'App',
  components: {
    HouseList,
    HouseDetail
  },


}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
