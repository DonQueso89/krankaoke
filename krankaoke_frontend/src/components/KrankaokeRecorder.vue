<template>
<b-container class='canvas-container'>
        <b-row>
            <b-col>
                <canvas ref="audioCanvas" resize="true"></canvas>
            </b-col>
        </b-row>
</b-container>
</template>

<script>
export default {
  name: 'KrankaokeRecorder',
  data() {
    return {
      paper: undefined
    }
  },
  mounted() {
    this.paper = this.$root.paper.setup(this.$refs.audioCanvas)
    var myCircle = new this.paper.Path.Circle(new this.paper.Point(100, 70), 50);
    myCircle.fillColor = 'yellow';
    this.paper.view.draw()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
html,
body {
    height: 100%;
}

/* Scale canvas with resize attribute to full size */
canvas[resize] {
    width: 100%;
    height: 100%;
    z-index: 100000;
}

.canvas-container { 
    background-color: black; 
    border-radius: 5px; 
}

h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
