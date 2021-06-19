<template>
  <v-container
    style="min-height: 672px"
    class="mt-16 my-main">
    <v-row
      justify='center'>
      <div>
      <h1 class="bold">
        Recognition
      </h1>
      </div>
    </v-row>  
    <v-row
      justify='center'>
      <hr
        class="mt-1"
        width="110px"
        size="1pt"
        color="black"
        text-align="center">
    </v-row>

    <v-row class="mt-6">
      <v-img :src="imageUrl"></v-img>
    </v-row>
    <v-row>
      <upload-box
        @submit-upload-data="uploadFile"
      ></upload-box>
    </v-row>
    <v-row
      justify="center"
      class="mt-8">
      <h2>
        <b>How to Use WALL·E Converter</b>
      </h2>
    </v-row>
    <v-row
      justify="space-around"
      class="mt-4">
      <v-col
        v-for="howToCard in howToCards"
        :key="howToCard.step"
        cols="3">
        <v-card
          class="mx-2"
          flat
          justify=center>
          <v-img
            :src="howToCard.src">
          </v-img>
          <v-card-text
            class="mt-n2 px-0">
            <pre><center>{{howToCard.information}}</center></pre>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import UploadBox from '../components/UploadBox.vue'
export default {
  name: "Convert",
  components: {
    UploadBox
  },
  data () {
    return {
      imageUrl: '',
      howToCards: [
        {
          step: 1,
          src: require("../img/page_converter/work_step1.png"),
          information: "[Upload] Drag&Drop\n번호판 이미지 업로드"
        },
        {
          step: 2,
          src: require("../img/page_converter/work_step2.png"),
          information: "[Detection] YOLO\n차량 번호판 탐지"
        },
        {
          step: 3,
          src: require("../img/page_converter/work_step3.png"),
          information: "[Recognition] OCR\n번호판 글씨 인식"
        },
        {
          step: 4,
          src: require("../img/page_converter/work_step4.png"),
          information: "[Show] Output\n인식한 차량번호 출력"
        },
      ],
    }
  },
  methods: {
    uploadFile(selectedFile) {
      this.$emit('submit-upload-data', selectedFile)
    }
  }
}
</script>

<style>
.bold {
  font-family: 나눔스퀘어_ac Bold !important;
  src: url(../font/NanumSquare_acB.ttf);
}
</style>