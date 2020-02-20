<template>
  <div>
    <van-sticky>
      <van-nav-bar title="商品详情" left-text="返回" left-arrow @click-left="$router.go(-1)">
      </van-nav-bar>
    </van-sticky>


    <van-row>
      <van-col span="24" style="">
        <van-image :src="img" />
      </van-col>
      <van-col span="24" style="background: #ff0036;text-align: left;">
        <span style="color: #fff;font-size: 20px;display: inline-block;margin-left: 20px;">￥{{group_price/100}}</span>
      </van-col>
      <van-col span="24">
        <div>
          <span style="color: #000;font-size: 0.875rem;display: inline-block;margin-left: 20px;">{{goods_name}}</span>
        </div>
      </van-col>
    </van-row>

    <van-goods-action>
      <van-goods-action-icon icon="chat-o" text="客服" @click="onClickIcon" />
      <van-goods-action-icon icon="cart-o" text="购物车" @click="onClickIcon" />
      <van-goods-action-button type="warning" text="加入购物车" @click="onClickButton" />
      <van-goods-action-button type="danger" text="立即购买" @click="onClickButton" />
    </van-goods-action>

    <van-sku v-model="show" :sku="sku" :goods="goods" :goods-id="goodsId" :quota="quota" :quota-used="quotaUsed"
      :hide-stock="sku.hide_stock" :message-config="messageConfig" @buy-clicked="onBuyClicked" @add-cart="onAddCartClicked" />

  </div>

</template>

<script>
  export default {
    name: 'cp',
    data() {
      return {
        goods_name: '',
        group_price: '',
        market_price: '',
        img: '',
        quota: 1,
        show: false,
        sku: {
          // 所有sku规格类目与其值的从属关系，比如商品有颜色和尺码两大类规格，颜色下面又有红色和蓝色两个规格值。
          // 可以理解为一个商品可以有多个规格类目，一个规格类目下可以有多个规格值。
          tree: [{
            k: '颜色', // skuKeyName：规格类目名称
            v: [{
                id: '30349', // skuValueId：规格值 id
                name: '默认', // skuValueName：规格值名称
                imgUrl: this.$route.params.img.replace(/_/g, '/'), // 规格类目图片，只有第一个规格类目可以定义图片
                previewImgUrl: this.$route.params.img.replace(/_/g, '/'), // 用于预览显示的规格类目图片
              },
            ],
            k_s: 's1' // skuKeyStr：sku 组合列表（下方 list）中当前类目对应的 key 值，value 值会是从属于当前类目的一个规格值 id
          }],
          // 所有 sku 的组合列表，比如红色、M 码为一个 sku 组合，红色、S 码为另一个组合
          list: [{
            id: 2259, // skuId，下单时后端需要
            price: 100, // 价格（单位分）
            s1: '1215', // 规格类目 k_s 为 s1 的对应规格值 id
            s2: '1193', // 规格类目 k_s 为 s2 的对应规格值 id
            s3: '0', // 最多包含3个规格值，为0表示不存在该规格
            stock_num: 110 // 当前 sku 组合对应的库存
          }],
          price: this.$route.params.group_price/100, // 默认价格（单位元）
          stock_num: 227, // 商品总库存
          collection_id: 2261, // 无规格商品 skuId 取 collection_id，否则取所选 sku 组合对应的 id
          none_sku: false, // 是否无规格商品
          messages: [{
            // 商品留言
            datetime: '0', // 留言类型为 time 时，是否含日期。'1' 表示包含
            multiple: '0', // 留言类型为 text 时，是否多行文本。'1' 表示多行
            name: '留言', // 留言名称
            type: 'text', // 留言类型，可选: id_no（身份证）, text, tel, date, time, email
            required: '1', // 是否必填 '1' 表示必填
            placeholder: '' // 可选值，占位文本
          }],
          hide_stock: false // 是否隐藏剩余库存
        },
        goods: {
          // 商品标题
          title: this.$route.params.goods_name,
          // 默认商品 sku 缩略图
          picture: this.$route.params.img.replace(/_/g, '/')
        },
        messageConfig: {
          // 数据结构见下方文档
        },
        goodsId: '1',
        quotaUsed: 1
      }
    },
    created() {
      this.img = this.$route.params.img.replace(/_/g, '/')
      this.goods_name = this.$route.params.goods_name
      this.group_price = this.$route.params.group_price
    },
    methods: {

      onBuyClicked() {
        this.show = true
      },
      onAddCartClicked() {
        this.show = true
      },
      onClickIcon() {
        this.show = true
      },
      onClickButton() {
        this.show = true
      }
    }
  }
</script>

<style>
</style>
