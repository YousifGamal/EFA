<template>
  <div>
    <Header />
    <div class="container">
      <b-nav tabs fill>
        <b-nav-item><router-link style="text-decoration:none;" to="/console/Users">Users</router-link></b-nav-item>
        <b-nav-item><router-link style="text-decoration:none;" to="/console/Pending">Pending</router-link></b-nav-item>
        <b-nav-item><router-link style="text-decoration:none;" to="/Tickets">Tickets</router-link></b-nav-item>
      </b-nav>
      <div class="text-center views">
        <b-button pill variant="outline-secondary"></b-button> | 
        <b-button pill variant="outline-secondary"></b-button>
      </div>
      <router-view />
    </div>
  </div>
</template>

<script>

import Header from './components/layout/Header.vue'

export default {
  name: 'App',
  components: {
    Header
    }
  }
</script>

<style>
.views{
  margin-bottom: 10px;
}
@import'~bootstrap/dist/css/bootstrap.css'
</style>