<template>
  <div>
    <van-sticky>
      <van-nav-bar title="评论" left-text="返回" left-arrow @click-left="goBack" />
    </van-sticky>

    <van-list v-model="detailLoading" :finished="detailFinished" :error="detailError" error-text="暂无评论" @load="detailLoad">
      <van-cell v-for="data in detailRes" :key="data.id">

        <van-row>
          <van-col span="6" style="min-width: 3.5rem;max-width: 4rem;">
            <van-image round width="3.5rem" height="3.5rem" :src="data.user.profile_image_url" />
          </van-col>
          <van-col span="12">
            <div class="" style="vertical-align: middle;margin-bottom: 5px;">{{data.user.screen_name}}</div>
            <div class="" style="">
              {{data.created_at}}
              <span v-show="data.source!='' ">来自 {{data.source}}</span>
            </div>
          </van-col>
        </van-row>

        <div v-html="data.text"></div>
      </van-cell>
    </van-list>

  </div>
</template>

<script>
  export default {
    name: '',
    data() {
      return {
        mid: '',
        gid: '',
        detailError: false,
        detailLoading: false,
        detailFinished: false,
        detailRes: [],
      }
    },
    created() {
      this.mid = this.$route.params.mid
      this.gid = this.$route.params.gid
    },
    methods: {
      goBack() {
        this.$router.go(-1)
      },
      detailLoad() {
        this.$axios
          .get('../static/weibo/' + this.gid + '/detail/' + this.mid + '.json')
          .then(response => {
            try{
              this.detailRes = response.data.data.data
            }catch(e){
              this.detailError = true
            }
            this.detailFinished = true
          }, function(e) {
            console.log(e)
          })
      }
    }
  }
</script>

<style>
</style>
