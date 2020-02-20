<template>
  <div>

   <van-sticky >
         <van-nav-bar title="" left-text="返回"  @click-left="$router.go(-1)">
      </van-nav-bar>
    </van-sticky>

    <van-address-edit :area-list="areaList" show-postal show-delete show-set-default show-search-result :search-result="searchResult"
      :area-columns-placeholder="['请选择', '请选择', '请选择']" @save="onSave" @delete="onDelete" @change-detail="onChangeDetail" />
   <van-tabbar v-model="tabbarController">
      <van-tabbar-item icon="home-o" :to="{name:'home'}">首页</van-tabbar-item>
      <van-tabbar-item icon="video-o" :to="{name:'bilibili'}">视频</van-tabbar-item>
      <van-tabbar-item icon="friends-o" :to="{name:'shop'}">商城</van-tabbar-item>
      <van-tabbar-item icon="contact" :to="{name:'my'}">我的</van-tabbar-item>
    </van-tabbar>
  </div>
</template>

<script>
  export default {
    name: 'address2',
    data() {
      return {
        areaList: this.$area.areaList,
        searchResult: []
      };
    },

    methods: {
      onSave() {
        Toast('save');
      },
      onDelete() {
        Toast('delete');
      },
      onChangeDetail(val) {
        this.searchResult = [];
      }
    }
  }
</script>

<style>
</style>
