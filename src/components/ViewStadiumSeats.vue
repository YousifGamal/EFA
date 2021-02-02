<template>
  <div class="container">
    <img src="./stadium.jpg">
    <div class="row">
      <div class="col-8 py-5">
        <div>
          <b-table class="mx-auto">
            <tbody>
              <tr v-for="idxr in rows" :key="idxr">
                <td v-for="idxc in cols" :key="idxc" class="pl-2" style="width: 10px;">
                  <div v-bind:class="{ clicked: isClicked[idxc+(idxr-1)*cols - 1], notClicked: !isClicked[idxc+(idxr-1)*cols - 1]}">
                    <img src="./seat.png">
                  </div>
                </td>
              </tr>
            </tbody>
          </b-table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  //import Vue from 'vue';
  import axios from 'axios';
  const seatsPath = "http://127.0.0.1:5000/getStadiumsSeats";
  export default {
    name: 'StadiumSeats',
    data() {
      return {
        rows: 10,
        cols: 10,
        isClicked: [],
        reservedSeats: []
      }
    },
    methods: {
      generateSeats:function(r,c) {
        for (let y = 1; y <= r; ++y) {
          for (let x = 1; x <= c; ++x) {
            this.isClicked.push(false);            
          }
        }
        for(let i=0; i<this.reservedSeats.length; i++){
          this.isClicked[this.reservedSeats[i]] = true;
        }
      }
    },
    beforeMount(){
      axios.get(seatsPath,{params:{match_id: 1}})
      .then(res => {this.rows =  res.data[0][0]; 
          this.cols = res.data[0][1];
          this.reservedSeats = res.data[0][2];
          this.generateSeats(this.rows, this.cols);
          })
      .catch(err => console.log(err))
    }
  }
</script>

<style scoped>
.notClicked{
    background:green;
}
.clicked{
    background:red;
}
</style>
