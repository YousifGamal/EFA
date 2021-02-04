<template>
  <div>
    <b-card  border-variant="success" header="MATCH" text-variant="black">
        <b-card-title>
        {{match.homeName}} vs. {{match.awayName}}
        </b-card-title>
        <b-card-sub-title sub-title-text-variant = "black" sub-title-tag="h5">
        {{match.stadiumName}}, {{match.date}}, {{match.time}}
        </b-card-sub-title>
        <b-card-text>
        Main Refree: {{match.refName}}, Linesmen: {{match.lName1}}, {{match.lName2}}
        </b-card-text>
        <b-button v-show="type === 0" :disabled="disbaleEdit" size="lg" @click.prevent="toggleEditMatch()"  
        variant="outline-dark" class="btl">{{editMatchButtonText}}</b-button>  
        <b-button v-show="type === 0 || type === 2" size="lg" @click.prevent="toggleStadium()" 
        variant="outline-dark" class="btr">Seats Details</b-button>
        <b-button v-show="type === 1" size="lg" @click.prevent="toggleReserveSeats()" variant="outline-dark">Reserve Seats</b-button>
    </b-card>
    <CreateMatch v-if="editMatch"  v-on:matchedited="closeCreateMatchCard" 
    v-bind:match="match"  v-bind:matchId="match.id" ></CreateMatch>
    <ViewStadiumSeats  v-if="showStadium" v-bind:matchId="match.id"></ViewStadiumSeats>
    <ReserveStadiumSeats  v-show="showReserve" v-bind:matchId="match.id" v-bind:userId="1"></ReserveStadiumSeats>
  </div>
</template>

<script>

import CreateMatch from '@/components/CreateMatch.vue'
import ViewStadiumSeats from '@/components/ViewStadiumSeats.vue'
import ReserveStadiumSeats from '@/components/ReserveStadiumSeats.vue'
import axios from 'axios';
import Pusher from 'pusher-js';
const numberOfResrvSeatsPath = "http://127.0.0.1:5000/numberOfReservedSeats";

export default {
  name: 'MatchCard',
  components: {
    CreateMatch,
    ViewStadiumSeats,
    ReserveStadiumSeats
  },
  props:["match","type"], 
  data(){
    return {
      editMatch: false,
      editMatchButtonText:'Edit Match Details',
      showStadium:false,
      disbaleEdit:false,
      showReserve:false
    }
  },
  created () {
    this.subscribe()
  },
  methods:{
    toggleEditMatch(){
      this.editMatch = !this.editMatch
    },
    toggleStadium(){
      this.showStadium = !this.showStadium
    },
    closeCreateMatchCard(){
      this.toggleEditMatch();
      this.$emit('matchedited')
    },
    toggleReserveSeats(){
      this.showReserve = !this.showReserve
    },
    subscribe () {
    let pusher = new Pusher('53327a58e47a84312542', { cluster: 'eu' })
    pusher.subscribe('seats')
    pusher.bind('seat-reserved', data => {
      console.log(data);
      axios.get(numberOfResrvSeatsPath,{params:{mid:this.match.id}})
      .then(res => {
        if(res.data == 0){
          this.disbaleEdit = false
        }
        else{
          this.disbaleEdit = true
        }
      })
      .catch(err => console.log(err))

        })
    }
  },
  beforeMount(){
    
    axios.get(numberOfResrvSeatsPath,{params:{mid:this.match.id}})
    .then(res => {
      if(res.data == 0){
        this.disbaleEdit = false
      }
      else{
        this.disbaleEdit = true
      }
    })
    .catch(err => console.log(err))
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.btl{
  margin-right: 2%;
}
.btr{
  margin-left: 2%;
}

</style>
