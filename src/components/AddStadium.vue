<template>
  <div>

    <b-form @submit="onSubmit">
        <b-row class="myRow">
            <b-col cols="3">
            <label for="stadium-id">Stadium Name:</label>
            </b-col>
            <b-col cols="9">
                <b-form-input id="stadium-id" placeholder="Enter stadium name" :type="text"
                    v-model="form.stadiumName">
                </b-form-input>
            </b-col>
        </b-row>
        <b-row class="myRow">
            <b-col cols="3">
            <label for="rows-id">Number of Rows:</label>
            </b-col>
            <b-col cols="9">
                <b-form-input id="rows-id" min="1"  type="number"
                    v-model="form.rows">
                </b-form-input>
            </b-col>
        </b-row>

        <b-row class="myRow">
            <b-col cols="3">
            <label for="seats-id">Seats Per Row:</label>
            </b-col>
            <b-col cols="9">
                <b-form-input id="seats-id" min="1"  type="number"
                    v-model="form.seatsPerRow">
                </b-form-input>
            </b-col>
        </b-row>

        <b-row class="myRow">
            <b-col cols="12">
             <b-button type="submit" variant="success">ADD</b-button>
            </b-col>
        </b-row>

    </b-form>
    <b-card class="mt-3" header="Form Data Result">
      <pre class="m-0">{{ form }}</pre>
    </b-card>
  </div>
</template>

<script>
export default {
  name: 'AddStadium',
  data() {
 
      return {
        form: {
            homeTeam:'',
            awayTeam:'',
            stadium:'',
            referee:'',
            lineman1:'',
            lineman2:'',
            date: '',
            time:'',
            stadiumName:'',
            rows:0,
            seatsPerRow:0

        },
        teams: [ 'Carrots', 'Beans', 'Tomatoes', 'Corn'],
        stadiums: ['Borg El Arab', 'El Salam', 'Cairo Stadium', 'Stad de Mahla'],

        
        
      }
    },
    methods: {
      onSubmit(event) {
        event.preventDefault()
        alert(JSON.stringify(this.form))
      }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.myRow{
    padding-top: 20px;
}
</style>
