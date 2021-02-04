<template>
  <div>
    Search for Pending user name : 
    <input type="text" name="search" v-model="searchInput" placeholder="search for user..." @keyup="searchPending" />
    <pendingList v-bind:pendingList="users" v-on:del-user="deleteUser" v-on:approve-user="approveUser"/>
  </div>
</template>

<script>
import pendingList from '../components/pendingList'
import axios from 'axios'

export default {
  name: 'pendingView',
  components: {
    pendingList
  },data(){
    return{
      searchInput:[],
      users:[]
    }
  },
  methods:{
    deleteUser(id){
      axios.get("http://localhost:5000/deleteuser/"+id)
    .then()
    .catch(err => console.log(err))
    this.users = this.users.filter(user => user[0] !== id);
    },
    searchPending(){
      if(this.searchInput !== "")
      {
        axios.get("http://localhost:5000/searchforpending/"+this.searchInput)
        .then(res => this.users = res.data)
        .catch(err => console.log(err));
      }else{
        axios.get("http://localhost:5000/showpendingusers/")
        .then(res => this.users = res.data)
        .catch(err => console.log(err))
      }
    },
    approveUser(id){
      axios.get("http://localhost:5000/approvepending/"+id)
      .then()
      .catch(err => console.log(err))
      this.users = this.users.filter(user => user[0] !== id);
    }
  },
  created(){
    axios.get("http://localhost:5000/showpendingusers/")
    .then(res => this.users = res.data)
    .catch(err => console.log(err))
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #344d66;
  margin-top: 60px;
}
</style>
