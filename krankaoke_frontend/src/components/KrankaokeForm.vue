<template>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show" enctype="multipart/form-data">
      <b-form-group
        id="input-group-1"
        label="Artist"
        label-for="input-1"
      >
        <b-form-input :state="errors.artist ? false : null"
          id="input-1"
          v-model="form.artist"
          required
          placeholder="Enter artist"
        ></b-form-input>
        <b-form-invalid-feedback :state="errors.artist ? false : null">
            {{ errors.artist ? errors.artist[0] : "" }}
        </b-form-invalid-feedback>
      </b-form-group>
      <b-form-group
        id="input-group-2"
        label="Title"
        label-for="input-2"
      >
        <b-form-input
          id="input-2"
          v-model="form.title"
          required
          placeholder="Enter title"
          :state="errors.title ? false : null"
        ></b-form-input>
        <b-form-invalid-feedback :state="errors.title ? false : null">
            {{ errors.title ? errors.title[0] : "" }}
        </b-form-invalid-feedback>
      </b-form-group>
      <b-form-group
          label="Audio file (mp3)"
          label-for="audio-file"
          :state="false"
      >
    <b-form-file id="audio-file" :state="errors.audio ? false : null" accept=".mp3" v-model="form.audio" class="mt-3" plain></b-form-file>
    <b-form-invalid-feedback :state="errors.audio ? false : null">
        {{ errors.audio ? errors.audio[0] : "" }}
    </b-form-invalid-feedback>
    </b-form-group>
      <b-button type="submit" variant="success">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
</template>
<script>
import api from '@/api.js';

export default {
    name: "KrankaokeForm",
    data() {
        return {
            form: {
                artist: '',
                title: '',
                audio: null,
                user: api.userId
            },
            show: true,
            errors: []
        }
    },
    methods: {
        onSubmit(e) {
            e.preventDefault();
            api.createKrankaoke(this.form).then(
                () => this.$router.push("list")
            ).catch(err => this.errors = err.response.data)
        },
        onReset(e) {
            e.preventDefault();
            this.form.artist = '';
            this.form.title = '';
            this.form.audio = null;
            // Trick to reset/clear native browser form validation state
            this.show = false
            this.$nextTick(() => {
                this.show = true
            })
        }
    }
}
</script>
<style scoped>
</style>
