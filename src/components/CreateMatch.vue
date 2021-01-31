<template>
  <div>

    <b-form @submit="onSubmit">
        <b-row class="myRow">
            <b-col cols="3">
            <label for="home-team">Home Team:</label>
            </b-col>
            <b-col cols="9">
                    <b-form-select id="home-team" v-model="form.homeTeam" :options="teams"
                                                                    required></b-form-select>
            </b-col>
        </b-row>
        <b-row class="myRow">
            <b-col cols="3">
            <label for="away-team">Away Team:</label>
            </b-col>
            <b-col cols="9">
                    <b-form-select id="away-team" v-model="form.awayTeam" :options="teams"
                                                                    required></b-form-select>
            </b-col>
        </b-row>

        <b-row class="myRow">
            <b-col cols="3">
            <label for="stadium-id">Stadium:</label>
            </b-col>
            <b-col cols="9">
                    <b-form-select id="stadium-id" v-model="form.stadium" :options="stadiums"
                                                                    required></b-form-select>
            </b-col>
        </b-row>

        <b-row class="myRow">
            <b-col cols="3">
            <label for="date-id">Date:</label>
            </b-col>
            <b-col cols="9">
                    <b-form-datepicker id="date-id"  v-model="form.date" :min="min_date"  locale="en">
                    </b-form-datepicker>
            </b-col>
        </b-row>

        <b-row class="myRow">
            <b-col cols="3">
            <label for="time-id">Time:</label>
            </b-col>
            <b-col cols="9">
                <b-form-timepicker id="time-id" :hour12="false" v-model="form.time" locale="en">
                </b-form-timepicker>
            </b-col>
        </b-row>

        <b-row class="myRow">
            <b-col cols="3">
            <label for="referee-id">Main Referee:</label>
            </b-col>
            <b-col cols="9">
                    <b-form-select id="referee-id" v-model="form.referee" :options="referees"
                                                                    required></b-form-select>
            </b-col>
        </b-row>

        <b-row class="myRow">
            <b-col cols="3">
            <label for="lineman1-id">Lineman 1:</label>
            </b-col>
            <b-col cols="9">
                    <b-form-select id="lineman1-id" v-model="form.lineman1" :options="linemen"
                                                                    required></b-form-select>
            </b-col>
        </b-row>

        <b-row class="myRow">
            <b-col cols="3">
            <label for="lineman2-id">Lineman 2:</label>
            </b-col>
            <b-col cols="9">
                    <b-form-select id="lineman2-id" v-model="form.lineman2" :options="linemen"
                                                                    required></b-form-select>
            </b-col>
        </b-row>
        <b-row class="myRow">
            <b-col cols="12">
             <b-button type="submit" variant="success">CREATE</b-button>
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
  name: 'CreateMatch',
  data() {
      const now = new Date()
      const today = new Date(now.getFullYear(), now.getMonth(), now.getDate())
      const minDate = new Date(today)
      return {
        form: {
            homeTeam:'',
            awayTeam:'',
            stadium:'',
            referee:'',
            lineman1:'',
            lineman2:'',
            date: '',
            time:''
        },
        teams: [ 'Carrots', 'Beans', 'Tomatoes', 'Corn'],
        stadiums: ['Borg El Arab', 'El Salam', 'Cairo Stadium', 'Stad de Mahla'],
        referees: ['Ahmed hassan', 'Hossam Btngan', 'Sayed Darwesh'],
        linemen: ['Khaled Huessian', 'Dawood EL Gamil', 'Ayman Ftaah'],
        min_date: minDate
        
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
