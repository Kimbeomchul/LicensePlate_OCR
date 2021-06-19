<template>
  <v-container
    style="min-height: 600px"
    class="my-main">
    <!-- about page -->
    <about
      id="about"></about>
    <v-spacer
      class="spacer"></v-spacer>
    <!-- converter page -->
    <convert
      id="convert"
      @submit-upload-data="uploadFile"
    ></convert>
    <!-- contact page -->
    <v-spacer
      class="spacer"></v-spacer>
    <contact
      id="contact"></contact>
    <real-time-btn
      id='realtime'></real-time-btn>
    <real-time></real-time>
  </v-container>
</template>

<script>
import About from './About.vue'
import Contact from './Contact.vue'
import Convert from './Convert.vue'
import RealTime from './RealTime.vue'
import RealTimeBtn from './RealTimeBtn.vue'

export default {
  name: 'Home',
  components: {
    About,
    Contact,
    Convert,
    RealTimeBtn,
    RealTime 
  },
    RealTimeethods: {
    uploadFile(selectedFile) {
      this.$emit('submit-upload-data', selectedFile)
    }
  }
}
</script>

<style scoped>
.spacer {
  height: 150px;
}
</style>
