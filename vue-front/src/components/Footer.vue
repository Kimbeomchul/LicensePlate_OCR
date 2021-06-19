<template>
  <v-footer
    color="thema"
    padless
  >
    <v-row
      align-content="center"
      justify="space-between"
      class="mx-auto"
      no-gutters
      style="max-width: 1200px"
    >
      <!-- <v-btn
        v-for="link in links"
        :key="link"
        color="white"
        text
        rounded
        class="my-2"
      >
        {{ link }}
      </v-btn> -->
      <v-col
        class="ml-7 lighten-2 py-4 text-start white--text"
        md="7"
      >
        <div>
        COPYRIGHT© 2020 KINDERGARTEN_AI. ALL RIGHT RESERVED.<br>
        찾아오시는 길: 06367 서울시 강남구 광평로 280 로즈데일 빌딩 6층
        </div>
      </v-col>
      <v-col
        class="py-3"
        align-self="end"
        cols="4"
        >
        <v-img
          class="ml-auto mr-2 mb-1"
          width="300px"
          contain
          src="../img/page_main/logo_DBCS.png"
          alt="대보 로고"
        >
        </v-img>
      </v-col>

      
    </v-row>
  </v-footer>
</template>

<script>
export default {
  name: "footer-vue"
}
</script>

<style>

</style>