<template>
	<div>
		<!-- <h1>I'm Main</h1> -->
		<el-container>
		  <el-aside width="auto">
			<Common-aside /> 
		  </el-aside>
		  
		  <el-container >
		    <el-header >
			  <Common-header />
			</el-header>
		    <el-main>
			<!-- 路由出口，路由匹配到的组件将渲染在这里 -->
			<router-view></router-view>	
			</el-main>
		  </el-container>
		</el-container>
	</div>
</template>

<script>
	import CommonAside from '../components/CommonAside.vue'
	import CommonHeader from '../components/CommonHeader.vue'
	export default{
		data(){
			
		},
		components:{
			CommonAside,
			CommonHeader
		}
	}
	
</script>

<style scoped>
	.el-header{
		padding: 0;
	}
</style>