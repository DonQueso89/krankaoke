<template>
  <div class="upload">
    <h1>Upload</h1>
    <b-form-row>
        <b-col>
            <KrankaokeForm/>
        </b-col>
    </b-form-row>
  </div>
</template>

<script>
// @ is an alias to /src
import KrankaokeForm from '@/components/KrankaokeForm.vue'

export default {
  name: 'upload',
  components: {
    KrankaokeForm
  }
}
</script>
<style scoped>
</style>
