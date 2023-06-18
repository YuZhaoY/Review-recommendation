<template>
  <div id="app">
	    <!-- 路由匹配到的组件将渲染在这里 -->
	    <router-view></router-view>
  </div>
</template>

<script>

export default {
  name: 'App'
}
</script>

<style lang="less" >
	//为了去掉默认的样式
	html,body,h3,p{
		margin: 0;
		padding: 0;
	}
</style>


