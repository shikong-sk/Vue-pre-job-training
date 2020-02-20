<template>
	<div>
		<div>
			<van-tabs v-model="tabsController" animated swipeable :sticky="true" color="#ff5f16">
				<van-tab v-for="v in channel" :key="v.gid" :title="v.name" :name="v.name">

					<van-list v-model="Loading[v.gid]" :finished="Finished[v.gid]" finished-text="没有更多了" @load="Load(v.gid)">
						<van-cell v-for="data in res[v.gid]" :key="data.mid">

							<van-row @click="$router.push('/detail/' + data.mblog.mid +'/' + v.gid)">
								<van-col span="6" style="min-width: 3.5rem;max-width: 4rem;">
									<van-image round width="3.5rem" height="3.5rem" :src="data.mblog.user.profile_image_url" />
								</van-col>
								<van-col span="18">
									<div class="" style="vertical-align: middle;margin-bottom: 5px;">{{data.mblog.user.screen_name}}</div>
									<div class="" style="">
										{{data.mblog.created_at}}
										<span v-show="data.mblog.source!='' ">来自 {{data.mblog.source}}</span>
									</div>
								</van-col>
							</van-row>

							<div v-html="data.mblog.text"></div>
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
		name: 'home',
		data() {
			return {
				tabbarController: 0,
				tabsController: '热门',
				channel: [{
					"gid": "102803",
					"name": "热门"
				}, {
					"gid": "102803_ctg1_7978_-_ctg1_7978",
					"name": "新鲜事"
				}, {
					"gid": "102803_ctg1_4388_-_ctg1_4388",
					"name": "搞笑"
				}, {
					"gid": "102803_ctg1_1988_-_ctg1_1988",
					"name": "情感"
				}, {
					"gid": "102803_ctg1_4288_-_ctg1_4288",
					"name": "明星"
				}, {
					"gid": "102803_ctg1_4188_-_ctg1_4188",
					"name": "社会"
				}, {
					"gid": "102803_ctg1_5088_-_ctg1_5088",
					"name": "数码"
				}, {
					"gid": "102803_ctg1_1388_-_ctg1_1388",
					"name": "体育"
				}, {
					"gid": "102803_ctg1_5188_-_ctg1_5188",
					"name": "汽车"
				}, {
					"gid": "102803_ctg1_3288_-_ctg1_3288",
					"name": "电影"
				}, {
					"gid": "102803_ctg1_4888_-_ctg1_4888",
					"name": "游戏"
				}],
				Loading: {
					'102803': false,
					"102803_ctg1_7978_-_ctg1_7978": false,
					"102803_ctg1_4388_-_ctg1_4388": false,
					"102803_ctg1_1988_-_ctg1_1988": false,
					"102803_ctg1_4288_-_ctg1_4288": false,
					"102803_ctg1_4188_-_ctg1_4188": false,
					"102803_ctg1_5088_-_ctg1_5088": false,
					"102803_ctg1_1388_-_ctg1_1388": false,
					"102803_ctg1_5188_-_ctg1_5188": false,
					"102803_ctg1_3288_-_ctg1_3288": false,
					"102803_ctg1_4888_-_ctg1_4888": false
				},
				Finished: {
					'102803': false,
					"102803_ctg1_7978_-_ctg1_7978": false,
					"102803_ctg1_4388_-_ctg1_4388": false,
					"102803_ctg1_1988_-_ctg1_1988": false,
					"102803_ctg1_4288_-_ctg1_4288": false,
					"102803_ctg1_4188_-_ctg1_4188": false,
					"102803_ctg1_5088_-_ctg1_5088": false,
					"102803_ctg1_1388_-_ctg1_1388": false,
					"102803_ctg1_5188_-_ctg1_5188": false,
					"102803_ctg1_3288_-_ctg1_3288": false,
					"102803_ctg1_4888_-_ctg1_4888": false
				},
				res: {},
			}
		},
		methods: {
			Load(gid) {
				this.$axios
					.get('../static/weibo/' + gid + '/1.json')
					.then(response => {
						this.res[gid] = response.data.data.cards
						this.Finished[gid] = true
					}, function(e) {
						console.log(e)
					})

				// this.$axios({
				//     method: "GET",
				//     url: 'https://m.weibo.cn/api/container/getIndex?containerid=102803&openApp=0',
				//     headers: {
				//       'Content-Type': 'application/x-www-form-urlencoded',
				//       'referer': 'https://m.weibo.cn/',
				//       'host': 'm.weibo.cn',
				//       'Origin': 'https://m.weibo.cn'
				//     },
				//   }, )
				//   .then(response => {
				//     this.hotRes = response.data.data.cards
				//     this.hotFinished = true
				//   }, function(e) {
				//     console.log(e)
				//   })

				// var instance = this.$axios.create({
				//   method:'GET',
				//   baseURL: 'https://m.weibo.cn/api/container/getIndex?containerid=102803&openApp=0',
				//   headers: {
				//     "Access-Control-Allow-Origin": "*",
				//     "Access-Control-Allow-Headers": "X-Requested-With,Content-Type",
				//     "Access-Control-Allow-Methods": "PUT,POST,GET,DELETE,OPTIONS",
				//     'Referer': 'https://m.weibo.cn/',
				//     'host': 'm.weibo.cn',
				//     'Origin': 'https://m.weibo.cn'
				//   },
				// })

				// instance.interceptors.request.use(config=>{
				//   config.headers['Origin'] = 'https://m.weibo.cn'
				//   return config
				// })

				// instance.get().then(response => {
				//   console.log(response)
				// }, function(e) {
				//   console.log(e)
				// })

			}
		}
	}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
	h1,
	h2 {
		font-weight: normal;
	}

	ul {
		list-style-type: none;
		padding: 0;
	}

	li {
		display: inline-block;
		margin: 0 10px;
	}

	a {
		color: #42b983;
	}
</style>
