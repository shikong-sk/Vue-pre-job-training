<template>
  <div>
    <van-sticky :offset-top="0">
      <van-nav-bar title="视频" left-text="" style="background-color: #F0F0F0;">
        <!-- <van-icon name="search" slot="right" /> -->
      </van-nav-bar>
    </van-sticky>

    <van-list v-model="dataLoading" :finished="dataFinished" finished-text="没有更多了" @load="dataLoad">
      <van-row>
        <!-- <van-cell v-for="data in dataRes" :key="data.aid"> -->
        <van-col span="12" style="height: 9.375rem;padding: 0 1px;margin-bottom: 1.5rem;" v-for="data in dataRes" :key="data.aid">
          <van-row @click="$router.push('/play/'+data.aid+'/'+data.pic.split('/')[data.pic.split('/').length-1]+'/'+data.play+'/'+data.video_review+'/'+data.title.replace(' ','')+'/'+data.author)">
            <van-col span="24" style="">
              <van-image radius="8" style="width: 11.6rem;height: 8.5rem;" :src="data.pic" />
            </van-col>
            <van-col span="24" style="height: 0.5rem;">

              <div style="font-size: 0.75rem;">{{data.title}}</div>

            </van-col>
          </van-row>

        </van-col>
        <!-- </van-cell> -->
      </van-row>
    </van-list>

    <van-tabbar v-model="tabbarController">
      <van-tabbar-item icon="home-o" :to="{name:'home'}">首页</van-tabbar-item>
      <van-tabbar-item icon="video-o" :to="{name:'bilibili'}">视频</van-tabbar-item>
      <van-tabbar-item icon="shopping-cart-o" :to="{name:'shop'}">商城</van-tabbar-item>
      <van-tabbar-item icon="contact" :to="{name:'my'}">我的</van-tabbar-item>
    </van-tabbar>
  </div>
</template>

<script>
  export default {
    name: 'bilibili',
    data() {
      return {
        tabbarController: 1,
        dataLoading: false,
        dataFinished: false,
        dataRes: ''
      }
    },
    methods: {
      dataLoad() {
        this.$axios
          .get('../static/bilibili/ranking.json')
          .then(response => {
            this.dataRes = response.data.data
            this.hotFinished = true
          }, function(e) {
            console.log(e)
          })
      }
    },
  }
</script>

<style>
</style>
