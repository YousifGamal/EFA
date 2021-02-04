<template>
  <div>
    Search for user name : 
    <input type="text" name="search" v-model="searchInput" placeholder="search for user..." @keyup="searchUser" />
    <usersList v-bind:usersList="users" v-on:del-user="deleteUser"/>
  </div>
</template>

<script>
import usersList from '../components/userList'
import axios from 'axios'

export default {
  name: 'UsersView',
  components: {
    usersList
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
    searchUser(){
      if(this.searchInput !== "")
      {
        axios.get("http://localhost:5000/searchforuser/"+this.searchInput)
        .then(res => this.users = res.data)
        .catch(err => console.log(err));
      }else{
        axios.get("http://localhost:5000/showallusers/")
        .then(res => this.users = res.data)
        .catch(err => console.log(err))
      }
    }
  },
  created(){
    axios.get("http://localhost:5000/showallusers/")
    .then(res => this.users = res.data)
    .catch(err => console.log(err))
  }
}
</script>

<style>
</style>
