<template>
  <div class="container">
    <form name="form1" v-show="showDialog">
    <div class="row">
      <div class="col">
        <label>Card Number  </label>
        <input name ='text1' type="number" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter card number" >
      </div>
      <div class=rq v-show="wrongCardNumber">Please input the card number.</div>
      <br>
      <div class="col">
        <label>Card Pin </label>
        <input name ='text2' type="number" class="form-control" id="exampleInputPassword1" placeholder="Pin">
      </div>
      <div class=rq v-show="wrongCardPin">Please input the card pin.</div>
      <br>
    </div>
      <button type="button" @click="required()" :disabled="isSubmit" class="info">
        Submit
      </button>
      <br><br>
      <div class=info v-show="isSubmit">Payment completed successfully.</div>
    </form>
  
    <br>
    <img src="./stadium.jpg">
    <br><br>
    <button type="button" @click="showDialog = true" :disabled="ticketCount==0" class="info">
        buy tickets
    </button>
    <br><br>
    <div class="row">
      <div class="col-8 py-5">
        <div>
          <b-table class="mx-auto">
            <tbody>
              <tr v-for="idxr in rows" :key="idxr">
                <td v-for="idxc in cols" :key="idxc" class="pl-2" style="width: 10px;">
                  <div v-bind:class="{ clicked: isClicked[idxc+(idxr-1)*cols - 1], notClicked: !isClicked[idxc+(idxr-1)*cols - 1]}"  @click="onSeatSelected(idxr, idxc)" >
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
  import vDialog from 'v-dialogs';
  export default {
    name: 'StadiumSeats',
    data() {
      return {
        isSubmit: false,
        wrongCardNumber: false,
        wrongCardPin: false,
        showDialog: false,
        rows: 10,
        cols: 10,
        ticketCount:0,
        reservedSeats: [],
        isClicked: []
      }
    },
    methods: {
      required: function(){
          var empt = document.forms["form1"]["text1"].value;
          var empt2 = document.forms["form1"]["text2"].value;
          if (empt == ""){
            this.wrongCardNumber = true;
            return;
          }
          else
            this.wrongCardNumber = false;
          if(empt2 == ""){
            this.wrongCardPin = true;
            return;
          }
          else
            this.wrongCardPin = false;
          
          this.isSubmit=true;

      },
      onSeatSelected: function (r, c) { 
          let seatIndx = c+(r-1)*this.cols - 1;
          if(this.isClicked[seatIndx]==true){
            this.isClicked[seatIndx]=false;
            this.ticketCount--;
            for(let i=0; i<this.reservedSeats.length; i++){
              if(this.reservedSeats[i]==seatIndx)
                this.reservedSeats.splice(i, 1);
            }
          }
          else{
            this.isClicked[seatIndx]=true;
            this.ticketCount++;
            this.reservedSeats.push(seatIndx);
          } 
          console.log(this.reservedSeats);
          this.$forceUpdate();
      },
      generateSeats:function() {
        let indx = 0;
        for (let y = 1; y <= this.rows; ++y) {
          for (let x = 1; x <= this.cols; ++x) {
            this.isClicked.push(false);
          }

        }
      }
    },
    beforeMount(){
      this.generateSeats()
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
.info {
    background-color: #13ce66;
    color: #fff;
  }
.rq {
color: 
#FF0000;
font-size: 10pt;
}
</style>
