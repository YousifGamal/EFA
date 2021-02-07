<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="dark">
          <b-navbar-brand href="/user">Home</b-navbar-brand>
          <b-navbar-brand href="/Tickets">My Tickets</b-navbar-brand>

          <b-collapse id="nav-collapse" is-nav>

            <b-navbar-nav class="ml-auto" >

              <b-navbar-brand href="/update">Profile</b-navbar-brand>
              <b-navbar-brand href="/login">Logout</b-navbar-brand>
            </b-navbar-nav>
          </b-collapse>
      </b-navbar>
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
      tickets:[],
      token:window.localStorage.getItem("token")
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
            axios.get("http://localhost:5000/deleteticket/"+id,{
        headers: { "x-access-token": `${this.token}` },
      })
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
      axios.get("http://localhost:5000/showusertickets/"+(window.localStorage.getItem("id")),{
        headers: { "x-access-token": `${this.token}` },
      })
      .then(res => this.tickets = res.data)
      .catch(err => console.log(err))  
    })
    }
  },
  beforeMount(){
    
    axios.get("http://localhost:5000/showusertickets/"+(window.localStorage.getItem("id")),{
        headers: { "x-access-token": `${this.token}` },
      })
    .then(res => this.tickets = res.data)
    .catch(err => console.log(err))
  },created(){
    this.subscribe();
  }
}
</script>

<style>
</style>
