import Vue from "vue";
import VueRouter from "vue-router";
import KrankaokeList from "../views/KrankaokeList.vue";
import KrankaokeCreate from "@/views/KrankaokeCreate.vue";
import KrankaokePlayer from "@/views/KrankaokePlayer.vue";
import KrankaokeRecorder from "@/components/KrankaokeRecorder.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/record/:id",
    name: "record",
    component: KrankaokeRecorder
  },
  {
    path: "/upload",
    name: "upload",
    component: KrankaokeCreate
  },
  {
    path: "/",
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
