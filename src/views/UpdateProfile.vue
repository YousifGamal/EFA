<template>
<div>
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <b-navbar-brand href="/">Home</b-navbar-brand>
      <b-navbar-brand href="/manager">Manager</b-navbar-brand>
      <b-navbar-brand href="/user">User</b-navbar-brand>


      <b-collapse id="nav-collapse" is-nav>

        <b-navbar-nav class="ml-auto" >

          <b-navbar-brand href="/update">Profile</b-navbar-brand>
          <b-navbar-brand href="/login">Logout</b-navbar-brand>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>


  <div class="card">
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">

      <b-form-group label="Username" label-for="username">
        <b-form-input
          v-model="form.username"
          placeholder="Enter name"
          disabled
        ></b-form-input>
      </b-form-group>

      <b-form-group label="Email address" label-for="input-1">
        <b-form-input
          v-model="form.email"
          type="email"
          placeholder="Enter email"
          disabled
        ></b-form-input>
      </b-form-group>

      <b-form-group  label="First Name" label-for="First Name">
        <b-form-input
          v-model="form.first_name"
          type="text"
          placeholder="Enter first name"
          required
        ></b-form-input>
      </b-form-group>

       <b-form-group  label="Last Name" label-for="last Name">
        <b-form-input
          v-model="form.last_name"
          type="text"
          placeholder="Enter last name"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group  label="Birth Date" label-for="birth_date">
        <b-form-datepicker id="birth_date"  v-model="form.birth_date" locale="en" required>
        </b-form-datepicker>
      </b-form-group>

      <b-form-group  label="City" label-for="city">
        <b-form-input
          v-model="form.city"
          type="text"
          placeholder="Enter your city"
          required
        ></b-form-input>
      </b-form-group>


      <b-form-group  label="Address" label-for="address">
        <b-form-input
          v-model="form.address"
          type="text"
          placeholder="Enter your address"
        ></b-form-input>
      </b-form-group>


      <!-- <b-form-group  label="Password" label-for="password">
        <b-form-input
          v-model="form.password"
          type="password"
          placeholder="Enter new password"
          required
        ></b-form-input>
      </b-form-group> -->

      <b-form-group label="Gender:" label-for="gender">
        <b-form-select
          v-model="form.gender"
          :options="genders"
          required
        ></b-form-select>
      </b-form-group>

      <b-form-group label="Role:" label-for="role">
        <b-form-select
          v-model="form.role"
          :options="roles"
          required
        ></b-form-select>
      </b-form-group>

      <b-button-group>
      <b-button type="edit" variant="success">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
      </b-button-group>
    </b-form>
   
  </div>
</div>
</template>

<script>
  import axios from 'axios';
  const profilePath = "http://127.0.0.1:5000/profile";
  const updatePath = "http://127.0.0.1:5000/profileUpdate";
  export default {
    data() {
      return {
        form: {
          username:'',
          email: '',
          first_name: '',
          last_name:'',
          gender:'',
          role:'',
          // password:'',
          city:'',
          address:'',
          birth_date:''
          
        },
        
        genders: ['Male', 'Female'],
        roles:['Fan', 'Manager'],
        show: true
      }
    },

    methods: {
      onSubmit(event) {
        event.preventDefault()
        // update current userprofile
      axios.put(updatePath,this.form).then(res => {
        console.log(res);

      })
      },
      onReset(event) {
        event.preventDefault()
        // Reset our form values
        this.form.role = ''
        this.form.first_name = ''
        this.form.last_name = ''
        this.form.gender=''
        // this.form.birth_date=''
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
    },
      beforeMount(){
      axios.get(profilePath,{params:{username: "onetwo"}}) 
      .then(res => {
        this.form = res.data.user
      }).catch(err => console.log(err))
    }
  }
</script>

<style scoped>
.card{
  /* position: center ; */
  /* padding: 25% 25% 25% ,0%; */
  padding-left: 25%;
  padding-right: 25%;
  padding-top: 5%;
  padding-bottom: 2%;
}

.btn-group{
  width: 100%;
}

.myRow {
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