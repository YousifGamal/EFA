import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Manager from '../views/Manager.vue'
import Login from '../views/Login.vue'
import UpdateProfile from '../views/UpdateProfile.vue'
import Users from '../views/UsersView.vue'
import Pending from '../views/PendingView.vue'
import Tickets from '../views/TicketsView.vue'
import Console from '../views/ConsoleView.vue'
import User from '../views/User.vue'
import Guest from '../views/Guest.vue'
Vue.use(VueRouter)

const routes = [
  {
    path:'/',
    name:'Login',
    component:Login
  },
  {
    path: '/home',
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
    path: '/tickets', // lazem tt3dl
    name: 'Tickets',
    component: Tickets
  },
  {
    path: '/console/', // lazem tt3dl
    name: 'Console',
    component: Console,
    children: [
      {
        path: '/console/Users',
        name: 'Users',
        component: Users
      },
      {
        path: '/console/Pending',
        name: 'Pending',
        component: Pending
      }
    ]
  },
  {
    path:'/user',
    name:'user',
    component: User
  },
  {
    path:'/guest',
    name:'guest',
    component: Guest
  }
]

const router = new VueRouter({
  routes,mode: 'history'
})

export default router
