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
            <b-col cols="12">
             <b-alert  v-model="sameTeamAlert" variant="danger">
                            Home Team and Away Team CANNOT be the same</b-alert>
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
                <b-form-timepicker id="time-id"  :hour12="false" v-model="form.time" locale="en">
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
             <b-alert  v-model="sameLineman" variant="danger">
                            Select Two Different Linemen</b-alert>
            </b-col>
        </b-row>
        <b-row class="myRow">
            <b-col cols="12">
             <b-button v-if="createButton" type="submit" variant="success">CREATE</b-button>
             <b-button v-if="!createButton" :disabled="disableEditButton" type="submit" 
                                            variant="success">EDIT</b-button>
            </b-col>
        </b-row>
     
    </b-form>
    
    <b-card class="mt-3" header="Form Data Result">
      <pre class="m-0">{{ form }}</pre>
    </b-card>
    
  </div>
</template>

<script>
import axios from 'axios';
const stadiumsPath = "http://127.0.0.1:5000/getStadiums";
const teamsPath = "http://127.0.0.1:5000/getTeams";
const refereesPath = "http://127.0.0.1:5000/getReferees";
const linemenPath = "http://127.0.0.1:5000/getLinemen";
const createMatchPath = "http://127.0.0.1:5000/createMatch";
export default {
  name: 'CreateMatch',
  props:['matchId','match'],
  data() {
      const now = new Date()
      const today = new Date(now.getFullYear(), now.getMonth(), now.getDate())
      const minDate = new Date(today)
      
      
      return {
        form: {
            id:0,
            homeTeam:'',
            awayTeam:'',
            stadium:'',
            referee:'',
            lineman1:'',
            lineman2:'',
            date: '',
            time:''
        },
        /*teams: [ 'M7la', 'Ismaili FC', 'Pyramids','Zamalek'],
        stadiums: ['Borg El Arab', 'El Salam', 'Cairo Stadium', 'Ismaili Stadium', 'M7la Stadium'],
        referees: ['Ahmed hassan', 'Sayed Darwesh','Hossam Hassan'],
        linemen: ['Abelkader Hamad', 'Ahmed Huessenaen', 'Dawood EL Gamil', 'Ayman Ftaah'],
        */
        teams:[],
        stadiums:[],
        referees:[],
        linemen:[],
        min_date: minDate,
        sameTeamAlert: false,
        sameLineman: false,
        errorInForm: false,
        createButton: true,
        disableEditButton: false,
        seatsReservedFlag: false
      }
    },
    methods: {
      onSubmit(event) {
        event.preventDefault()
        //reset flags
        this.sameTeamAlert = false;
        this.sameLineman = false;
        this.errorInForm = false;
        //check for errors 
        if (this.form.homeTeam === this.form.awayTeam ) {
          this.sameTeamAlert = true;
          this.errorInForm = true;
        }
        if (this.form.lineman1 === this.form.lineman2){
          this.sameLineman = true;
          this.errorInForm = true;
        }
        //check if form is valid 
        if (this.errorInForm === false) {
          var payload = {
            homeTeam: this.form.homeTeam,
            awayTeam: this.form.awayTeam,
            stadium: this.form.stadium,
            referee: this.form.referee,
            lineman1: this.form.lineman1,
            lineman2: this.form.lineman2,
            mdate: this.form.date,
            mtime: this.form.time
          }
          axios.post(createMatchPath,payload)
          .then(res => {
            if (res.data == false) {
              this.form.homeTeam = '',
              this.form.awayTeam = '',
              this.form.stadium = '',
              this.form.referee = '',
              this.form.lineman1 = '',
              this.form.lineman2 = '',
              this.form.date = '',
              this.form.time = ''
            }
            else{
              console.log(res.data)
            }
          })
          .catch(err => console.log(err))
        }
        //alert(JSON.stringify(this.form))
      },
      fillMatchData(){ 
       /* this.form.homeTeam = "Carrots",
        this.form.awayTeam = "Beans",
        this.form.stadium = "Borg El Arab",
        this.form.referee = "Hossam Btngan",
        this.form.lineman1 = "Khaled Huessian",
        this.form.lineman2 = "Dawood EL Gamil",
        this.form.date = "2021-01-31",
        this.form.time = "00:59:00"*/
        /*
        this.form.homeTeam = this.match.homeTeam,
        this.form.awayTeam = this.match.awayTeam,
        this.form.stadium = this.match.stadium,
        this.form.referee = this.match.referee,
        this.form.lineman1 = this.match.lineman1,
        this.form.lineman2 = this.match.lineman2,
        this.form.date = this.match.date,
        this.form.time = this.match.time
        */
       this.form = this.match
      }
    },
     beforeMount(){
       if(this.matchId != "-1"){
        this.fillMatchData();
        this.createButton = false;
        if(this.seatsReservedFlag === true){
          this.disableEditButton = true;
        }
        //related to time cancel
        /* 
        var givenDate = new Date(this.match.date);
        var  currentDate = new Date();
        var daysFlag = (givenDate - currentDate) / (1000 * 3600 * 24);
        daysFlag = parseInt(flag)+1
        if (daysFlag > 3) {
        }
       */
        }
        //get selectors data
        //get stadiums
        axios.get(stadiumsPath,{})
        .then(res => this.stadiums =  res.data)
        .catch(err => console.log(err))
        //get teams
        axios.get(teamsPath,{})
        .then(res => this.teams = res.data)
        .catch(err => console.log(err))
        //get referees
        axios.get(refereesPath,{})
        .then(res => this.referees = res.data)
        .catch(err => console.log(err))
        //get Linemen
        axios.get(linemenPath,{})
        .then(res => this.linemen = res.data)
        .catch(err => console.log(err))
      }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.myRow{
    padding-top: 20px;
}

.form-control:focus {
  border-color: #08db12;
  box-shadow: 0 0 10px #72f705;
}
select:focus {
  border-color: #08db12;
  box-shadow: 0 0 10px #72f705;
}


</style>
