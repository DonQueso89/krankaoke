import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import { BootstrapVue } from "bootstrap-vue";
import paper from "paper";

Vue.config.productionTip = false;
Vue.use(BootstrapVue);

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import api from "@/api.js";

api.initialize().then(() => {
  new Vue({
    router,
    render: h => h(App),
    created() {
      this.paper = paper;
    }
  }).$mount("#app");
});
