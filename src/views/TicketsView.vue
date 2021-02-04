<template>
  <div>
    <h3>dummy</h3>
    <!--
    Search for ticket : 
    <input type="text" name="search" v-model="searchInput" placeholder="search for user..." @keyup="searchUser" />-->
    <div class="container">
      <ticketList v-bind:ticketsList="tickets" v-on:del-ticket="deleteTicket"/>
    </div>
  </div>
</template>

<script>
import ticketList from '../components/ticketList'
import axios from 'axios'

export default {
  name: 'TicketsView',
  components: {
    ticketList
  },data(){
    return{
      tickets:[]
    }
  },
  methods:{
    deleteTicket(id,date){
        console.log(id);
        var mdate = new Date(date).getTime() / 1000;
        var currentDate = new Date().getTime() / 1000;
        var timeDiff = mdate - currentDate;
        if(timeDiff >= 3*24*60*60)
        {
            axios.get("http://localhost:5000/deleteticket/"+id)
            .then()
            .catch(err => console.log(err))
            this.tickets = this.tickets.filter(ticket => ticket[0] !== id);
        }
    }
  },
  created(){
    axios.get("http://localhost:5000/showusertickets/"+2) // lazem tt3dl
    .then(res => this.tickets = res.data)
    .catch(err => console.log(err))
  }
}
</script>

<style>
</style>
