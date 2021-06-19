<template>
  <v-container
    style="min-height: 600px; max-height:600px;"
    class="mt-16 my-main">
    <v-row
      justify='center'>
      <div>
      <h1 class="bold">
        Contact Us
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
    
    <v-row
      justify="space-around"
      >
      <v-col
        cols="3"
        v-for="member in member_list"
        :key="member.title"
        class="px-3">
        <v-card   
          flat
        >
          <v-container>
            <v-row
              class="mb-5 px-5">
            
              <v-img
                contain
                :src="member.src"
                
              ></v-img>
            </v-row>
            <v-row
              class="px-5"
              justify="space-between">
              <v-col
                cols="4"
                class="px-0 py-1">
                <a :href="'mailto:' + member.mail_href"
                  target="_blank">
                  <v-img
                    contain
                    src="../img/page_contact/icon_mail.png"
                    
                  ></v-img>
                </a>
              </v-col>
              <v-col 
                cols="4"
                class="px-0 py-1">
                <a :href="'https://github.com/' + member.git_href"
                  target="_blank">
                  <v-img
                    contain
                    src="../img/page_contact/icon_github.png"
                  ></v-img>
                </a>
              </v-col>
              <v-col 
                cols="4"
                class="px-0 py-1">
                <a :href="'https://www.instagram.com/' + member.insta_href + '/'"
                  target="_blank">
                  <v-img
                    contain
                    src="../img/page_contact/icon_instagram.png"
                  ></v-img>
                </a>
              </v-col>
            </v-row>
            <v-card-title
              class="pb-0 mb-0">
              <div
                class="mx-auto">
                {{member.nm}}
              </div>
            </v-card-title>
            <v-card-text>
              <div
                class="mx-auto text-align-center">
                {{member.enm}}<br>
                {{member.information}}
              </div>
            </v-card-text>
            

          </v-container>
          
        </v-card>
      </v-col>
    </v-row>
    
  </v-container>
</template>

<script>
export default {
  name: "Contact",
  data () {
    return {
      member_list: [
        {
          title: "SHY",
          nm: "양승현",
          src:require("../img/page_contact/member_SeungHyeonYang.png"),
          mail_href: "seunghyeon.yang@dbcs.co.kr",
          git_href: "gabiiii",
          insta_href: "sh.gabriella",
          enm: "SeungHyeon Yang",
          information: "12기/전략기술팀",
        },
        {
          title: "BCK",
          nm: "김범철",
          src:require( '../img/page_contact/member_BeomChulKim.png'),
          mail_href: "beomchul.kim@dbcs.co.kr",
          git_href: "Kimbeomchul",
          insta_href: "m_ozz_i",
          enm: "BeomChul Kim",
          information: "12기/금융사업부",

        },
        {
          title: "DPH",
          nm: "홍두표",
          src:require('../img/page_contact/member_DuPyoHong.png'),
          mail_href: "dupyo.hong@dbcs.co.kr",
          git_href: "hdp0545",
          insta_href: "dupyo_91",
          enm: "DuPyo Hong",
          information: "12기/복지사업단",
        },
        {
          title: "KSB",
          nm: "배기성",
          src:require('../img/page_contact/member_KiSungBae.png'),
          mail_href: "kisung.bae@dbcs.co.kr",
          git_href: "",
          insta_href: "baeks0208",
          enm: "KiSung Bae",
          information: "12기/ABC사업부",
        }
      ],
    }
  },
  methods: {
    mail(member) {
      console.log(member)
      alert(`${member.nm}의 이메일은 ${member.mail_href}입니다.`)
    }
  }
}
</script>

<style>
.text-align-center {
  text-align: center;
}
.bold {
  font-family: 나눔스퀘어_ac Bold !important;
  src: url(../font/NanumSquare_acB.ttf);
}
</style>