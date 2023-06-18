<template>
	<div>
		<el-card class="box-card0">
			<h3> 评论达人 </h3>
			<el-table  :data="tableData.slice((page[0].currentPage - 1) * page[0].pageSize, page[0].currentPage*page[0].pageSize)" border style="width: 100%">
				<el-table-column prop="user_id" label="用户ID" width="300">
				</el-table-column>
				<el-table-column prop="user_name" label="用户名" width="300">
				</el-table-column>
				<el-table-column prop="user_review_count" label="评论数">
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

		<el-card class="box-card1">
			<h3>搜索商家  </h3>
		<el-dropdown @command="handleCommand">
			<span class="el-dropdown-link">
				下拉菜单<i class="el-icon-arrow-down el-icon--right"></i>
			</span>
			<el-dropdown-menu slot="dropdown">
				<el-dropdown-item command="a">距离排序</el-dropdown-item>
				<el-dropdown-item command="b">星级排序</el-dropdown-item>
				<el-dropdown-item command="c">开门否</el-dropdown-item>
			</el-dropdown-menu>
		</el-dropdown>

		<el-table :data="tableData1" style="width: 100%" border max-height="360px">
			<el-table-column fixed="left" prop="address" label="address" width="300">
			</el-table-column>
			<el-table-column prop="business_id" label="business_id" width="300">
			</el-table-column>
			<el-table-column prop="categories" label="categories">
			</el-table-column>
			<el-table-column prop="distance_to_business" label="distance_to_business">
			</el-table-column>
			<el-table-column prop="is_open" label="is_open">
			</el-table-column>
			<el-table-column prop="name" label="name">
			</el-table-column>
			<el-table-column prop="stars" label="stars">
			</el-table-column>
		</el-table>
		</el-card>
		
		<el-card class="box-card2">
			<h3> 人气达人 </h3>
			<el-table :data="poptable.slice((page[1].currentPage - 1) * page[1].pageSize, page[1].currentPage*page[1].pageSize)" style="width: 100%">
				<el-table-column prop="user_id" label="用户id" width="300">
				</el-table-column>
				<el-table-column prop="user_name" label="用户名" width="300">
				</el-table-column>
				<el-table-column prop="user_fans" label="粉丝数">
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
		<h3>   </h3>
		<el-table :data="fakeData.slice((page[2].currentPage - 1) * page[2].pageSize, page[2].currentPage*page[2].pageSize)" style="width: 100%">
			<el-table-column prop="reviewerID" label="re_id" >
			</el-table-column>
			<el-table-column prop="rating" label="rating" >
			</el-table-column>
			<el-table-column prop="reviewContent" label="内容">
			</el-table-column>
			<el-table-column prop="predict" label="预测">
				<!-- 自定义列 -->
				<template slot-scope="scope">
					<span>{{ scope.row.predict === "N" ? "真实评价" : "虚假评价" }}</span>
				</template>
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

		<el-card>
			<h3> 虚假评论分析</h3>
		<el-table :data="emotionsData.slice((page[2].currentPage - 1) * page[2].pageSize, page[2].currentPage*page[2].pageSize)" style="width: 100%">
			<el-table-column prop="rev_text" label="rev_text" >
			</el-table-column>
			<el-table-column prop="rev_stars" label="rev_stars" >
			</el-table-column>
			<el-table-column prop="predict_class" label="predict_class">
			</el-table-column>
		</el-table>
		<el-pagination
		  @size-change="handleSizeChange3"
		  @current-change="handleCurrentChange3"
		  :current-page="page[3].currentPage"
		  :page-sizes="[2, 5, 8, 10]"
		  :page-size="page[3].pageSize"
		  layout="total, sizes, prev, pager, next, jumper"
		  :total="100">
		</el-pagination>
		</el-card>
		
		<el-card>
			<h3> 评论情感分析</h3>
			<el-dropdown @command="handleChooce">
			  <span class="el-dropdown-link">
			    下拉菜单<i class="el-icon-arrow-down el-icon--right"></i>
			  </span>
			  <el-dropdown-menu slot="dropdown">
			    <el-dropdown-item command="Chinese">Chinese</el-dropdown-item>
			    <el-dropdown-item command="American">American</el-dropdown-item>
			    <el-dropdown-item command="Mexican">Mexican</el-dropdown-item>
			  </el-dropdown-menu>
			</el-dropdown>
		</el-card>
	</div>


</template>

<script>
	import {
		getList,
		getListOne,
		getListTwo,
		getListThree,
		getPopular,
		getFake,
		getEmotions,
		postBestCatelog
	} from '../api'
	export default {
		data() {
			return {
				tableData: [],
				tableData1: [],
				poptable:[],
				fakeData:[],
				emotionsData:[],
				page:[
					{currentPage: 1,
					pageSize: 5},
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
				total: []
			}
		},
		methods: {
			handleCommand(command) {
				//三个表数据
				if (command === "a") {
					getListOne().then(({
						data
					}) => {
						console.log(data, "datalist1")
						this.tableData1 = data.nearbySearch
					})
				} else if (command === "b") {
					getListTwo().then(({
						data
					}) => {
						console.log(data, "datalist2")
						this.tableData1 = data.nearbySearch
					})
				} else {
					getListThree().then(({
						data
					}) => {
						console.log(data, "datalist3")
						this.tableData1 = data.nearbySearch
					})
				}
				},
				
				
				handleChooce(command){
					console.log("进入commandCH")
					if(command === "Chinese" ){
						this.chooce.category = "Chinese"
						postBestCatelog(this.chooce).then(({data}) =>{
							console.log(data,"choose")
						})
						console.log(this.chooce)
					}else if(command === "American"){
						this.chooce.category = "American"
						postBestCatelog(this.chooce).then(({data}) =>{
							console.log(data,"choose")
						})
					}else if(command === "Mexican"){
						this.chooce.category = "Mexican"
						postBestCatelog(this.chooce).then(({data}) =>{
							console.log(data,"choose")
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
			  handleSizeChange3(val) {
				console.log(`每页 ${val} 条`)
				this.page[3].pageSize = val
			  },
			  handleCurrentChange3(val) {
			  	console.log(`当前页: ${val}`)
			  	this.page[3].currentPage = val
			  }
			},
			
			
			mounted() {
				//表格1
				getList().then(({
					data
				}) => {
					console.log(this.page[0],"page0")
					console.log(data, "datalist")
					this.tableData = data.registerAnnually
					console.log("5个1")
					this.total[0] = data.registerAnnually.length
					console.log(this.total)
				})
				//表格2
				this.handleCommand
				//表格3
				getPopular().then(({data}) => {
					console.log(data,"popular")
					this.poptable = data.userPopular
					this.total[1] = data.userPopular.length
					console.log(this.total)
				})
				
				getFake().then(({data}) => {
					console.log(data,"fake")
					this.fakeData = data.fake
					this.total[2] = data.fake.length
				})
				
				getEmotions().then(({data}) => {
					console.log(data,"emotions")
					for(var i = 0; i < 100; i++){
					  this.emotionsData.push(data.emotions[i])
					}
					console.log(this.emotionsData,"this.emo")
				})
				
				this.handleChooce
				

				

			}

		}
	
</script>

<style lang="less" scoped>
	.box-card0{
		height: 360px;
		border: 1px #0f1c28;
		margin-bottom: 20px;
	}
	.box-card1{
		
	}
</style>
