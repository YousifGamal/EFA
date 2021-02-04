<template>
    <b-container fluid >
        <b-row>
            <b-col cols="2"></b-col>
            <b-col cols="8">
              <b-row class="myRow">
                <b-col cols="12">
                  <b-button v-b-toggle.createMatchCollapse block variant="outline-success">
                    CREATE NEW MATCH</b-button>   
                  <b-collapse id="createMatchCollapse">
                    <CreateMatch matchId="-1"></CreateMatch>
                  </b-collapse>
                </b-col>
              </b-row>
              <b-row class="myRow">
                <b-col cols="12">
                  <b-button v-b-toggle.createStadiumCollapse block variant="outline-success">
                    ADD NEW Stadium</b-button>   
                  <b-collapse id="createStadiumCollapse">
                    <AddStadium/>
                  </b-collapse>
                </b-col>
              </b-row>
              <b-row class="myRow">
                <b-col cols="12">
                  <div v-bind:key="match.id" v-for="match in matches">
                  <MatchCard v-bind:type="true" v-on:matchedited="refreshMatches" v-bind:match="match"/>
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
import CreateMatch from '@/components/CreateMatch.vue'
import AddStadium from '@/components/AddStadium.vue'
import axios from 'axios';
const matchesPath = "http://127.0.0.1:5000/getMatches";
export default {
  name: 'Manager',
  components: {
    MatchCard,
    CreateMatch,
    AddStadium
  },
  data(){
    return{
      matches:[]
      /*
      matches: [
        {
          id:1,
          homeTeam:"Zamalek",
          awayTeam:"Pyramids",
          stadium:"M7la Stadium",
          referee:"Hossam Hassan",
          lineman1:"Ahmed Huessenaen",
          lineman2:"Abelkader Hamad",
          date: "2021-02-04",
          time:"00:59:00"
        },
        {
          id:2,
          homeTeam:"Ismaili FC",
          awayTeam:"M7la",
          stadium:"Ismaili Stadium",
          referee:"Hossam Hassan",
          lineman1:"Ahmed Huessenaen",
          lineman2:"Abelkader Hamad",
          date: "2021-01-30",
          time:"00:59:00"
        }
      ]*/
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
