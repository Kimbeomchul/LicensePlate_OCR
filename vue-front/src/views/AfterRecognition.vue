<template>
  <v-container
    style="min-height: 672px"
    class="mt-16 my-main">
    
    <v-row
      class="mx-0 outline">
      <v-col
        cols="8"
        class="px-2 py-2">
        <h3>Recognized Image</h3>
        <v-img
          class="imgbox"
          :src="yoloResult.detectPath"></v-img>
      </v-col>
      <v-col
        cols="4"
        class="pr-2 py-2">
        <h3>Plate Image</h3>
        <v-img
          class="imgbox mb-2"
          :src="yoloResult.platePath"></v-img>
        <h3>Result</h3>
        <div
          class="resultBox">
          <h2>"{{ this.ocrText }}"</h2>
        </div>
      </v-col>
    </v-row>
    <v-row></v-row>
  
  </v-container>
</template>

<script>
export default {
  name: "AfterRecognition",
  data () {
    return {
    }
  },
  props: {
    yoloResult: {
      type: Object
    },
    ocrText: {
      type: String
    }
  }
}
</script>

<style>
.outline {
  background-color: rgb(245, 247, 249);
}
.imgbox {
  background-color: rgb(232, 235, 240);
}
.col {
  padding: 0;
}
.resultBox {
  background-color: white ;
  line-height: 248px;
  text-align: center;
}
</style>