<template>
  <div>

    <b-form @submit="onSubmit">
        <b-row class="myRow">
            <b-col cols="3">
            <label for="stadium-id">Stadium Name:</label>
            </b-col>
            <b-col cols="9">
                <b-form-input id="stadium-id" placeholder="Enter stadium name" type="text"
                    v-model="form.stadiumName">
                </b-form-input>
            </b-col>
        </b-row>
        <b-row class="myRow">
            <b-col cols="12">
             <b-alert  v-model="stadiumAlert" variant="danger">
                            Stadium Name Is Taken</b-alert>
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
    <!--
    <b-card class="mt-3" header="Form Data Result">
      <pre class="m-0">{{ form }}</pre>
    </b-card>
    -->
  </div>
</template>

<script>
import axios from 'axios';
const path = "http://127.0.0.1:5000/AddStadium";
export default {
  name: 'AddStadium',
  data() {
 
      return {
        form: {
            stadiumName:'',
            rows:0,
            seatsPerRow:0
        },
        stadiums: ['Borg El Arab', 'El Salam', 'Cairo Stadium', 'Ismaili Stadium', 'M7la Stadium'],
        stadiumAlert:false
      }
    },
    methods: {
      onSubmit(event) {
        event.preventDefault()
        this.stadiumAlert = false;
        var payload = {
          stadiumName:this.form.stadiumName,
          rows: this.form.rows,
          seatsPerRow: this.form.seatsPerRow
        }
        axios.post(path,payload)
        .then(res => {
          console.log(res.data)
           if (res.data.res == true) {
          this.stadiumAlert = true;
          console.log("here at if")
        }
        else{
          console.log("here at else")
          this.form.stadiumName = '';
          this.form.rows = 0;
          this.form.seatsPerRow=0;
          //after adding the stadium emit global event
          this.$root.$emit('stadium-added')
        }
        })
        .catch(err => console.log(err));

       
        //alert(JSON.stringify(this.form))
      }
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
</style>
