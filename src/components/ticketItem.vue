<template>
  <div class="user-item">
    <div>
    <!--<input type="checkbox" v-on:click="markUser" />-->
      <b-badge>{{ticket[1]}}</b-badge>vs<b-badge>{{ticket[2]}}</b-badge>
      <button @click="$emit('del-ticket', ticket[0],ticket[3])" style="float:right;" title="delete ticket">&#10062;</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "TicketItem",
  props: ['ticket']
}
</script>

<style scoped>
  .user-item {
    background: #f4f4f4;
    border-bottom: 1px #ccc dotted;
  }
</style>
