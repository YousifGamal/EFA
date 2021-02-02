<template>
  <div>
    <img src="./stadium.jpg" class="std">
          <table class="mx-auto">
            <tbody>
              <tr v-for="idxr in rows" :key="idxr">
                <td v-for="idxc in cols" :key="idxc"  style="width: 10px;">
                  <div v-bind:class="{ clicked: isClicked[idxc+(idxr-1)*cols - 1], notClicked: !isClicked[idxc+(idxr-1)*cols - 1]}">
                    <img class="std" src="./seat.png">
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
  </div>
</template>

<script>
  //import Vue from 'vue';
  import axios from 'axios';
  const seatsPath = "http://127.0.0.1:5000/getStadiumsSeats";
  export default {
    name: 'ViewStadiumSeats',
    props:['matchId'],
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
      axios.get(seatsPath,{params:{match_id: this.matchId}})
      .then(res => {this.rows =  res.data[0][0]; 
          this.cols = res.data[0][1];
          this.reservedSeats = res.data[0][2];
          if(this.reservedSeats[0]==null) this.reservedSeats=[]
          this.generateSeats(this.rows, this.cols);
          })
      .catch(err => console.log(err))
    }
  }
</script>

<style scoped>
table.mx-auto
{
    table-layout:fixed;
    width:100%;
    border-spacing: 0;
}
.std{
    max-width: 100%;
}
.notClicked{
    background:green;
}
.clicked{
    background:red;
}

</style>
