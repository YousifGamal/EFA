import { createRouter } from "vue-router";
import Users from "../views/Users.vue";
import Pending from "../views/Pending.vue";

const routes = [
  {
    path: "/users",
    name: "Users",
    component: Users,
  },
  {
    path: "/pending",
    name: "Pending",
    component: Pending,
  },
];

const router = createRouter({
  routes,
});

export default router;