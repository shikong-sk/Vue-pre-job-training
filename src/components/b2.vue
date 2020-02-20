<template>
  <div>
    <van-sticky>
      <van-nav-bar title="视频" left-text="返回" left-arrow @click-left="goBack" />
    </van-sticky>

    <van-list v-model="b2loading" :finished="b2finished" finished-text="没有更多了" @load="b2Load">
    </van-list>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        b2finished: false,
        b2loading: false,
        film: {}
      }
    },
    cretaed() {
      this.$axios()
    },
    methods: {
      goBack() {
        this.$router.go(-1)
      }
    }
  }
</script>

<style>
</style>
