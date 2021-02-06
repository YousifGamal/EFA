<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <b-navbar-brand href="/">Home</b-navbar-brand>
      <b-navbar-brand href="/manager">Manager</b-navbar-brand>
      <b-navbar-brand href="/user">User</b-navbar-brand>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto">
          <b-navbar-brand href="/update">Profile</b-navbar-brand>
          <b-navbar-brand href="/login" @click="Logout()"
            >Logout</b-navbar-brand
          >
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

        <b-form-group label="First Name" label-for="First Name">
          <b-form-input
            v-model="form.first_name"
            type="text"
            placeholder="Enter first name"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group label="Last Name" label-for="last Name">
          <b-form-input
            v-model="form.last_name"
            type="text"
            placeholder="Enter last name"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group label="Birth Date" label-for="birth_date">
          <b-form-datepicker
            id="birth_date"
            v-model="form.birth_date"
            locale="en"
            required
          >
          </b-form-datepicker>
        </b-form-group>

        <b-form-group label="City" label-for="city">
          <b-form-input
            v-model="form.city"
            type="text"
            placeholder="Enter your city"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group label="Address" label-for="address">
          <b-form-input
            v-model="form.address"
            type="text"
            placeholder="Enter your address"
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
    <div class="card">
      <b-form @submit="onChange" @reset="onReset">
        <b-form-group label="Old Password" label-for="password1">
          <b-form-input
            v-model="password"
            type="password"
            placeholder="Enter your old password"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group label="New Password" label-for="password2">
          <b-form-input
            v-model="newPassword"
            type="password"
            placeholder="Enter your new password"
            required
          ></b-form-input>
        </b-form-group>
        <b-button-group>
          <b-button type="edit" variant="success">Change Password</b-button>
        </b-button-group>
      </b-form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
const profilePath = "http://127.0.0.1:5000/profile";
const updatePath = "http://127.0.0.1:5000/profileUpdate";
const updatePassword = "http://127.0.0.1:5000/passUpdate";
export default {
  data() {
    return {
      form: {
        username: "",
        email: "",
        first_name: "",
        last_name: "",
        gender: "",
        role: "",
        // password:'',
        city: "",
        address: "",
        birth_date: "",
      },
      prevRole: "",
      genders: ["Male", "Female"],
      roles: ["Fan", "Manager"],
      show: true,
      newPassword: "",
      password: "",
      token: localStorage.getItem("token"),
    };
  },

  methods: {
    onSubmit(event) {
      event.preventDefault();

      // update current userprofile
      if ((this.prevRole === "Fan") & (this.form.role === "Manager")) {
        console.log("change status");
        this.form.status = 1;
        axios
          .put(updatePath, this.form, {
            headers: { "x-access-token": `${this.token}` },
          })
          .then((res) => {
            if (res.code === 401) {
              console.log("dadma;dladmadmad;amdasdml");
            }
          })
          .catch((err) => {
            console.log("error here", err.code);
          });
        window.localStorage.clear();
        this.$router.push({ name: "Login" });
      } else {
        this.form.status = 0;
        axios
          .put(updatePath, this.form, {
            headers: { "x-access-token": `${this.token}` },
          })
          .then((res) => {
            console.log(res);
          });
      }

      this.$notify({
        group: "login",
        type: "success",
        title: "Profile Updated.",
        // text: "Try again..",
        duration: 3000,
      });
    },
    onChange(event) {
      event.preventDefault();

      const payload = {
        username: this.form.username,
        password: this.password,
        newPassword: this.newPassword,
      };
      axios
        .put(updatePassword, payload, {
          headers: { "x-access-token": `${this.token}` },
        })
        .then((res) => {
          console.log(res);
          if (res.data.update === "failed") {
            this.$notify({
              group: "login",
              type: "error",
              title: "Failed to update Password.",
              text: "Password is incorrect Try again..",
              duration: 3000,
            });
          } else {
            this.$notify({
              group: "login",
              type: "success",
              title: "Password Updated.",
              // text: "Try again..",
              duration: 3000,
            });
          }
        });
    },
    onReset(event) {
      event.preventDefault();
      // Reset our form values
      this.form.role = "";
      this.form.first_name = "";
      this.form.last_name = "";
      this.form.gender = "";
      // this.form.birth_date=''
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
    Logout() {
      window.localStorage.clear();
      // this.$router.push({ name: "Login" });
    },
  },
  beforeMount() {
    const username = window.localStorage.getItem("username");
    console.log(this.token);
    axios
      .get(profilePath, {
        params: { username: username },
        headers: { "x-access-token": `${this.token}` },
      })
      .then((res) => {
        this.form = res.data.user;
        this.prevRole = this.form.role;
      })
      .catch((err) => console.log(err));
  },
};
</script>

<style scoped>
.card {
  /* position: center ; */
  /* padding: 25% 25% 25% ,0%; */
  padding-left: 25%;
  padding-right: 25%;
  padding-top: 5%;
  padding-bottom: 2%;
}

.btn-group {
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
