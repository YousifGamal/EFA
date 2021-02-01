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
                  <div v-bind:class="{ clicked: isClicked[idxc+(idxr-1)*cols - 1], notClicked: !isClicked[idxc+(idxr-1)*cols - 1]}" >
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
  import Vue from 'vue';
  
  export default {
    name: 'StadiumSeats',
    data() {
      return {
        selectedSeat: null,
        rows: 10,
        cols: 10,
        seats: [],
        isClicked: []
      }
    },
    methods: {
      onSeatSelected: function (r, c) {
          let seatIndx = c+(r-1)*this.cols - 1;
          if(this.isClicked[seatIndx]==true)
            this.isClicked[seatIndx]=false;
          else
            this.isClicked[seatIndx]=true;
          
          if(this.seats[seatIndx].status == 'RA'){
              this.seats[seatIndx].status = 'RB';
          }
          else
              this.seats[seatIndx].status = 'RA'; 
          this.$forceUpdate();
      },
      generateSeats:function() {
        for (let y = 1; y <= this.rows; ++y) {
          for (let x = 1; x <= this.cols; ++x) {
            this.isClicked.push(false);            
          }

        }
        this.isClicked[10] = true;
        this.isClicked[11] = true;
        this.isClicked[12] = true;
      }
    },
    beforeMount(){
      this.rows = 5;
      this.cols = 6;
      this.generateSeats();
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
