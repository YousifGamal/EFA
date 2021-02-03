<template>
  <div class="user-item">
    <div>
    <!--<input type="checkbox" v-on:click="markUser" />-->
      <b-badge>{{user[1]}}</b-badge>
      <button @click="$emit('del-user', user[0])" style="float:right;" title="delete user">&#10062;</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "UserItem",
  props: ['user'],
  methods: {
      markUser(){
          console.log(this.user[0]);
      }
  }
}
</script>

<style scoped>
  .user-item {
    background: #f4f4f4;
    border-bottom: 1px #ccc dotted;
  }

  .is-complete {
    text-decoration: line-through;
  }

  .del {
    background: #5f5f5f;
    color: #fff;
    border: none;
    padding: 5px 9px;
    border-radius: 50%;
    cursor: pointer;
    float: right;
  }
</style>
