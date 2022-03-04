import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/branches",
      name: "branches",
      component: () => import("../views/BranchView.vue"),
    },
    {
      path: "/branchdetail",
      name: "branch_detail",
      component: () => import("../views/CommitView.vue"),
    },
    {
      path: "/pullrequest",
      name: "pullrequest",
      component: () => import("../views/PullRequestView.vue"),
    },
    {
      path: "/addpullrequest",
      name: "addpullrequest",
      component: () => import("../views/AboutView.vue"),
    },
    {
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/AboutView.vue"),
    },
  ],
});

export default router;
