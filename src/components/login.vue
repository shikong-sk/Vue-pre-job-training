<template>
  <div>
    <div>

      <van-sticky :offset-top="0">
        <van-nav-bar title="" left-text="返回" left-arrow @click-left="$router.go(-1)">
          <!-- <van-icon name="search" slot="right" /> -->
        </van-nav-bar>
      </van-sticky>

      <van-list v-model="loading" :finished="finished" finished-text="" @load="onLoad">
        <van-cell v-for="item in list" :key="item" :title="item" />

<van-sticky :offset-top="80">
        <van-cell-group>
          <van-field v-model="username" required clearable label="用户名" right-icon="question-o" placeholder="请输入用户名"
            @click-right-icon="$toast('question')" />

          <van-field v-model="password" type="password" label="密码" placeholder="请输入密码" required />
        </van-cell-group>

        <van-cell-group>
          <van-field v-model="sms" center clearable label="短信验证码" placeholder="请输入短信验证码">
            <van-button slot="button" size="small" type="primary">发送验证码</van-button>
          </van-field>
        </van-cell-group>
</van-sticky>
<van-sticky :offset-top="530">
 

 <van-button round color="linear-gradient(to right, #4bb0ff, #6149f6)" type="primary"  block to="home" >登录</van-button>
   <van-button round color="#ffffff " type="primary"  block to="home" size="small"></van-button>
        <van-button round color="linear-gradient(to right, #4bb0ff, #6149f6)" type="primary" block to="logon">注册</van-button>
</van-sticky>
        


      </van-list>
    </div>
<!--    <van-tabbar v-model="tabbarController">
      <van-tabbar-item icon="home-o" :to="{name:'home'}">首页</van-tabbar-item>
      <van-tabbar-item icon="video-o" :to="{name:'bilibili'}">视频</van-tabbar-item>
      <van-tabbar-item icon="friends-o" :to="{name:'shop'}">商城</van-tabbar-item>
      <van-tabbar-item icon="contact" :to="{name:'my'}">我的</van-tabbar-item>
    </van-tabbar> -->
  </div>
</template>
</div>
</template>

<script>
  export default {
    name: 'login',
    data() {
      return {
        tabbarController: 3,
        areaList: this.$area.areaList,
        searchResult: [],
        checked: true,
        list: [],
        loading: false,
        finished: true,
      }
    },
    methods: {
      onSave() {
        Toast('save');
      },
      onDelete() {
        Toast('delete');
      },

    }
  }
</script>

<style>
</style>
