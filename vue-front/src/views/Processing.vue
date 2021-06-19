<template>
  <v-container
    style="min-height: 600px; max-height:600px;"
    class="mt-16 my-main">
    <!-- 제목 -->
    <v-row
      justify='center'>
      <div>
      <h1 class="bold">
        Processing
      </h1>
      </div>
    </v-row>
    <v-row
      justify='center'
      class="mb-6">
      <hr
        class="mt-1"
        width="110px"
        size="1pt"
        color="black"
        text-align="center">
    </v-row>

    <!-- 스텝퍼 -->
    <v-stepper 
      v-model="recogStep"
      alt-labels
      class="mx-n1">
      <v-stepper-header
        class="px-5">
        <v-stepper-step
          :complete="recogStep > 1"
          step="1"
        >
          [Upload]
        </v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step
          :complete="recogStep > 2"
          step="2"
        >
          [Detection]
        </v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step 
          :complete="recogStep > 3"
          step="3">
          [Recognition]
        </v-stepper-step>

        <v-divider></v-divider>
        
        <v-stepper-step 
          :complete="recogStep > 4"
          step="4">
          [Show]
        </v-stepper-step>
      </v-stepper-header>
    </v-stepper>

    <!-- 카드이미지 -->
    <v-row
      justify="space-around"
      class="mt-1">
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
export default {
  name: 'Processing',
  data () {
    return {
      imageUrl: '',
      howToCards: [
        {
          step: 1,
          src: require("../img/page_converter/work_step1.png"),
          information: "Drag&Drop"
        },
        {
          step: 2,
          src: require("../img/page_converter/work_step2.png"),
          information: "YOLO"
        },
        {
          step: 3,
          src: require("../img/page_converter/work_step3.png"),
          information: "OCR"
        },
        {
          step: 4,
          src: require("../img/page_converter/work_step4.png"),
          information: "Output"
        },
      ],
    }
  },
  props: {
    recogStep: {
      type: Number,
    },
  },
}
</script>

<style>

</style>