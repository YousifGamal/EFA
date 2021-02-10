<template>
  <div>
    <Header />
    <div class="container">
      <b-nav tabs fill>
        <b-nav-item><router-link style="text-decoration:none;" to="/console/Users">Users</router-link></b-nav-item>
        <b-nav-item><router-link style="text-decoration:none;" to="/console/Pending">Pending</router-link></b-nav-item>
      </b-nav>
      <router-view />
    </div>
  </div>
</template>

<script>

import Header from '../components/layout/Header'

export default {
  name: 'ConsoleView',
  components: {
    Header
    },
  beforeMount(){
    const role = window.localStorage.getItem('role');
    if(role === 'Admin')
    {
      this.getMatches()
    }
    else{
      this.$router.push({ name: "Home" });
    }
  }
  }
</script>

<style>
.views{
  margin-bottom: 10px;
}
@import'~bootstrap/dist/css/bootstrap.css'
</style>