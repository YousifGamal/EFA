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
      users:[],
      token:window.localStorage.getItem("token")
    }
  },
  methods:{
    deleteUser(id){
      axios.get("http://localhost:5000/deleteuser/"+id,{
        headers: { "x-access-token": `${this.token}` },
      })
    .then()
    .catch(err => console.log(err))
    this.users = this.users.filter(user => user[0] !== id);
    this.$notify({
      group: "login",
      type: "success",
      title: "Pending user deleted",
      // text: "Try again..",
      duration: 3000,
      });
    },
    searchPending(){
      if(this.searchInput !== "")
      {
        axios.get("http://localhost:5000/searchforpending/"+this.searchInput,{
        headers: { "x-access-token": `${this.token}` },
      })
        .then(res => this.users = res.data)
        .catch(err => console.log(err));
      }else{
        axios.get("http://localhost:5000/showpendingusers/",{
        headers: { "x-access-token": `${this.token}` },
      })
        .then(res => this.users = res.data)
        .catch(err => console.log(err))
      }
    },
    approveUser(id){
      axios.get("http://localhost:5000/approvepending/"+id,{
        headers: { "x-access-token": `${this.token}` },
      })
      .then()
      .catch(err => console.log(err))
      this.users = this.users.filter(user => user[0] !== id);
      this.$notify({
        group: "login",
        type: "success",
        title: "User has been approved",
        // text: "Try again..",
        duration: 3000,
      });
    }
  },
  created(){
    axios.get("http://localhost:5000/showpendingusers/",{
        headers: { "x-access-token": `${this.token}` },
      })
    .then(res => this.users = res.data)
    .catch(err => console.log(err))
  }
}
</script>

<style>
</style>
