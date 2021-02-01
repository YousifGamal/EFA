<template>
  <div class="hello">
    <h1>Site Manager</h1>
    <button>Log out</button><br />
    <input type="text" name="search" placeholder="search for user..." />
    <input type="submit" name="searchBtn" value="search" />
  </div>
</template>

<script>
export default {
  name: 'Header',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
