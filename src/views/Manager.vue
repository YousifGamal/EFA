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
                    <CreateMatch/>
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
                  <MatchCard/>
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

export default {
  name: 'Manager',
  components: {
    MatchCard,
    CreateMatch,
    AddStadium
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.myRow{
    padding-top: 20px;
}
</style>
