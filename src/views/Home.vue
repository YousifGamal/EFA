<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <b-navbar-brand href="/">Home</b-navbar-brand>
      <b-navbar-brand href="/manager">Manager</b-navbar-brand>
      <b-navbar-brand href="/user">User</b-navbar-brand>


      <b-collapse id="nav-collapse" is-nav>

        <b-navbar-nav class="ml-auto" >

          <b-navbar-brand href="/update">Profile</b-navbar-brand>
          <b-navbar-brand href="/login" @click="Logout()">Logout</b-navbar-brand>
        </b-navbar-nav>
      </b-collapse>
  </b-navbar>
    <img src="../assets/Stadium.jpg" class="std">
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  methods:{
        Logout(){
        console.log("Here");
        window.localStorage.clear();
        // this.$router.push({ name: "Login" });
      },
  }
}
</script>
<style scoped>
.std{
    max-width: 100%;
}
.element{
    color:green;
}
</style>>
