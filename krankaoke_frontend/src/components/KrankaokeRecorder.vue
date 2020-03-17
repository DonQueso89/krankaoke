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
        this.paper.project.activeLayer.removeChildren()
        let width = this.$refs.oscilloscope.width
        let height = this.$refs.oscilloscope.height
        var bufferLength = this.analyser.frequencyBinCount;
        var dataArray = new Uint8Array(bufferLength);

        var barWidth = (width / bufferLength) * 2.5;
        var barHeight;
        var x = 0;

        for(var i = 0; i < bufferLength; i++) {
            this.analyser.getByteFrequencyData(dataArray);
            barHeight = dataArray[i] ** 1.2;

            let rect = new this.paper.Path.Rectangle(x,height-barHeight/2,barWidth,barHeight);
            rect.strokeColor = "white";
            rect.fillColor = 'rgb(' + (barHeight+100) + ',50,50)';

            x += barWidth + 1;
        }
  }},
  mounted() {
    api.getKrankaoke(this.$route.params.id).then(v => { 
        this.krankaoke = v;
    });
    this.paper = this.$root.paper.setup(this.$refs.oscilloscope);
    window.paperr = this.paper;

    
    this.$nextTick(function() {
        //  run this after all child components have also been mounted

        this.audioGraph = new (window.AudioContext || window.webkitAudioContext)();
        let audio = document.querySelector("audio")
        let source = this.audioGraph.createMediaElementSource(audio);
        let analyser = this.audioGraph.createAnalyser()
        source.connect(analyser)
        analyser.connect(this.audioGraph.destination)
        analyser.fftSize = 256;  // coarse granularity for bar visualisation
        this.analyser = analyser;

        
        let playIt = function() {
            this.audioGraph.resume()
            this.paper.view.onFrame = this.visualiseSound
        }.bind(this);

        let pauseIt = function() {
            this.audioGraph.suspend()
            this.paper.view.pause()
        }.bind(this);
        audio.addEventListener("play", playIt)
        audio.addEventListener("pause", pauseIt)
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
}

.canvas-container { 
    background-color: black; 
    border-radius: 5px; 
}

</style>
