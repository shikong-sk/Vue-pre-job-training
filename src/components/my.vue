<template>
  <div>

    <van-pull-refresh v-model="isLoading" @refresh="onRefresh">
      <div>

        <van-sticky :offset-top="0">
          <van-nav-bar title="个人中心" left-text=""  >
            <!-- <van-icon name="search" slot="right" /> -->
          </van-nav-bar>
        </van-sticky>


        <van-notice-bar color="#1989fa" background="#ecf9ff" left-icon="volume">

          60+ 高质量组件
          90% 单元测试覆盖率
          完善的中英文文档和示例
          支持按需引入
          支持主题定制
          支持国际化
          支持 TS
          支持 SSR

        </van-notice-bar>

        <van-list v-model="loading" :finished="finished" finished-text="没有更多了" @load="onLoad">
          <van-cell v-for="item in list" :key="item" :title="item" />




          <van-row type="flex" justify="space-around">
            <van-col span="6"></van-col>
            <van-col span="6">
              <van-uploader :before-read="beforeRead">
                <van-image round width="5rem" height="5rem" src="../static/img/logo.png">
                </van-image>
              </van-uploader>

            </van-col>
            <van-col span="6">
              <van-icon name="chat-o" dot />
            </van-col>
          </van-row>





          <van-row type="flex" justify="center">
            <van-col span="0" offset="0">作死中队</van-col>
          </van-row>

          <van-divider :style="{ color: '#1989fa', borderColor: '#1989fa', padding: '0 16px' }">
          </van-divider>



          <van-row type="flex">
            <van-col span="6">历史记录</van-col>
            <van-col span="6"></van-col>
            <van-col span="6"></van-col>
          </van-row>

          <van-swipe :autoplay="3000" indicator-color="blue">
            <van-swipe-item>
              <van-image width="100" height="100" src="https://img.yzcdn.cn/vant/cat.jpeg" />
            </van-swipe-item>
            <van-swipe-item>
              <van-image width="100" height="100" src="https://img.yzcdn.cn/vant/cat.jpeg" />
            </van-swipe-item>
            <van-swipe-item>
              <van-image width="100" height="100" src="https://img.yzcdn.cn/vant/cat.jpeg" />
            </van-swipe-item>
            <van-swipe-item>
              <van-image width="100" height="100" src="https://img.yzcdn.cn/vant/cat.jpeg" />
            </van-swipe-item>

          </van-swipe>


          <van-cell value="更多" is-link to="setup">
            <!-- 使用 title 插槽来自定义标题 -->
            <template slot="title">
              <span class="custom-title" link-type="navigateTo" url="setup">设置</span>
            </template>
          </van-cell>


          <van-cell value="" is-link to="address">
            <!-- 使用 title 插槽来自定义标题 -->
            <template slot="title">
              <span class="custom-title" link-type="navigateTo" url="setup">我的收货地址</span>
            </template>
          </van-cell>



<van-grid>
  <van-grid-item icon="photo"  text="我的相册" />
  <van-grid-item icon="manager" text="我的故事" />
  <van-grid-item icon="like" text="我的赞" />
  <van-grid-item icon="friends" text="粉丝服务" />
  <van-grid-item icon="alipay" text="钱包" />
  <van-grid-item icon="invition" text="我的缓存" />
  <van-grid-item icon="weapp-nav" text="历史记录" />
  <van-grid-item icon="manager" text="客服中心" />
  
</van-grid>


        </van-list>

      </div>

      <van-tabbar v-model="tabbarController">
        <van-tabbar-item icon="home-o" :to="{name:'home'}">首页</van-tabbar-item>
        <van-tabbar-item icon="video-o" :to="{name:'bilibili'}">视频</van-tabbar-item>
        <van-tabbar-item icon="friends-o" :to="{name:'shop'}">商城</van-tabbar-item>
        <van-tabbar-item icon="contact" :to="{name:'my'}">我的</van-tabbar-item>
      </van-tabbar>
    </van-pull-refresh>
  </div>
</template>

<script>
  export default {
    name: 'my',
    data() {
      return {
        tabbarController: 3,
        list: [],
        loading: false,
        finished: false,
        count: 0,
        isLoading: false,
      };
    },

    computed: {
      cardType() {
        return this.chosenContactId !== null ? 'edit' : 'add';
      },

      currentContact() {
        const id = this.chosenContactId;
        return id !== null ? this.list.filter(item => item.id === id)[0] : {};
      }
    },

    methods: {
      onRefresh() {
        setTimeout(() => {
          this.$toast('刷新成功');
          this.isLoading = false;
          this.count++;
        }, 500);
      }
    },

    // 返回布尔值
    beforeRead(file) {
      if (file.type !== 'image/jpeg') {
        Toast('请上传 jpg 格式图片');
        return false;
      }

      return true;
    },

    // 返回 Promise
    asyncBeforeRead(file) {
      return new Promise((resolve, reject) => {
        if (file.type !== 'image/jpeg') {
          Toast('请上传 jpg 格式图片');
          reject();
        } else {
          resolve();
        }
      });
    }



  }
</script>

<style>
</style>
