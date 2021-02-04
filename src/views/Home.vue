<template>
  <div class="home">
      <div id="nav">
      <router-link to="/user">User</router-link> |
      <router-link to="/manager">Manager</router-link>|
      <router-link to="/login">Logout</router-link>|
      <router-link to="/update">UpdateProfile</router-link>
      
      </div>
    <img alt="Vue logo" src="../assets/logo.png">
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
}
</script>
