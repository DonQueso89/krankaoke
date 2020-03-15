<template>
<b-row class="krankaoke-item">
    <b-col>
        <h3>{{ krankaoke.artist }}</h3>
    </b-col>
    <b-col>
        <h3>{{ krankaoke.title }}</h3>
    </b-col>
    <b-col>
        <audio
                preload="metadata"
                controls
                :src="krankaoke.audio"
                crossorigin=anonymous>
                    Your browser does not support the
                    <code>audio</code> element.
        </audio>
    </b-col>
</b-row>
</template>
<script>
export default {
    name: "Krankaoke",
    props: ["krankaoke"]
}
</script>
<style scoped>
    .krankaoke-item {
        border: 5px;
    }
</style>
