<template>
  <div class="home">
    <h1>Record</h1>
    <KrankaokeRecorder msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import KrankaokeRecorder from '@/components/KrankaokeRecorder.vue'

export default {
  name: 'home',
  components: {
    KrankaokeRecorder
  }
}
</script>
