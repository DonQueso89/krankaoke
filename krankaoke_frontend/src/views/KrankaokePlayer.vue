<template>
  <b-row>
    <b-col>
  
  <b-row>
    <b-col>
    <h3>KrankaokePlayer</h3>
    <Krankaoke :krankaoke="krankaoke"/>
    </b-col>
  </b-row>
    <b-row>
        <b-col>
            <canvas ref="lyricsCanvas" resize="true"></canvas>
        </b-col>
    </b-row>
    </b-col>
  </b-row>
</template>

<script>
import api from '@/api.js';
import Krankaoke from "@/components/Krankaoke.vue"


export default {
  name: "KrankaokePlayer",
  components: {
      Krankaoke
  },
  data() { 
    return {
        krankaoke: {},
        canvasCtx: undefined
    }
  },
  mounted: function() {
      api.getKrankaoke(this.$route.params.id).then(v => { 
          // Provisional test data
          v.timings = [
            ["hello", 1000, 2000],
            ["world", 2001, 3500],
            ["what", 4000, 10000],
            ["is", 10001, 20000],
            ["up?????", 20001, 50000]
          ]; 
          this.krankaoke = v;
      });
    this.$nextTick(function() {
      //  run this after all child components have also been mounted
        // Assume that created re-initialises when page is reloaded

        this.audioGraph = new AudioContext();
        let audio = document.querySelector("audio")
        let source = this.audioGraph.createMediaElementSource(audio);
        let analyser = this.audioGraph.createAnalyser()
        source.connect(analyser)
        analyser.connect(this.audioGraph.destination)
        
        this.canvas = this.$refs.lyricsCanvas;
        this.canvasCtx = this.$refs.lyricsCanvas.getContext("2d");
        this.canvasCtx.font = "30px Serif";
        this.canvasCtx.fillStyle = "white";
        this.canvasCtx.textAlign = "left";
        
        let playIt = function() {
            this.audioGraph.resume()
            this.playKrankaoke()
        }.bind(this);
        audio.addEventListener("play", playIt)
    })
  },
  methods: {
    clearCanvas() {
        let ctx = this.canvasCtx;
        ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height)
    },
    wordFits(ctx, x, wordLength) {
        return x + wordLength <= ctx.canvas.width;
    },
    displaySentence(sentence) {
        this.clearCanvas();
        sentence.map(word => {
            this.canvasCtx.fillStyle = "white";
            if (word.highlighted) {
                this.canvasCtx.fillStyle = "yellow";
            }
            this.canvasCtx.fillText(word.word, word.x, word.y)
        })
    },
    playKrankaoke() {
        /*ctx:: CanvasContext, wordTuples:: three-tupls of word-start-end*/
        // TODO: Display words in response to events fired from AudioContext
        const whiteSpace = 5;
        
        let ctx = this.canvasCtx
        let wordTuples = this.krankaoke.timings.sort((a, b) => {
            a[1] < b[1] ? -1 : a[1] > b[1] ? 1 : alert("Corrupt krankaoke timings")
        })
         
        var i = 0;
        var y = ctx.canvas.height / 2;
        while (i < wordTuples.length) {
            var x = 0; 
            let nextSentence = [];

            while (i < wordTuples.length) {
                let nextWord = wordTuples[i][0];
                let wordLength = ctx.measureText(nextWord).width;

                if (this.wordFits(ctx, x, wordLength)) {
                    let wordDef = Object.fromEntries(wordTuples[i].map((a, i) => [["word", "start", "end"][i], a]));
                    wordDef.x = x;  // add location
                    wordDef.y = y;  // add location
                    nextSentence.push(wordDef)
                    x += wordLength
                    x += whiteSpace
                    i++;
                } else { break; }
            }

            this.displaySentence(nextSentence);
            
            nextSentence.map((word, idx) => {
                var sentenceSnapshot = JSON.parse(JSON.stringify(nextSentence))
                sentenceSnapshot[idx].highlighted = true
                // highlight the word when it starts
                window.setTimeout(() => this.displaySentence(sentenceSnapshot), word.start) 
                // unhighlight word when it ends
                window.setTimeout(() => this.displaySentence(nextSentence), word.end) 
            })
        }
        
    },
  }
}
</script>

<style scoped>
html,
body {
    height: 100%;
}

/* Scale canvas with resize attribute to full size */
canvas[resize] {
    width: 100%;
    height: 100%;
    background-color: black; 
}
</style>
