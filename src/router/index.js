import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Manager from '../views/Manager.vue'
import Login from '../views/Login.vue'
import UpdateProfile from '../views/UpdateProfile.vue'
import User from '../views/User.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/manager',
    name: 'Manager',
    component: Manager
  },
  {
    path:'/login',
    name:'Login',
    component:Login
  },
  {
    path:'/update',
    name:'UpdateProfile',
    component:UpdateProfile
  },
  {
    path:'/user',
    name:'user',
    component: User
  }
]

const router = new VueRouter({
  routes,mode: 'history'
})

export default router
