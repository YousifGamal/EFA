<template>
  <div>
    <nav class="navbar navbar-light bg-light p-3 mb-2 bg-dark text-white">
      <h3>Site admin</h3><b-button size="sm" @click="Logout()">Log out</b-button>
    </nav>
    
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
