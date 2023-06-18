import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../Views/Home.vue'
import Main from '../Views/Main.vue'
import Mall from '../Views/Mall.vue'
import Login from '../Views/Login'
import Word from '../Views/Word'
import List from '../Views/List'
import List1 from '../Views/List1'
import List2 from '../Views/List2'
import List3 from '../Views/List3'
import List4 from '../Views/List4'
import List5 from '../Views/List5'
import List6 from '../Views/List6'


Vue.use(VueRouter)

//1.创建路由组件
const routes = [
	{
		path:'/',
		component:Main,
		name:'Main',
		redirect:'/home', //重定向到home
		//子路由
		children:[

		]
	},
	{
		path:'/login',
		name:'login',
		component:Login
	}

]

//创建router实例
const router = new VueRouter({
  routes // (缩写) 相当于 routes: routes
})

export default router



