<template>
  <div>


    <van-sticky :offset-top="0">
      <van-nav-bar title="" left-text="返回" @click-left="$router.go(-1)">
        <van-icon name="search" slot="right" />
      </van-nav-bar>
    </van-sticky>


<form action="/">
  <van-search
    v-model="value"
    placeholder="请输入搜索关键词"
    show-action
    @search="onSearch"
    @cancel="onCancel"
  />
</form>

    <van-cell value="" is-link to="address">
      <!-- 使用 title 插槽来自定义标题 -->
      <template slot="title">
        <span class="custom-title" link-type="navigateTo" url="setup">我的收货地址</span>
      </template>
    </van-cell>


    <van-address-list v-model="chosenAddressId" :list="list" :disabled-list="disabledList" default-tag-text="默认" @add="onAdd"
      @edit="onEdit" />


  </div>
</template>

<script>
  export default {
    name: 'address',
    data() {
      return {
        tabbarController: 1,
        chosenAddressId: '1',
        list: [{
            id: '1',
            name: '张er',
            tel: '13000000000',
            address: '浙江省杭州市西湖区文三路 138 号东方通信大厦 7 楼 501 室'
          },
          {
            id: '2',
            name: '李四',
            tel: '1310000000',
            address: '浙江省杭州市拱墅区莫干山路 50 号'
          }
        ]
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
      onAdd() {
        //   Toast('新增地址');
        this.$router.push('/address2')

      }
    }
  };
</script>

<style>
</style>
