<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <b-navbar-brand href="#">Console Page</b-navbar-brand>
      <b-navbar-brand href="/login" @click="Logout" class="ml-auto">Logout</b-navbar-brand>
    </b-navbar>
    
  </div>
</template>

<script>
export default {
  name: 'Header',
  props: {
    msg: String
  },
    methods:{
        Logout(){
        console.log("Here");
        window.localStorage.clear();
        this.$router.push({ name: "Login" });
      },
  }
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
