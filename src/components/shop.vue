<template>
  <div>
    <div>
      <van-tabs v-model="tabsController" animated swipeable :sticky="true" color="#ff0036">
        <van-tab v-for="(shopId,idName) in shopList" :name="idName" :title="idName" :key="shopId">
          <van-list v-model="dataLoading[idName]" :finished="dataFinished[idName]" finished-text="没有更多了" @load="dataLoad(idName)">
            <van-cell v-for="data in dataRes[idName]" :key="data.goods_id"
            @click="$router.push('/cp/'+data.hd_thumb_url.replace(/\//g,'_')+'/'+data.goods_name+'/'+data.group_price)"
            >
              <van-row>
                <van-col span="8" style="min-width: 8.5rem;max-width: 8.5rem;">
                  <van-image width="8rem" height="6rem" :src="data.hd_thumb_url" />
                </van-col>
                <van-col span="14">
                  <div class="" style="vertical-align: middle;margin-bottom: 5px;">{{data.goods_name}}</div>
                  <div class="" style="">
                    <!-- {{data.short_name}} -->
                    <span>￥{{data.group_price / 100}}</span>
                    <span style="color: #cbcbcb;text-decoration: line-through;">
                      ￥{{data.market_price / 100}}
                    </span>
                    <!-- <span v-show="data.mblog.source!='' ">来自 {{data.mblog.source}}</span> -->
                  </div>
                </van-col>
              </van-row>
              <div v-html="data.title"></div>
            </van-cell>
          </van-list>
        </van-tab>

      </van-tabs>

    </div>

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
    name: 'shop',
    data() {
      return {
        tabsController: "当季女装",
        tabbarController: 2,
        dataLoading: {
          '当季女装': false,
          '热销鞋包': false,
          '品牌男装': false,
          '环球美食': false,
          '家具百货': false,
          '医药健康': false,
        },
        dataFinished: {
          '当季女装': false,
          '热销鞋包': false,
          '品牌男装': false,
          '环球美食': false,
          '家具百货': false,
          '医药健康': false,
        },
        dataRes: {},
        shopList: {
          '当季女装': '5571',
          '热销鞋包': '5572',
          '品牌男装': '5574',
          '环球美食': '5576',
          '家具百货': '5578',
          '医药健康': '22498',
        }
      }
    },
    beforeCreate() {
      // for (var x in this.shopList) {
      //   this.dataLoading[x] = false
      //   this.dataFinished[x] = false
      // }
    },
    methods: {
      dataLoad(idName) {
        this.$axios
          .get('../static/pinduoduo/' + this.shopList[idName] + '.json')
          .then(response => {
            this.dataRes[idName] = response.data.data
            this.dataFinished[idName] = true
          }, function(e) {
            console.log(e)
          })
      }
    },
  }
</script>

<style>
</style>
