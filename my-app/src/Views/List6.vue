<template>
	<div>
	<el-card class="box-card1">
		<h3> 商户评分分布及评论数量 </h3>
	<el-dropdown @command="handleChooce">
		<span class="el-dropdown-link">
			下拉菜单<i class="el-icon-arrow-down el-icon--right"></i>
		</span>
		<el-dropdown-menu slot="dropdown">
			<el-dropdown-item command="a">Chinese</el-dropdown-item>
			<el-dropdown-item command="b">American</el-dropdown-item>
			<el-dropdown-item command="c">Mexican</el-dropdown-item>
		</el-dropdown-menu>
	</el-dropdown>
	
	<el-table :data="ReviewData.slice((page[0].currentPage - 1) * page[0].pageSize, page[0].currentPage*page[0].pageSize)" style="width: 100%" border max-height="360px">
		<el-table-column fixed="left" prop="category" label="category" width="300">
		</el-table-column>
		<el-table-column prop="name" label="name" width="300">
		</el-table-column>
		<el-table-column prop="rev_num" label="rev_num">
		</el-table-column>
	</el-table>
	<el-pagination
	  @size-change="handleSizeChange"
	  @current-change="handleCurrentChange"
	  :current-page="page[0].currentPage"
	  :page-sizes="[2, 5, 8, 10]"
	  :page-size="page[0].pageSize"
	  layout="total, sizes, prev, pager, next, jumper"
	  :total="total[0]">
	</el-pagination>
	</el-card>	
	
	<el-card>
		<h3> 城市最好商户 </h3>
		<el-table :data="CityData.slice((page[1].currentPage - 1) * page[1].pageSize, page[1].currentPage*page[1].pageSize)" style="width: 100%" border max-height="360px">
			<el-table-column fixed="left" prop="business_id" label="business_id" width="300">
			</el-table-column>
			<el-table-column prop="city" label="city" width="300">
			</el-table-column>
			<el-table-column prop="name" label="name">
			</el-table-column>
			<el-table-column prop="stars" label="stars">
			</el-table-column>
		</el-table>
		<el-pagination
		  @size-change="handleSizeChange1"
		  @current-change="handleCurrentChange1"
		  :current-page="page[1].currentPage"
		  :page-sizes="[2, 5, 8, 10]"
		  :page-size="page[1].pageSize"
		  layout="total, sizes, prev, pager, next, jumper"
		  :total="total[1]">
		</el-pagination>
	</el-card>
	
	<el-card>
		<h3> 最近一周评分 </h3>
		<el-table :data="RecentData.slice((page[2].currentPage - 1) * page[2].pageSize, page[2].currentPage*page[2].pageSize)" style="width: 100%" border max-height="360px">
			<el-table-column fixed="left" prop="rev_business_id" label="rev_business_id" width="300">
			</el-table-column>
			<el-table-column prop="rev_date" label="rev_date" width="300">
			</el-table-column>
			<el-table-column prop="rev_stars" label="rev_stars">
			</el-table-column>
		</el-table>
		<el-pagination
		  @size-change="handleSizeChange2"
		  @current-change="handleCurrentChange2"
		  :current-page="page[2].currentPage"
		  :page-sizes="[2, 5, 8, 10]"
		  :page-size="page[2].pageSize"
		  layout="total, sizes, prev, pager, next, jumper"
		  :total="total[2]">
		</el-pagination>
	</el-card>
	</div>
</template>

<script>
	import {
	postRecentWeek,
	postReviewNum,
	postCityBest
	} from '../api'
	export default {
		data() {
			return {
					RecentData:[],
					ReviewData:[],
					CityData:[],
				page:[
					{currentPage: 1,
					pageSize: 5},
					{currentPage: 1,
					pageSize: 5},
					{currentPage: 1,
					pageSize: 5},
				],
				chooce:{
					category: ''
				},
				total: [],
				putfir:{
					city:"Affton"
				},
				putsec:{
					date:"2018-04-15"
				}
			}
		},
		methods: {				
				handleChooce(command){
					console.log("进入commandCH")
					if(command === "a" ){
						this.chooce.category = "Chinese"
						postReviewNum(this.chooce).then(({data}) =>{
							console.log(data,"chooseC")
							this.ReviewData = data.reviewNumber
							this.total[0] = data.reviewNumber.length
						})
						console.log(this.chooce)
					}else if(command === "b"){
						this.chooce.category = "American"
						postReviewNum(this.chooce).then(({data}) =>{
							console.log(data,"chooseA")
							this.ReviewData = data.reviewNumber
							this.total[0] = data.reviewNumber.length
						})
					}else if(command === "c"){
						this.chooce.category = "Mexican"
						postReviewNum(this.chooce).then(({data}) =>{
							console.log(data,"chooseM")
							this.ReviewData = data.reviewNumber
							this.total[0] = data.reviewNumber.length
						})
						
					}
				},
				
				
			  handleSizeChange(val) {
				console.log(`每页 ${val} 条`)
				this.page[0].pageSize = val
			  },
			  handleCurrentChange(val) {
				console.log(`当前页: ${val}`)
				this.page[0].currentPage = val
			  },
			  handleSizeChange1(val) {
				console.log(`每页 ${val} 条`)
				this.page[1].pageSize = val
			  },
			  handleCurrentChange1(val) {
			  	console.log(`当前页: ${val}`)
			  	this.page[1].currentPage = val
			  },
			  handleSizeChange2(val) {
				console.log(`每页 ${val} 条`)
				this.page[2].pageSize = val
			  },
			  handleCurrentChange2(val) {
			  	console.log(`当前页: ${val}`)
			  	this.page[2].currentPage = val
			  },
			},
			mounted() {
				this.handleChooce
				postCityBest(this.putfir).then(({data}) =>{
					console.log(data,"putfir")
					this.CityData = data.cityBestBusiness
					this.total[1] = data.cityBestBusiness.length
				})
				
				postRecentWeek(this.putsec).then(({data}) =>{
					console.log(data,"putsec")
					this.RecentData = data.recentWeedstars
					this.total[2] = data.recentWeedstars.length
				})
			}
	
		}
</script>

<style>
</style>