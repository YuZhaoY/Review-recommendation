<template>
	<el-menu 
	default-active="1-4-1" 
	class="el-menu-vertical-demo" 
	@open="handleOpen" 
	@close="handleClose" :collapse="isCollapse"
	background-color="#545c64"
	text-color="#fff"
	>
		<h3>{{isCollapse ? '后台' :'通用后台管理系统'}}</h3>
	
	  <el-menu-item @click="clickMenu(item)" v-for="item in noChildren":key="item.name" V-bind:index="item.name">
	    <i :class="`el-icon-${item.icon}`"></i>
	    <span slot="title">{{item.label}}</span>
	  </el-menu-item>
	  
	  <el-submenu v-for="item in hasChildren":key="item.label" :index="item.label">
	    <template slot="title">
	      <i class="`el-icon-${item.icon}`"></i>
	      <span slot="title">{{item.label}}</span>
	    </template>
	    <el-menu-item-group v-for="subItem in item.children":key="subItem.page">
	      <!-- <span slot="title">分组一</span> -->
	      <el-menu-item index="subItem.page">{{subItem.label}}</el-menu-item>
	    </el-menu-item-group>
	  </el-submenu>

<!-- 	  <el-menu-item index="3" disabled>
	    <i class="el-icon-document"></i>
	    <span slot="title">导航三</span>
	  </el-menu-item>
	  <el-menu-item index="4">
	    <i class="el-icon-setting"></i>
	    <span slot="title">导航四</span>
	  </el-menu-item> -->
	</el-menu>
</template>




<script>
	import Cookie from "js-cookie"
  export default {
    data() {
      return {
		// menuData:[
		// 	{
		// 		path:'/',
		// 		name:'home',
		// 		label:"首页",
		// 		icon:"s-home",
		// 		url:"Home/Home,"
		// 	},
		// 	{
		// 		path:'/mall',
		// 		name:'mall',
		// 		label:"商品管理",
		// 		icon:"video-play",
		// 		url:"MallManage/MallManage,"
		// 	},
		// 	{
		// 		path:'/user',
		// 		name:'user',
		// 		label:"用户管理",
		// 		icon:"user",
		// 		url:"UserManage/UserManage,"
		// 	},
		// 	{
		// 		path:'/word',
		// 		name:'word',
		// 		label:"词云",
		// 		icon:"thumb",
		// 		url:"WordShow/WordShow,"
		// 	},
		// 	{
		// 		label:"其他",
		// 		icon:"location",
		// 		children:[
		// 			{
		// 			path:'/page1',
		// 			name:'page1',
		// 			label:"页面1",
		// 			icon:"setting",
		// 			url:"Other/PageOne,"	
		// 			},
		// 			{
		// 			path:'/page2',
		// 			name:'page2',
		// 			label:"页面2",
		// 			icon:"setting",
		// 			url:"Other/PageTwo,"	
		// 			}
		// 		]
		// 	},
		// ]
      };
    },
    methods: {
      handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      },
	  //
	  clickMenu(item){
		  console.log(item)
		  if(this.$router.path !== item.path || (this.$router.path==='/home' &&(item.path ==='/'))){
			this.$router.push(item.path)//路由跳转
		  }
		  this.$store.commit('selectMenu',item)//this.那个文件夹下.那个函数
	  }
    },
	computed:{
		//没有子菜单
		noChildren(){
			return this.menuData.filter(item => !item.children)
		},
		//有子菜单
		hasChildren(){
			return this.menuData.filter(item => item.children)
		},
		menuData(){
			//判断当前数据，如果缓存中没有，当前store中获取
			return JSON.parse(Cookie.get('menu')) || this.$store.state.tab.menu
		},
		isCollapse(){
			return this.$store.state.tab.isCollapse
		}
	}
  }
</script>

<style lang="less" scoped>
  .el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 200px;
    min-height: 400px;
  }
  .el-menu {
	  border-right: none;
	  height: 100vh;
	  h3{
		  color: #fff;
		  text-align: center;
		  line-height: 48px;
		  font-size: 16px;
		  font-weight: 400;
	  }
  }
</style>