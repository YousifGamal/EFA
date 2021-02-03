import Vue from 'vue'
import VueRouter from 'vue-router'
import Users from '../../views/UsersView.vue'
import Pending from '../../views/PendingView.vue'
import Tickets from '../../views/TicketsView.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/console/Users',
    name: 'Users',
    component: Users
  },
  {
    path: '/console/Pending',
    name: 'Pending',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: Pending//() => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/tickets', // lazem tt3dl
    name: 'Tickets',
    component: Tickets
  }
]

const router = new VueRouter({
  routes
})

export default router
