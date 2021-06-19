<template>
  <v-app>
    <!-- background -->
    <v-img
      alt="Background Image"
      src='@/img/background.png'
      height='800px'
      gradient="to top, rgba(0,0,0,.4), rgba(0,0,0,.9)"
      background-position
      >
      <v-layout column align-center justify-center class="mt-n7 white--text" fill-height>
        <h1 class="white--text font-weight-bold display-2 mb-1 text-center">Kindergarten_AI</h1>
        <hr
          width="150px"
          class="my-4">
				<div class="subheading mb-4 text-center">인공지능을 이용한 차량 번호판 화질 개선 및 인식 프로젝트</div>
      </v-layout>
    </v-img>

    <!-- navigation bar -->
    <v-app-bar
      v-scroll="onScroll"
      color="white"
      light
      flat
      :fixed="fixed"
      :class="bosang"
    > 
      <v-container
        class="mx-auto"
        style="min-width: 1000px">
        <v-row
          justify="space-between">
          <v-col>
            <a href="/">
              <div class="d-flex-inline mb-n20 align-start">
                <v-img
                  alt="Wall-E Logo"
                  class="shrink mr-2 mt-2"
                  contain
                  src="./img/page_main/logo_horizontal.png"
                  transition="scale-transition"
                  width="250px"
                />
              </div>
            </a>
          </v-col>
          <v-col
            class="mt-3">
            <v-tabs
              lights
              optional
              right
              >
              <v-tab
                text
                @click="$vuetify.goTo(0, {duration: 500,
                                                offset: 0,
                                                easing: 'easeInOutCubic'})"
              >
                <span class="mr-2">Home</span>
              </v-tab>
              <v-tab
                text
                @click="$vuetify.goTo('#about', {duration: 500,
                                                offset: 100,
                                                easing: 'easeInOutCubic'})"
              >
                <span class="mr-2">About Program</span>
              </v-tab>
              <v-tab
                text
                @click="$vuetify.goTo('#convert', {duration: 500,
                                                offset: 100,
                                                easing: 'easeInOutCubic'})"
              >
                <span class="mr-2">Converter</span>
              </v-tab>
              <v-tab
                text
                @click="$vuetify.goTo('#contact', {duration: 500,
                                                offset: 100,
                                                easing: 'easeInOutCubic'})"
              >
                <span class="mr-2">Contact</span>
              </v-tab>
            </v-tabs>
          </v-col>
        </v-row>
      </v-container>
    </v-app-bar>

    <!-- fixed margin for navbar -->
    <div
      v-if="this.fixed"
      class="pt-11"></div>
    
    <!-- main contents -->
    <v-main>
      <router-view
        @submit-upload-data="uploadFile"
        :recog-step="this.recogStep"
        :ocr-text="this.ocrText"
        :yolo-result="this.yoloResult"
      ></router-view>
    </v-main>

    <!-- footer bar -->
    <footer-vue/>
  </v-app>
</template>

<script>
import footerVue from '@/components/Footer.vue'
import axios from 'axios'
import UploadService from "@/services/UploadFilesService";


// const SERVER_URL = 'http://34.64.197.76/api'
const SERVER_URL = 'http://127.0.0.1:8000'
export default {
  name: 'App',

  components: {
    footerVue,
  },

  data: () => ({
    // 업로드 파일 관련
    progress: 0,
    message: "",

    // processing 관련
    recogStep: 1,
  
    fixed: false,
    offsetTop: 0,
    bosang: "",
    
    // Yolo 결과
    yoloResult: {
      'detectPath': "",
      'platePath' : ""
    },

    // Ocr결과
    ocrText: ""
  }),
  methods: {
    uploadFile(selectedFile) {
      this.progress = 0
      this.recogStep = 1
      this.message = ""
      this.detectPath = ""
      this.platePath = ""
      this.ocrText = ""
      
      console.log(selectedFile)
      UploadService.upload(selectedFile, (event) => {
        this.progress = Math.round((100 * event.loaded) / event.total);
      })
        .then((response) => {
          this.message = response.data.message;
          console.log(response)
          console.log(this.message)
          this.recogStep = 2
          this.startYolo(response.data.name)
          this.progress = 0
        }).catch((err) => {
          console.log(err)
          this.progress = 0;
          this.message = "Could not upload the file!";
          console.log(this.message)
        });
    },
    onScroll () {
      if (window.scrollY >= 800) {
        this.bosang = "pb-16"
        this.fixed = true
      } else if (window.scrollY <= 736) {
        this.bosang = ""
        this.fixed = false
      }
    },
    startYolo(filename) {
      axios.get(`${SERVER_URL}/img/recognition/`+filename)
      .then((response) => {
        console.log(response)
        this.yoloResult.detectPath = response.data.detect
        this.yoloResult.platePath = response.data.plate
        console.log(this.yoloResult)
        this.recogStep = 3
        this.startOcr(filename.replace('.jpg', 'plate.jpg'))
      })
    },
    startOcr(plate) {
      axios.get(`${SERVER_URL}/img/ocr/` + plate)
      .then((response) => {
        this.recogStep = 4
        console.log(response)
        this.ocrText = response.data.ocr_text
        this.$router.push('/afterRecognition')
      })
    }
  }
};
</script>
<style scoped>
.my-main {
  max-width: 900px;
}
.bold {
  font-family: 나눔스퀘어_ac Bold !important;
  src: url(./font/NanumSquare_acB.ttf);
}
.v-application{
  /* font-family: 나눔스퀘어_ac; */
  /* src: url(./font/NanumSquare_acR.ttf); */
  font-family: D2Coding;
  src: url(./font/D2Coding-Ver1.3.2-20180524.ttf);
}


</style>


