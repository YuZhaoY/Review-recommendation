import Vue from 'vue'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import App from './App.vue'
import router from './router'
import store from './store'
import './api/mock'
import Cookie from 'js-cookie'

Vue.config.productionTip = false

//按序引用
Vue.use(ElementUI)

//添加全局前置导航守卫
router.beforeEach((to, from, next) => {
  // token存不存在
  const token = Cookie.get('token')
  if(!token && to.name !== 'login'){
	 //token不存在，说明当前用户为登录，应该跳转到登录页
	  next({name:'login'})
  }else if(token && to.name === 'login'){
	  //token存在应该跳转到首页
	  next({name:'home'})
  }else{
	  next()
  }
})

new Vue({
  store,
  router,
  render: h => h(App),
  created() {
  	store.commit('addMenu',router)
  }
}).$mount('#app')
