<template>
<div>
  <b-navbar toggleable="lg" type="dark" variant="dark">
    <b-navbar-brand href="/">Home</b-navbar-brand>
     <b-navbar-nav>
        <b-nav-item href="/login">Login</b-nav-item>
        <b-nav-item href="/about" disabled>about</b-nav-item>
      </b-navbar-nav>


    <b-collapse id="nav-collapse" is-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
        </b-nav-form>

        <b-nav-item-dropdown text="Lang" right>
          <b-dropdown-item href="#">EN</b-dropdown-item>
          <b-dropdown-item href="#">ES</b-dropdown-item>
          <b-dropdown-item href="#">RU</b-dropdown-item>
          <b-dropdown-item href="#">FA</b-dropdown-item>
        </b-nav-item-dropdown>

        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <template #button-content>
            <em>User</em>
          </template>
          <b-dropdown-item href="#">Profile</b-dropdown-item>
          <b-dropdown-item href="#">Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
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


      <b-form-group  label="Password" label-for="password">
        <b-form-input
          v-model="form.password"
          type="password"
          placeholder="Enter new password"
          required
        ></b-form-input>
      </b-form-group>

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
  export default {
    data() {
      return {
        form: {
          username:'Gellesh',
          email: 'sssss@ssssss.com',
          first_name: 'khaled',
          last_name:'galal',
          gender:'Male',
          role:'Fan',
          password:'kkkk',
          city:'Giza',
          address:'',
          birth_date:'2020-01-01'
          
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
      },
      onReset(event) {
        event.preventDefault()
        // Reset our form values
        this.form.role = ''
        this.form.first_name = ''
        this.form.last_name = ''
        this.form.gender=''
        this.form.birth_date=''
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
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