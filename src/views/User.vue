<template>
    <b-container fluid >
        <b-row>
            <b-col cols="2"></b-col>
            <b-col cols="8">
              <b-row class="myRow">
                <b-col cols="12">
                  <div v-bind:key="match.id" v-for="match in matches">
                  <MatchCard v-on:matchedited="refreshMatches" v-bind:type="false" v-bind:match="match"/>
                  <b-button @click.prevent="toggleReserveSeats(match)" variant="outline-dark">Seats Details</b-button>
                  <ReserveStadiumSeats  v-show="match.show" v-bind:matchId="match.id" v-bind:userId="1"></ReserveStadiumSeats>
                  </div>
                </b-col>
              </b-row>
            </b-col>
            <b-col cols="2"></b-col>
        </b-row>
    </b-container>
</template>

<script>
import MatchCard from '@/components/MatchCard.vue'
import ReserveStadiumSeats from '@/components/ReserveStadiumSeats.vue'
import axios from 'axios';
const matchesPath = "http://127.0.0.1:5000/getMatches";
export default {
  name: 'User',
  components: {
    MatchCard,
    ReserveStadiumSeats
  },
  data(){
    return{
      matches:[]
    }
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
    }
  },
  beforeMount(){
    this.getMatches()
  },
  mounted(){
  //catch the global event of stadium added 
  this.$root.$on('new-match',()  =>{
    this.getMatches()
  })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.myRow{
    padding-top: 20px;
}
</style>
