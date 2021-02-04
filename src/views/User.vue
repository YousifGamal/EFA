<template>
    <b-container fluid style="padding-left:0;padding-right:0">
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
        <b-row>
            <b-col cols="2"></b-col>
            <b-col cols="8">
              <b-row class="myRow">
                <b-col cols="12">
                  <div v-bind:key="match.id" v-for="match in matches.slice(start,end)">
                  <MatchCard v-on:matchedited="refreshMatches" v-bind:type="1" v-bind:match="match"/>
                  </div>
                </b-col>
              </b-row>
              <b-row class="myRow">
                <b-col cols="12">
                  <b-button :disabled="disablePrev" @click.prevent="retreat()" variant="outline-success"> Previous</b-button> - 
                  <b-button :disabled="disableNext" @click.prevent="advance()" variant="outline-success"> Next</b-button>
                </b-col>
              </b-row>
            </b-col>
            <b-col cols="2"></b-col>
        </b-row>
    </b-container>
</template>

<script>
import MatchCard from '@/components/MatchCard.vue'
import axios from 'axios';
import Pusher from 'pusher-js'
const matchesPath = "http://127.0.0.1:5000/getMatches";
export default {
  name: 'User',
  components: {
    MatchCard
  },
  data(){
    return{
      matches:[],
      start:0,
      end:3,
      disablePrev:true,
      disableNext:false
    }
  },
  created () {
    this.subscribe()
    //this.matchEdited()
  },
  methods:{
    getMatches(){
      axios.get(matchesPath,{})
      .then(res => this.matches = res.data)
      .catch(err => console.log(err))
    },
    refreshMatches(){
      this.getMatches()
    },
    toggleReserveSeats(match){
      match.show = !match.show
    },
    advance(){
      this.start += 3
      this.end += 3
      this.disableButtons()
    },
    retreat(){
      this.start -= 3
      this.end -= 3
      this.disableButtons()
    },
    disableButtons(){
      this.disablePrev = false;
      this.disableNext = false;
      if(this.end > this.matches.length){
        this.disableNext = true;
      }
      if(this.start === 0){
        this.disablePrev = true;
      }
    },
    subscribe () {
    let pusher = new Pusher('53327a58e47a84312542', { cluster: 'eu' })
    pusher.subscribe('matches')
    pusher.bind('match-added', data => {
      console.log(data);
      this.getMatches()
      })
      pusher.bind('match-edited', data => {
      console.log(data);
      this.getMatches()
      })
    }
    
  },
  beforeMount(){
    this.getMatches()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.myRow{
    padding-top: 20px;
}
.row{
  margin-left: 0;
  margin-right: 0;
}
</style>
