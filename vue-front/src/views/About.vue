<template>
  <v-container
    style="min-height: 672px"
    class="mt-16 my-main">
    <v-row
      justify='center'>
      <div>
      <h1 class="bold">
        About Program
      </h1>
      </div>
    </v-row>
     <v-row
      justify='center'
      class="mb-8">
      <hr
        class="mt-1"
        width="110px"
        size="1pt"
        color="black"
        text-align="center">
    </v-row>
    
    <v-row
      justify="center">
      <div
        class="align-center px-10">
        WALL·E Convert는 사용자가 가지고 있는 저화질 차량 이미지를 고화질로 변환하고,<br>
        변환된 이미지 내 차량 번호판 글자를 출력하는 서비스입니다.<br>
        AI(인공지능) 기반인 이미지 처리와 글자 인식 기술을 통해 제작한 서비스는 사용자의 기술적 이해를 필요로 하지 않습니다.<br>
        사용자는 Drag&Drop 한번으로 WALL·E Convert 서비스를 손쉽게 이용할 수 있습니다.<br>
        사고 처리 및 신고를 위해 차량 번호가 필요한 경우 WALL·E Convert를 유용하게 활용할 수 있습니다.
      </div>
    </v-row>
    <v-row
      justify="space-around"
      class="mt-16">
      <v-col
        lg='4'>
        <v-card
          class="px-5"
          flat
          justify=center>
          <v-img
            height="100px"
            contain
            src="../img/page_about/repair.png"
          ></v-img>
          <v-card-title>
            <h3 class="mx-auto mt-5 bold">"GAN Algorithm"</h3>
          </v-card-title>
          <v-card-text
            class="mt-2">
            GAN은 진짜와 같은 데이터를 만들어내는 기술입니다. 저화질 이미지 데이터를 고화질 이미지 데이터로 변환하기 위해 사용하였습니다.
          </v-card-text>
        </v-card>
      </v-col>
      <v-col
        lg='4'>
        <v-card
          class="px-5"
          flat
          justify=center>
          <v-img
            height="100px"
            contain
            src="../img/page_about/evaluation.png"
          ></v-img>
          <v-card-title>
            <h3 class="mx-auto mt-5 bold">"YOLO Algorithm"</h3>
          </v-card-title>
          <v-card-text
            class="mt-2">
            YOLO는 이미지 내 특정 물체를 탐지하는 기술입니다. 이미지에 존재하는 차량 번호판을 탐지하고 번호판 이미지를 추출하려 사용하였습니다.
          </v-card-text>
        </v-card>
      </v-col>
      <v-col
        lg='4'>
        <v-card
          class="px-5"
          flat
          justify=center>
          <v-img
            height="100px"
            contain
            src="../img/page_about/transformation.png"
          ></v-img>
          <v-card-title>
            <h3 class="mx-auto mt-5 bold">"OCR Algorithm"</h3>
          </v-card-title>
          <v-card-text
            class="mt-2">
            OCR은 이미지 내 글자를 인식하여 추출하는 기술입니다. 차량 번호판 이미지의 글자를 텍스트 형식으로 반환하기 위해 사용하였습니다.
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {

}
</script>

<style scoped>
.align-center {
  text-align: center;
}
.bold {
  font-family: 나눔스퀘어_ac Bold !important;
  src: url(../font/NanumSquare_acB.ttf);
}
</style>

