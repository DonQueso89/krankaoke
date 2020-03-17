<template>
    <b-row>
        <b-col class="col-12">
            <h1>Record</h1>
            <Krankaoke :krankaoke="krankaoke"/>
        </b-col>
        <b-col class="canvas-container">
            <canvas ref="oscilloscope" resize="true"></canvas>
        </b-col>
    </b-row>
</template>

<script>
import Krankaoke from "@/components/Krankaoke.vue"
import api from "@/api.js"

export default {
  name: 'KrankaokeRecorder',
  components: {
      Krankaoke
  },
  data() {
    return {
      paper: undefined,
      krankaoke: {},
      analyser: undefined,
    }
  },
  methods: { 
  visualiseSound: function() {
    // Execute this <= 60 times per sec
    /* eslint-disable no-console */
    let width = this.$refs.oscilloscope.width
    let height = this.$refs.oscilloscope.height
    var bufferLength = this.analyser.frequencyBinCount;
    var dataArray = new Uint8Array(bufferLength);

    let rect = new this.paper.Rectangle(0, 0, width, height);
    rect.fillColor = "black";
    var barWidth = (width / bufferLength) * 2.5;
    var barHeight;
    var x = 0;

    for(var i = 0; i < bufferLength; i++) {
        barHeight = dataArray[i]/2;

        this.paper.fillStyle = 'rgb(' + (barHeight+100) + ',50,50)';
        let rect = new this.paper.Rectangle(x,height-barHeight/2,barWidth,barHeight);
        rect.fillColor = "white";

        x += barWidth + 1;
    }
  }},
  mounted() {
    api.getKrankaoke(this.$route.params.id).then(v => { 
        this.krankaoke = v;
    });
    this.paper = this.$root.paper.setup(this.$refs.oscilloscope)

    
    this.$nextTick(function() {
        //  run this after all child components have also been mounted

        this.audioGraph = new AudioContext();
        let audio = document.querySelector("audio")
        let source = this.audioGraph.createMediaElementSource(audio);
        let analyser = this.audioGraph.createAnalyser()
        source.connect(analyser)
        analyser.connect(this.audioGraph.destination)
        analyser.fftSize = 256;  // coarse granularity for bar visualisation
        this.analyser = analyser;
        
        let playIt = function() {
            var visualiseIt = this.visualiseSound.bind(this)
            this.audioGraph.resume()
            this.paper.view.onFrame = () => visualiseIt()
        }.bind(this);
        audio.addEventListener("play", playIt)
    })
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
