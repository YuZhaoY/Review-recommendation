<template>
	<div>
		<el-card style="height: 360px;">
			<h3>用户比例</h3>
			<!-- 折线图 -->
			<div ref="echarts1" style="height: 360px;"></div>
		</el-card>
		
		<el-row>
		  <el-col :span="12">
			  <el-card style="height: 260px;">
				<h3>菜系比例</h3>
			  	<div ref="echarts3" style="height: 240px;"></div>
			  </el-card>
		  </el-col>
		  <el-col :span="12">
			  <el-card style="height: 260px;">
				  <!-- 柱状图 -->
				  <h3>每年新注册用户</h3>
			  	<div ref="echarts2" style="height: 260px;"></div>
			  </el-card>
		  </el-col>
		</el-row>
		

	</div>

</template>

<script>
	import * as echarts from 'echarts'
	import {
		getNewUser,getMostCategory,getNumber
	} from '../api'
	
	export default {
		data() {
			return {
				userData:[],
				cateData:[],
				NumberData:[],
				data1:[],
				data2:[],
				year:[]
				}
		},
		mounted() {
			getNewUser().then(({
					data
				}) => {
					this.userData = data.registerAnnually
					

					console.log(this.userData.map(item => item.year),"????")
					// const echarts1 = echarts.init(this.$refs.echarts1)
					// //指定图表的配置项和数据
					// var echarts1Option = {}
					// //处理数据xAxis(解构数据)
					// const {
					// 	orderData
					// } = data.data
					// const xAxis = Object.keys(orderData.data[0])
					// const xAxisData = {
					// 	data: xAxis
					// }
					// echarts1Option.xAxis = xAxisData
					// echarts1Option.yAxis = {}
					// echarts1Option.legend = xAxisData
					// echarts1Option.series = []
					// xAxis.forEach(key => {
					// 	echarts1Option.series.push({
					// 		name: key,
					// 		data: orderData.data.map(item => item[key]),
					// 		type: 'line'
					// 	})
					// })
					// console.log(echarts1Option)
					// //使用指定的配置项和数据显示图表
					// echarts1.setOption(echarts1Option)
					

					
					//柱状图
					const echarts2 = echarts.init(this.$refs.echarts2)
					const echart2Option = {
						legend: {
							// 图例文字颜色
							textStyle: {
								color: "#333",
							},
						},
						grid: {
							left: "20%",
						},
						// 提示框
						tooltip: {
							trigger: "axis",
						},
						xAxis: {
							type: "category", // 类目轴
							data: this.userData.map(item => item.year),
							axisLine: {
								lineStyle: {
									color: "#17b3a3",
								},
							},
							axisLabel: {
								interval: 0,
								color: "#333",
							},
						},
						yAxis: [{
							type: "value",
							axisLine: {
								lineStyle: {
									color: "#17b3a3",
								},
							},
						}, ],
						color: ["#2ec7c9", "#b6a2de", "#5ab1ef", "#ffb980", "#d87a80", "#8d98b3"],
						series: [{
								name: '新增用户',
								data: this.userData.map(item => item.count),
								type: 'bar'
							}
							// ,
							// {
							// 	name: '活跃用户',
							// 	data: userData.map(item => item.active),
							// 	type: 'bar'
							// }
						],
					}
					echarts2.setOption(echart2Option)
				})
				
				getMostCategory().then(({data}) =>{
					console.log(data,"datarecent")
					this.cateData = data.mostCategory
					
					//饼状图
					const echarts3 = echarts.init(this.$refs.echarts3)
					const echarts3Option = {
						tooltip: {
							trigger: "item",
						},
						color: [
							"#0f78f4",
							"#dd536b",
							"#9462e5",
							"#a6a6a6",
							"#e1bb22",
							"#39c362",
							"#3ed1cf",
						],
						series: [{
							data: this.cateData,
							type: 'pie'
						}],
					}
					console.log("饼状图")
					echarts3.setOption(echarts3Option)
					
				})
				
				getNumber().then(({data}) =>{
					console.log(data,"getNum")
					this.NumberData = data.userNumber
					
					for(var i=0;i<data.userNumber.length;i++){
						
						this.data1.push(this.NumberData[i].elite_number/this.NumberData[i].user_number)
						this.data2.push(this.NumberData[i].silence_number/this.NumberData[i].user_number)
						this.year.push(this.NumberData[i].year)
					}
					
					console.log(this.NumberData.year,"this.NumberData.year")
					const echarts1 = echarts.init(this.$refs.echarts1)
					//指定图表的配置项和数据
					var echarts1Option = {}

					echarts1Option.xAxis = {
						type: 'category',
						data: this.year
					}
					echarts1Option.yAxis = {}
					echarts1Option.legend = {data: ['person','silence']}
					echarts1Option.series = [
						{
							data:this.data1,
							name:'person',
							type:'line',

						},
						{
							data:this.data2,
							name:'silence',
							type:'line',

						}
					]

					console.log(echarts1Option,"echarts1Option")
					//使用指定的配置项和数据显示图表
					echarts1.setOption(echarts1Option)
				})
			}
	}
</script>

<style>
</style>
