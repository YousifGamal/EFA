<template>
  <div>
    <b-card bg-variant="success" text-variant="black">
        <b-card-title>
        {{match.homeName}} vs. {{match.awayName}}
        </b-card-title>
        <b-card-sub-title sub-title-text-variant = "black" sub-title-tag="h5">
        {{match.stadiumName}}, {{match.date}}, {{match.time}}
        </b-card-sub-title>
        <b-card-text>
        Main Refree: {{match.refName}}, Linesmen: {{match.lName1}}, {{match.lName2}}
        </b-card-text>
        <b-button v-show="type" :disabled="disbaleEdit" size="lg" @click.prevent="toggleEditMatch()"  variant="outline-dark">{{editMatchButtonText}}</b-button>  
        <b-button v-show="type" size="lg" @click.prevent="toggleStadium()" variant="outline-dark">Seats Details</b-button>
    </b-card>
    <CreateMatch v-if="editMatch"  v-on:matchedited="closeCreateMatchCard" 
    v-bind:match="match"  v-bind:matchId="match.id" ></CreateMatch>
    <ViewStadiumSeats  v-if="showStadium" v-bind:matchId="match.id"></ViewStadiumSeats>
  </div>
</template>

<script>

import CreateMatch from '@/components/CreateMatch.vue'
import ViewStadiumSeats from '@/components/ViewStadiumSeats.vue'
import axios from 'axios';
const numberOfResrvSeatsPath = "http://127.0.0.1:5000/numberOfReservedSeats";

export default {
  name: 'MatchCard',
  components: {
    CreateMatch,
    ViewStadiumSeats
  },
  props:["match","type"], 
  data(){
    return {
      editMatch: false,
      editMatchButtonText:'Edit Match Details',
      showStadium:false,
      disbaleEdit:false
    }
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
</style>
