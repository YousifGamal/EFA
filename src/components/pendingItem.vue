<template>
  <div class="user-item">
    <div style="text-align:left;">
      <b-badge>{{pendingUser[1]}}</b-badge>
      <button @click="$emit('del-user', pendingUser[0])" class="del" title="delete user">&#10062;</button>
      <button @click="$emit('approve-user', pendingUser[0])" class="del" title="approve user">&#9989;</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "PendingItem",
  props: ['pendingUser'],
  methods: {
      
  }
}
</script>

<style scoped>
  .user-item {
    background: #f4f4f4;
    padding: 10px;
    border-bottom: 1px #ccc dotted;
  }

  .is-complete {
    text-decoration: line-through;
  }

  .del {
    color: #fff;
    border: none;
    padding: 5px 9px;
    border-radius: 50%;
    cursor: pointer;
    float: right;
  }
</style>
