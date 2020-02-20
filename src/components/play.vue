<template>
  <div>
    <van-sticky>
      <van-nav-bar title="视频播放" left-text="返回" left-arrow @click-left="$router.go(-1)">
        <!-- <van-icon name="search" slot="right" /> -->
      </van-nav-bar>
    </van-sticky>


    <van-row>
      <van-col span="24" style="">
        <van-image :src="'../static/bilibili/image/'+img" />
      </van-col>
      <van-col span="24">
        <div class="" style="">
          {{title}}
        </div>
        <div>
          {{author}}
          <span style="color: #cbcbcb;font-size: 0.875rem;display: inline-block;margin-left: 20px;">{{play}}次观看</span>
          <span style="color: #cbcbcb;font-size: 0.875rem;display: inline-block;">{{video_review}}弹幕</span>
        </div>
      </van-col>
    </van-row>


  </div>
</template>

<script>
  export default {
    name: 'play',
    data() {
      return {
        aid,
        img,
        play,
        video_review,
        title,
        author,
      }
    },
    created() {
      this.aid = this.$route.params.aid
      this.img = this.$route.params.img
      this.play = this.$route.params.play
      this.video_review = this.$route.params.video_review
      this.title = this.$route.params.title
      this.author = this.$route.params.author
    },
    methods: {

    }
  }
</script>

<style>
</style>
