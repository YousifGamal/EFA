<template>
  <div>
    <b-card bg-variant="success" text-variant="black">
        <b-card-title>
        {{match.homeTeam}} vs. {{match.awayTeam}}
        </b-card-title>
        <b-card-sub-title sub-title-text-variant = "black" sub-title-tag="h5">
        {{match.stadium}}, {{match.date}}, {{match.time}}
        </b-card-sub-title>
        <b-card-text>
        Main Refree: {{match.referee}}, Linesmem: {{match.lineman1}}, {{match.lineman2}}
        </b-card-text>
        <b-button size="lg" @click.prevent="toggleEditMatch()"  variant="outline-dark">Edit Match Details</b-button> -
        <b-button size="lg"  variant="outline-dark">Seats Details</b-button>
    </b-card>
    <CreateMatch v-if="editMatch" v-bind:match="match" v-bind:matchId="match.id" ></CreateMatch>
  </div>
</template>

<script>
import CreateMatch from '@/components/CreateMatch.vue'
export default {
  name: 'MatchCard',
  components: {
    CreateMatch
  },
  props:["match"], 
  data(){
    return {
      editMatch: false,
      matchh: {
            homeTeam:"Zamalek",
            awayTeam:"Pyramidss",
            stadium:"M7la Stadium",
            referee:"Hossam Hassan",
            lineman1:"Ahmed Huessenaen",
            lineman2:"Abelkader Hamad",
            date: "2021-01-31",
            time:"00:59:00"
        }
    }
  },
  methods:{
    toggleEditMatch(){
      this.editMatch = !this.editMatch
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
