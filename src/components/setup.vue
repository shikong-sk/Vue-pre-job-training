<template>
  <div>
    <div>

      <van-sticky :offset-top="0">
        <van-nav-bar title="设置" left-text="返回" @click-left="$router.go(-1)" left-arrow="">
          <!-- <van-icon name="search" slot="right" /> -->
        </van-nav-bar>
      </van-sticky>

      <van-list v-model="loading" :finished="finished" finished-text="没有更多了" @load="onLoad">
        <van-cell v-for="item in list" :key="item" :title="item" />



        <van-cell-group title="账号">



          <van-cell is-link @click="showPopup">账号安全中心</van-cell>
          <van-cell title="地区设置" is-link value="中国大陆" />



          <van-cell title="使用Touch ID登录">
            <van-switch v-model="checked" />
          </van-cell>

        </van-cell-group>


        <van-cell-group title="播放">
          <van-cell title="跳过片头片尾">
            <van-switch v-model="checked" />
          </van-cell>
          <van-cell title="连续播放">
            <van-switch v-model="checked" />
          </van-cell>
        </van-cell-group>



        <van-cell-group title="缓存">
          <van-cell title="允许非WiFi下缓存">
            <van-switch v-model="checked" />
          </van-cell>
          <van-cell is-link @click="showPopup">缓存文件路径选择</van-cell>
          <van-cell title="默认缓存清晰度" is-link value="超清" />
          <van-cell title="同时缓存个数" is-link value="1个" />
          <van-cell title="缓存完成提示音">
            <van-switch v-model="checked" />
          </van-cell>
        </van-cell-group>



        <van-cell-group title="其他">
          <van-cell is-link @click="showPopup">隐私</van-cell>

          <van-cell is-link @click="showPopup">版本号</van-cell>

        </van-cell-group>




        <van-button color="linear-gradient(to right, #4bb0ff, #6149f6)" to="login">
          退出登录</van-button>
      </van-list>
    </div>
    <van-tabbar v-model="tabbarController">
      <van-tabbar-item icon="home-o" :to="{name:'home'}">首页</van-tabbar-item>
      <van-tabbar-item icon="video-o" :to="{name:'bilibili'}">视频</van-tabbar-item>
      <van-tabbar-item icon="friends-o" :to="{name:'shop'}">商城</van-tabbar-item>
      <van-tabbar-item icon="contact" :to="{name:'my'}">我的</van-tabbar-item>
    </van-tabbar>
  </div>
</template>
</div>
</template>

<script>
  export default {
    name: 'setup',
    data() {
      return {
        checked: true,
        tabbarController: 3,
        areaList: this.$area.areaList,
        searchResult: [],
        list: [],
        loading: false,
        finished: false,


      }
    },
    methods: {
      goBack() {
        this.$router.go(-1)
      },
      onSave() {
        Toast('save');
      },
      onDelete() {
        Toast('delete');
      },
      onInput(checked) {
        Dialog.confirm({
          title: '提醒',
          message: '是否切换开关？'
        }).then(() => {
          this.checked = checked;
        });
      }
    }
  }
</script>

<style>
</style>
