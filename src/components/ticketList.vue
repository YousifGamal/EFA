<template>
    <div>
        <div v-bind:key="ticket[0]" v-for="ticket in ticketsList">
            <ticketItemList v-bind:ticket="ticket" v-on:del-ticket="$emit('del-ticket',ticket[0],ticket[3])"/>
        </div>
    </div>
</template>

<script>
import ticketItemList from '../components/ticketItem';
export default {
  name: "TicketsList",
  components:{
      ticketItemList
  },
  props: ['ticketsList']
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
    background: #5f5f5f;
    color: #fff;
    border: none;
    padding: 5px 9px;
    border-radius: 50%;
    cursor: pointer;
    float: right;
  }
</style>
