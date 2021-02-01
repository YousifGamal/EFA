<template>
  <div>
    <Header />
    <Users v-bind:usersList="users" v-on:del-user="deleteUser"/>
  </div>
</template>

<script>
import Header from './components/layout/Header.vue'
import Users from '../views/Users.vue'
import axios from 'axios'

export default {
  name: 'App',
  components: {
    Header, //export components to be used in the templates above
    Users
  },data(){
    return{
      users:[]
    }
  },
  methods:{
    deleteUser(id){
      axios.get("http://localhost:7777/deleteuser/"+id)
    .then()
    .catch(err => console.log(err))
    this.users = this.users.filter(user => user[0] !== id);
    }
  },
  created(){
    axios.get("http://localhost:7777/showallusers/")
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
