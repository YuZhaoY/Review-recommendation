<template>

		<el-form ref="form" label-width="70px" class="login-container" :inline="true" :model="form" :rules="rules">
			<h3 class="login-title"> 系统登录 </h3>
			<el-form-item label="用户名" prop="username">
				<el-input v-model="form.username" placeholder="请输入用户名"></el-input>
			</el-form-item>
			<el-form-item label="密码" prop="password">
				<el-input type="password" v-model="form.password" placeholder="请输入密码"> </el-input>
			</el-form-item>
			<el-form-item >
				<el-button style="margin-left:105px;margin-top:10px" type="primary" @click="submit"> 登录 </el-button>
			</el-form-item>
		</el-form>


		
</template>

<script>
	import Mock from "mockjs"
	import Cookie from "js-cookie"
	import {getMenu} from '../api'
	
	export default {
		data() {
			return {
				form:{
					username:'',
					password:''
				},
				rules: {
				          username: [
				            { required: true, message: '请输入账号', trigger: 'blur' }
				          ],
				          password: [
				            { required: true, message: '请输入密码', trigger: 'blur' }
				          ]
				        }
			}
		},
		methods: {
			//登录
			submit() {
				// //token信息
				// const token = Mock.Random.guid()
				// //token信息存入到cookie中用于不同页面的通信
				// Cookie.set('token',token)
				
				//校验通过
				console.log(12345)
				this.$refs.form.validate((valid) => {
					console.log(1234)
					if(valid){
						console.log(1235,this.form)
						getMenu(this.form).then((data) => {
							console.log("进入getMenu")
							console.log(data)
							
							if(data.data.code === "success"){
								Cookie.set('token',data.data.access_token)

								//获取菜单的数据，然后store中
								this.$store.commit('setMenu',data.data.flag)

								this.$store.commit('addMenu',this.$router)

								// //跳转到首页
								this.$router.push('/home')

							}else{

								 this.$message.error(data.data.message)
							}
						})
					}
				})
				

			}
		},
	}
</script>

<style lang="less" scoped>
	.login-container{
		width: 350px;
		border:1px soild #eaeaea;
		margin:180px auto;
		padding:35px 35px 15px 35px;
		background:#fff;
		border-radius:15px;
		box-shadow:0 0 25px #cac6c6;
		box-sizing:border-box;
		.el-input{
			width: 198px;
		}
		.login-title{
			text-align:center;
			margin-bottom:40px;
			color:#505428;
		}
	}
</style>