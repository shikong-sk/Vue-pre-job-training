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
          
          <van-field v-model="password" type="password" label="密码" placeholder="再次确认密码" required />
          <van-field v-model="password" type="password" label="手机号" placeholder="注册手机号" required />
           
        </van-cell-group>

        <van-cell-group>
        
        </van-cell-group>
</van-sticky>

<van-sticky :offset-top="580">
        <van-button round color="linear-gradient(to right, #4bb0ff, #6149f6)" type="primary" block to="login">完成注册</van-button>

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
    name: 'logon',
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
