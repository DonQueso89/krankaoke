import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import KrankaokeList from "../views/KrankaokeList.vue";
import KrankaokeCreate from "@/views/KrankaokeCreate.vue";
import KrankaokePlayer from "@/views/KrankaokePlayer.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "record",
    component: Home
  },
  {
    path: "/upload",
    name: "upload",
    component: KrankaokeCreate
  },
  {
    path: "/list",
    name: "list",
    component: KrankaokeList
  },
  {
    path: "/play/:id",
    name: "play",
    component: KrankaokePlayer
  }
];

const router = new VueRouter({
  routes
});

export default router;
