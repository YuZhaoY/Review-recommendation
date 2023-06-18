<template>
	<div>
	<el-card class="box-card0">
		<h3>前20商户</h3>
		<el-table  :data="BussData.slice((page[0].currentPage - 1) * page[0].pageSize, page[0].currentPage*page[0].pageSize)" border style="width: 100%">
			<el-table-column prop="avg_stars" label="avg_stars" width="300">
			</el-table-column>
			<el-table-column prop="name" label="name" width="300">
			</el-table-column>
			<el-table-column prop="name_count" label="name_count">
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
		
		<el-card class="box-card2">
			<h3>商户菜系统计</h3>
			<el-table :data="CateData.slice((page[1].currentPage - 1) * page[1].pageSize, page[1].currentPage*page[1].pageSize)" style="width: 100%">
				<el-table-column prop="category_count" label="category_count" width="300">
				</el-table-column>
				<el-table-column prop="name" label="name" width="300">
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
	</div>
</template>

<script>
	import {
		getMostBusiness,
		getMostCategory
		} from '../api'
	export default{
	data() {
		return {
			BussData: [],
			CateData: [],
			page:[
				{currentPage: 1,
				pageSize: 5},
				{currentPage: 1,
				pageSize: 5},
			],
			total: []
		}
	},
	methods:{
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
	},
	
		mounted() {
			getMostBusiness().then(({data}) =>{
				console.log(data,"buss")
				this.BussData = data.mostBestBusiness
				this.total[0] = data.mostBestBusiness.length
			})
			
			getMostCategory().then(({data}) =>{
				console.log(data,"cate")
				this.CateData = data.mostCategory
				this.total[1] = data.mostCategory.length
			})
		}
	}	

</script>

<style>
</style>