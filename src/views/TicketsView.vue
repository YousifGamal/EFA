<template>
  <div>
    <!--
    Search for ticket : 
    <input type="text" name="search" v-model="searchInput" placeholder="search for user..." @keyup="searchUser" />-->
    <div class="container">
      <b-card border-variant="success" text-variant="black" header="My Tickets">
        <ticketList v-bind:ticketsList="tickets" v-on:del-ticket="deleteTicket"/>
      </b-card>
    </div>
  </div>
</template>

<script>
import ticketList from '../components/ticketList'
import axios from 'axios'
import Pusher from 'pusher-js';

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
    },
    subscribe () {
    let pusher = new Pusher('53327a58e47a84312542', { cluster: 'eu' })
    pusher.subscribe('seats')
    pusher.bind('seat-reserved', data => {
      console.log(data);
      axios.get("http://localhost:5000/showusertickets/"+1) // lazem tt3dl
      .then(res => this.tickets = res.data)
      .catch(err => console.log(err))  
    })
    }
  },
  beforeMount(){
    
    axios.get("http://localhost:5000/showusertickets/"+1) // lazem tt3dl
    .then(res => this.tickets = res.data)
    .catch(err => console.log(err))
  },created(){
    this.subscribe();
  }
}
</script>

<style>
</style>
