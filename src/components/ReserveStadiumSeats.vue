<template>
  <div>
    <img src="./stadium.jpg" class="std">
    <div id="target-id"></div>
    <form name="form1" v-show="ticketCount>0">
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
      <button type="button" @click="required()" class="info">
        Buy Tickets
      </button>
    </form>
     <div class=info v-show="isPaid">Payment completed successfully.</div>
    <br>
          <table class="mx-auto">
            <tbody>
              <tr v-for="idxr in rows" :key="idxr">
                <td v-for="idxc in cols" :key="idxc" style="width: 10px;">
                  <div v-bind:class="{clicked: isReserved[idxc+(idxr-1)*cols - 1], inProgress: isClicked[idxc+(idxr-1)*cols - 1], notClicked: !isClicked[idxc+(idxr-1)*cols - 1]}"  @click="onSeatSelected(idxr, idxc)" >
                    <img src="./seat.png" class="std">
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
  </div>
</template>

<script>
  import axios from 'axios';
  import Pusher from 'pusher-js' // import Pusher
  const seatsPath = "http://127.0.0.1:5000/getStadiumsSeats";
  const reserveSeatsPath = "http://127.0.0.1:5000/addSeats";  
  export default {
    name: 'StadiumSeats',
    data() {
      return {
        isSubmit: false,
        wrongCardNumber: false,
        wrongCardPin: false,
        rows: 10,
        cols: 10,
        ticketCount:0,
        reservedSeats: [],
        isClicked: [],
        isReserved: [],
        reservedSeatsBeforehead: [],
        matchId: 2,
        userId: 1,
        alreadyReservedSeats:[],
        alreadyReservedSeats2:[],
        isPaid: false
      }
    },
    created () {
    // ...
      this.subscribe()
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
          for(let i=0; i<this.reservedSeats.length; i++){
            this.isReserved[this.reservedSeats[i]] = true;
            this.isClicked[this.reservedSeats[i]] = false;
            this.reservedSeatsBeforehead.push(this.reservedSeats[i]);
          }
          
          var payload = {
            matchId: this.matchId,
            userId: this.userId,
            seats: this.reservedSeats
          }

          axios.post(reserveSeatsPath,payload)
          .then(res => {this.alreadyReservedSeats =  res.data;
            if(this.alreadyReservedSeats.length==0){
              this.$root.$emit('seat-reserved');
              this.isPaid = true;
              this.ticketCount = 0;
            }else{
              this.ticketCount = 0;
              for(let i=0; i<this.alreadyReservedSeats.length; i++){
                for(let i=0; i<this.reservedSeatsBeforehead.length; i++){
                  if(this.reservedSeatsBeforehead[i]==this.alreadyReservedSeats[i])
                    this.reservedSeatsBeforehead.splice(i, 1);
                }
                let r=Math.ceil(this.alreadyReservedSeats[i]/this.cols);
                let c=this.alreadyReservedSeats[i]+1-(r-1)*this.cols;
                document.getElementById('target-id').innerHTML = '<p>Seat at row number '+r+' and column ' +c+' is already taken. ';
              }
            }

          })
          .catch(err => console.log(err));
          this.$forceUpdate();
      },
      onSeatSelected: function (r, c) { 
          this.isPaid=false;
          let seatIndx = c+(r-1)*this.cols - 1;
          if(this.reservedSeatsBeforehead.includes(seatIndx)) return;
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
          this.$forceUpdate();
      },
      subscribe () {
        let pusher = new Pusher('53327a58e47a84312542', { cluster: 'eu' })
        pusher.subscribe('seats')
        pusher.bind('seat-reserved', data => {
          console.log(data);
          axios.get(seatsPath,{params:{match_id: 2}})
          .then(res => {this.rows =  res.data[0][0]; 
              this.cols = res.data[0][1];
              this.reservedSeatsBeforehead = res.data[0][2];
              if(this.reservedSeats[0]==null) this.reservedSeats=[]
              this.generateSeats(this.rows, this.cols);
              })
          .catch(err => console.log(err))
        })
      },
      generateSeats:function(r,c) {
        for (let y = 1; y <= r; ++y) {
          for (let x = 1; x <= c; ++x) {
            this.isClicked.push(false);
            this.isReserved.push(false);            
          }
        }
        for(let i=0; i<this.reservedSeatsBeforehead.length; i++){
          this.isReserved[this.reservedSeatsBeforehead[i]] = true;
        }
      }
    },
    beforeMount(){
      axios.get(seatsPath,{params:{match_id: 2}})
      .then(res => {this.rows =  res.data[0][0]; 
          this.cols = res.data[0][1];
          this.reservedSeatsBeforehead = res.data[0][2];
          if(this.reservedSeats[0]==null) this.reservedSeats=[]
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
.inProgress{
    background:yellow;
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
table.mx-auto
{
    table-layout:fixed;
    width:100%;
    border-spacing: 0;
}
.std{
    max-width: 100%;
}
</style>
