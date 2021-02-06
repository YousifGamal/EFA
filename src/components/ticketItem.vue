<template>
  <div>
    <div class="user-item">
    <!--<input type="checkbox" v-on:click="markUser" />-->
    <b-card  border-variant="success" header="Ticket" text-variant="black">
      <b-card-title>
        <img src="ticketIcon.png"/> <b-badge>{{ticket[1]}}</b-badge>  vs  <b-badge>{{ticket[2]}}  </b-badge>
        <button @click="$emit('del-ticket', ticket[0],ticket[3])" class="del" style="float:right;" title="delete ticket">&#10062;</button>
      </b-card-title>
      <b-card-sub-title sub-title-text-variant = "black" sub-title-tag="h5">
        {{ticket[3]}}, {{ticket[4]}}, {{ticket[5]}}
      </b-card-sub-title>
      <b-card-text>
        Seat Number {{ticket[6]}}
      </b-card-text>
    </b-card>
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
    padding: 10px;
  }

  .is-complete {
    text-decoration: line-through;
  }

  .del {
    background-color: #ffffff;
    color: #ffffff;
    border: none;
    padding: 5px 9px;
    border-radius: 50%;
    cursor: pointer;
    float: right;
  }
</style>
