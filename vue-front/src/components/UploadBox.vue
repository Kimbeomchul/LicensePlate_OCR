<template>
  <v-container>
    <div
      class="uploadBox"  @drop.prevent="addFile" @dragover.prevent>
      <div v-if="selectedFile" class="progress">
        <v-progress-linear
          color="light-blue"
          height="10"
          :value="progress"
          striped
        > {{ progress }}% </v-progress-linear>
      </div>
      <div class="my-auto upload-word">Choose File <br> OR <br> Drag & Drop Files Here</div>
    </div>
  </v-container>
</template>

<script>

export default {
  name: "upload-box",
  data() {
    return {
      selectedFile: undefined,
      // imageUrl: "",
      

   
      
      // fileInfos: [],
      // rules: [
      //   value => !value || value.size < 2000000 || 'Picture size should be less than 2 MB!',
      // ],
    }
  },
  methods: {
    fileUpload() {
      if (!this.selectedFile) {
        this.message = "Please select a file!";
        return;
      }
      this.message = ""
      this.$emit('submit-upload-data', this.selectedFile)
      this.selectedFile = undefined
      this.$router.push('/processing')
    },
    addFile(e) {
      console.log("드래그 앤 드랍으로 파일 업로드를 시도합니다.")
      this.selectedFile = e.dataTransfer.files[0]
      console.log(this.selectedFile)
      this.fileUpload()
    }
  },
}

</script>

<style>
.uploadBox {
  background-color:rgb(132, 151, 176);
  width: 100%;
  height: 280px;
  border: dashed rgb(68, 114, 196);
  line-height: 1.5rem;
  margin: auto;
  text-align: center;
  align-content: center;
  color: white;
  display: block;
  position: relative;
}
.upload-word {
  position: relative;
  top: 90px;
}
.progress {
  position: absolute;
  width: 100%;
} 




</style>