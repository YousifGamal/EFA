<template>
  <div class="row">
    <div class="col-md-6 mx-auto p-0">
      <div class="card-transparent">
        <div class="login-box">
          <div class="login-snip">
            <input
              id="tab-1"
              type="radio"
              name="tab"
              class="sign-in"
              checked
            /><label for="tab-1" class="tab">Login</label>
            <input id="tab-2" type="radio" name="tab" class="sign-up" /><label
              for="tab-2"
              class="tab"
              >Sign Up</label
            >
            <div class="login-space">
              <form class="login">
                <div class="group">
                  <label for="user" class="label">Username</label>
                  <input
                    id="login_username"
                    v-model="login_data.login_username"
                    type="text"
                    class="input"
                    placeholder="Enter your username"
                    required
                  />
                </div>
                <div class="group">
                  <label for="pass" class="label">Password</label>
                  <input
                    id="login_pass"
                    v-model="login_data.login_pass"
                    type="password"
                    class="input"
                    data-type="password"
                    placeholder="Enter your password"
                    required
                  />
                </div>
                <!-- <div class="group">
                  <input id="check" type="checkbox" class="check" checked />
                  <label for="check"
                    ><span class="icon"></span> Keep me Signed in</label
                  >
                </div> -->
                <div class="group">
                  <input
                    type="button"
                    @click="login($event)"
                    class="button"
                    value="Sign In"
                  />
                </div>

                <div class="hr"></div>
                <div class="group">
                  <input
                    type="button"
                    @click="login_guest()"
                    class="button"
                    value="Login as guest"
                  />
                </div>
              </form>
              <form class="sign-up-form">
                <div class="group">
                  <label for="user" class="label">Username</label>
                  <input
                    id="username"
                    v-model="register_data.username"
                    type="text"
                    class="input"
                    placeholder="Enter your Username"
                    required
                  />
                </div>
                <div class="group">
                  <label for="user" class="label">First name</label>
                  <input
                    id="first-name"
                    v-model="register_data.first_name"
                    type="text"
                    class="input"
                    placeholder="First name"
                    required
                  />
                </div>
                <div class="group">
                  <label for="user" class="label">Last name</label>
                  <input
                    id="last-name"
                    v-model="register_data.last_name"
                    type="text"
                    class="input"
                    placeholder="Last Name"
                    required
                  />
                </div>
                <div class="group">
                  <label for="gender" class="label">Gender</label>
                  <select
                    v-model="register_data.gender"
                    class="form-control"
                    id="Gender"
                  >
                    <option>Male</option>
                    <option>Female</option>
                  </select>
                </div>
                <div class="group">
                  <label for="role" class="label">role</label>
                  <select
                    v-model="register_data.role"
                    class="form-control"
                    id="role"
                  >
                    <option>Manager</option>
                    <option>Fan</option>
                  </select>
                </div>
                <div class="group">
                  <label for="user" class="label">City</label>
                  <input
                    id="city"
                    v-model="register_data.city"
                    type="text"
                    class="input"
                    placeholder="Enter your city"
                    required
                  />
                </div>
                <div class="group">
                  <label for="user" class="label">Address</label>
                  <input
                    id="address"
                    v-model="register_data.address"
                    type="text"
                    class="input"
                    placeholder="Enter your Address"
                  />
                </div>

                <div class="group">
                  <label for="date" class="label">Birth Date</label
                  ><b-form-datepicker
                    id="date-id"
                    v-model="register_data.birth_date"
                    locale="en"
                    required
                  ></b-form-datepicker>
                </div>

                <div class="group">
                  <label for="pass" class="label">Password</label>
                  <input
                    id="pass1"
                    v-model="register_data.pass1"
                    type="password"
                    class="input"
                    data-type="password"
                    placeholder="Create your password"
                    required
                  />
                </div>
                <div class="group">
                  <label for="pass" class="label">Repeat Password</label>
                  <input
                    id="pass2"
                    v-model="register_data.pass2"
                    type="password"
                    class="input"
                    data-type="password"
                    placeholder="Repeat your password"
                    required
                  />
                  <!-- <button @click="showPassword">{{ btnText }}</button> -->
                </div>
                <div class="group">
                  <label for="pass" class="label">Email Address</label>
                  <input
                    id="email"
                    v-model="register_data.email"
                    type="email"
                    class="input"
                    placeholder="name@example.com"
                    required
                  />
                </div>
                <div class="group">
                  <input
                    type="button"
                    @click="signup($event)"
                    class="button"
                    value="Sign Up"
                  />
                </div>
                <div class="hr"></div>
                <div class="foot">
                  <label for="tab-1">Already Member?</label>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import $ from "jquery"; // import jquery
import axios from "axios";
const login = "http://127.0.0.1:5000/login";
const register = "http://127.0.0.1:5000/createUser";

export default {
  name: "Login",
  data() {
    return {
      login_data: { login_username: "", login_pass: "" },
      register_data: {
        username: "",
        first_name: "",
        last_name: "",
        gender: "Male",
        role: "Fan",
        city: "",
        address: "",
        email: "",
        pass1: "",
        pass2: "",
        birth_date: "2020-01-01",
      },
      //   type: 'password',
      //   btnText: 'Show Password'
    };
  },
  components: {},
  methods: {
    login() {
      // evt.preventDefault();
      const myForm = $(".login");

      if (!myForm[0].checkValidity()) {
        console.log(myForm[0].checkValidity());
        myForm[0].reportValidity();
      } else {
        console.log(this.login_data);
        axios
          .post(login, this.login_data)
          .then((res) => {
            window.localStorage.setItem(
              "username",
              this.login_data.login_username
            );

            window.localStorage.setItem("role", res.data.role);
            window.localStorage.setItem("id", res.data.id);
            if (res.data.role === "Fan") {
              window.localStorage.setItem("token", res.data.token);
              this.$router.push({ name: "user" });
            } else if (res.data.role === "Admin") {
              window.localStorage.setItem("token", res.data.token);
              this.$router.push({ name: "Console" });
            } else {
              if (res.data.status === 0) {
                // not pending
                window.localStorage.setItem("token", res.data.token);
                this.$router.push({ name: "Manager" });
              } else {
                this.$notify({
                  group: "login",
                  type: "warn",
                  title: "Account Activation",
                  text:
                    "Your account needs to be verified first then you can login ...",
                  duration: 3000,
                });
              }
            }
          })
          .catch((err) => {
            console.log(err);
            this.$notify({
              group: "login",
              type: "warn",
              title: "Username or Password is incorrect.",
              text: "Try again..",
              duration: 3000,
            });
          });
      }

      // todo send request to back to authenticate credentials and if user exist redirect to fan / manger / admin page
    },

    login_guest() {
      // redirect to guest page
      this.$router.push({ name: "guest" });
    },
    signup() {
      const myForm = $(".sign-up-form");

      if (!myForm[0].checkValidity()) {
        console.log(myForm[0].checkValidity());
        myForm[0].reportValidity();
      } else {
        if (this.register_data.pass1 != this.register_data.pass2) {
          this.$notify({
            group: "login",
            type: "warn",
            title: "Passwords doesnot match",
            text: "",
            duration: 3000,
          });
        } else {
          // request to create user if username is availabe
          axios
            .post(register, this.register_data)
            .then((res) => {
              console.log(res);
              if (this.register_data.role === "Fan") {
                window.localStorage.setItem(
                  "username",
                  this.register_data.username
                );
                this.$notify({
                  group: "login",
                  type: "success",
                  title: "Account Created..",
                  text: "Use your credentials to login in ...",
                  duration: 3000,
                });
              } else {
                // manger handle it to first approve than enter
                {
                  this.$notify({
                    group: "login",
                    type: "warn",
                    title: "Account Activation",
                    text:
                      "Your account needs to be verified first then you can login ...",
                    duration: 3000,
                  });
                }
              }
            })
            .catch((err) => {
              console.log(err);
              this.$notify({
                group: "login",
                type: "warn",
                title:
                  "Username " +
                  this.register_data.username +
                  " is not available.",
                text: "Try using another username",
                duration: 3000,
              });
            });
        }
      }
    },
    // showPassword() {
    //   if(this.type === 'password') {
    //     this.type = 'text'
    //     this.btnText = 'Hide Password'
    //   } else {
    //     this.type = 'password'
    //     this.btnText = 'Show Password'
    //   }
    // }
  },
};
</script>

<style scoped>
html,
body {
  color: #6a6f8c;
  font: 600 16px/18px "Open Sans", sans-serif;
  height: 100%;
}

.box {
  background: red;
  height: 100vh;
}

.row {
  background: url("../assets/homeImg.jpg") no-repeat center;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
  height: 1400px;
  max-width: 100%;
  margin: auto;
  background-position: relative;
}

.login-box {
  width: auto;
  margin: auto;
  max-width: 525px;
  min-height: 900px;
  position: relative;
  /* background: url(https://images.unsplash.com/photo-1507208773393-40d9fc670acf?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1268&q=80) no-repeat center; */
  /* box-shadow: 0 12px 15px 0 rgba(0, 0, 0, .24), 0 17px 50px 0 rgba(0, 0, 0, .19) */
}

.login-snip {
  width: 100%;
  height: 100%;
  position: absolute;
  padding: 90px 70px 50px 70px;
  /* background-image: url("../assets/homeImg.jpg"); */
  /* background: rgba(0, 77, 77, .9) */
}

.login-snip .login,
.login-snip .sign-up-form {
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  position: absolute;
  transform: rotateY(180deg);
  backface-visibility: hidden;
  transition: all 0.4s linear;
}

.login-snip .sign-in,
.login-snip .sign-up,
.login-space .group .check {
  display: none;
}

.login-snip .tab,
.login-space .group .label,
.login-space .group .button {
  text-transform: uppercase;
}

.login-snip .tab {
  font-size: 22px;
  margin-right: 15px;
  padding-bottom: 5px;
  margin: 0 15px 10px 0;
  display: inline-block;
  color: white;
  border-bottom: 2px solid transparent;
}

.login-snip .sign-in:checked + .tab,
.login-snip .sign-up:checked + .tab {
  color: #fff;
  border-color: #1161ee;
}

.login-space {
  min-height: 345px;
  position: relative;
  perspective: 1000px;
  transform-style: preserve-3d;
}

.login-space .group {
  margin-bottom: 15px;
}

.login-space .group .label,
.login-space .group .input,
.login-space .group .button {
  width: 100%;
  color: #fff;
  display: block;
  outline: none;
}

.form-control {
  border: none;
  border-radius: 25px;
  background: rgba(156, 158, 9, 0.6);
  color: #fff;
}

.login-space .group .input,
.login-space .group .button {
  border: none;
  padding: 15px 20px;
  border-radius: 25px;
  background: rgba(156, 158, 9, 0.6);
}

.login-space .group input[data-type="password"] {
  -webkit-text-security: circle;
}

.login-space .group .label {
  color: rgb(255, 255, 255);
  font-size: 12px;
}

.login-space .group .button {
  background: #1161ee;
}

.login-space .group label .icon {
  width: 15px;
  height: 15px;
  border-radius: 2px;
  position: relative;
  display: inline-block;
  background: rgba(255, 255, 255, 1);
}

.login-space .group label .icon:before,
.login-space .group label .icon:after {
  content: "";
  width: 10px;
  height: 2px;
  background: #fff;
  position: absolute;
  transition: all 0.2s ease-in-out 0s;
}

.login-space .group label .icon:before {
  left: 3px;
  width: 5px;
  bottom: 6px;
  transform: scale(0) rotate(0);
}

.login-space .group label .icon:after {
  top: 6px;
  right: 0;
  transform: scale(0) rotate(0);
}

.login-space .group .check:checked + label {
  color: #fff;
}

.login-space .group .check:checked + label .icon {
  background: #1161ee;
}

.login-space .group .check:checked + label .icon:before {
  transform: scale(1) rotate(45deg);
}

.login-space .group .check:checked + label .icon:after {
  transform: scale(1) rotate(-45deg);
}

.login-snip .sign-in:checked + .tab + .sign-up + .tab + .login-space .login {
  transform: rotate(0);
}

.login-snip .sign-up:checked + .tab + .login-space .sign-up-form {
  transform: rotate(0);
}

*,
:after,
:before {
  box-sizing: border-box;
}

.clearfix:after,
.clearfix:before {
  content: "";
  display: table;
}

.clearfix:after {
  clear: both;
  display: block;
}

a {
  color: inherit;
  text-decoration: none;
}

.hr {
  height: 2px;
  margin: 60px 0 50px 0;
  background: rgba(255, 255, 255, 0.2);
}

.foot {
  text-align: center;
}

.foot label {
  color: white;
}

.card {
  width: 500px;
  left: 100px;
}

::placeholder {
  color: #ffffff;
}
</style>
