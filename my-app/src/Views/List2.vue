<template>
	<div>
	<el-card>
		<h3> </h3>
		<el-table  :data="tableData.slice((currentPage - 1) * pageSize, currentPage*pageSize)" border style="width: 100%">
			<el-table-column prop="categories_number" label="目录数" width="300">
			</el-table-column>
			<el-table-column prop="category" label="目录" width="300">
			</el-table-column>
		</el-table>
		<el-pagination
		  @size-change="handleSizeChange"
		  @current-change="handleCurrentChange"
		  :current-page="currentPage"
		  :page-sizes="[2, 5, 8, 10]"
		  :page-size="pageSize"
		  layout="total, sizes, prev, pager, next, jumper"
		  :total="total">
		</el-pagination>
	</el-card>
	
	<el-card>
		<el-table  :data="tableData1.slice((currentPage1 - 1) * pageSize1, currentPage1*pageSize1)" border style="width: 100%">
			<h3> 用户商家推荐 </h3>
			<el-table-column prop="rev_user_id" label="rev_user_id" width="300">
			</el-table-column>
			<el-table-column prop="rev_stars" label="rev_stars" width="300">
			</el-table-column>
			<el-table-column prop="rev_business_id" label="rev_business_id" width="300">
			</el-table-column>
			<el-table-column prop="user" label="user" width="300">
			</el-table-column>
			<el-table-column prop="recommendations" label="recommendations" width="300">
			</el-table-column>
			<el-table-column prop="f1" label="f1" width="300">
			</el-table-column>
			<el-table-column prop="business" label="business" width="300">
			</el-table-column>
		</el-table>
		<el-pagination
		  @size-change="handleSizeChange1"
		  @current-change="handleCurrentChange1"
		  :current-page="currentPage1"
		  :page-sizes="[2, 5, 8, 10]"
		  :page-size="pageSize1"
		  layout="total, sizes, prev, pager, next, jumper"
		  :total="total1">
		</el-pagination>
	</el-card>
	</div>
</template>

<script>
	import {getCategories,getUserrecs} from '../api'
	
	export default{
		data() {
			return{
				tableData:[],
				tableData1:[],
				currentPage:1,
				pageSize:5,
				currentPage1:1,
				pageSize1:5,
				total:0,
				total1: 0
			}
		},
		methods:{
		handleSizeChange(val) {
			console.log(`每页 ${val} 条`)
			this.pageSize = val
		},
		handleCurrentChange(val) {
			console.log(`当前页: ${val}`)
			this.currentPage = val
		},
			handleSizeChange1(val) {
				console.log(`每页 ${val} 条`)
				this.pageSize1 = val
			},
			handleCurrentChange1(val) {
				console.log(`当前页: ${val}`)
				this.currentPage1 = val
			}	
		},
		
		mounted() {
			getCategories().then(({data}) =>{
				console.log(data,"list1")
				this.tableData = data.categoriesNumber
				this.total = data.categoriesNumber.length
			})
			
			getUserrecs().then(({data}) =>{
				console.log(data,"list2")
				this.tableData1 = data.userrecs
				this.total1 = data.userrecs.length
			})
		}
	}
</script>

<style>
</style>