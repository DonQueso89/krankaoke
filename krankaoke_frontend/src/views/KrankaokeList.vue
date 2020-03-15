<template>
  <b-row>
    <b-col>
    <h3>Krankaokes</h3>
    <hr>
        <b-table striped hover :items="krankaokes" :fields="fields" dark class="mx-0 px-0">
            <template v-slot:cell(play_link)="data">
            <b-link :to='"/play/" + data.item.id'>Play</b-link>
            </template>
        </b-table>
    </b-col>
  </b-row>
</template>

<script>
// @ is an alias to /src
// import Krankaoke from '@/components/Krankaoke.vue';
import api from '@/api.js';


export default {
  name: "KrankaokeList",
  data() { 
    return {
        krankaokes: [],
        fields: ["artist", "title", "play_link"]
    }
  },
  mounted: function() {
      api.krankaokes().then(v => this.krankaokes = v);
  }
}
</script>

<style scoped>

</style>
