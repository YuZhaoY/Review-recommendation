<template>
	<el-card>
		<h3> 好友推荐 </h3>
		<el-table  :data="tableData.slice((currentPage - 1) * pageSize, currentPage*pageSize)" border style="width: 100%">
			<el-table-column prop="user_id" label="user_id" width="300">
			</el-table-column>
			<el-table-column prop="recommend" label="recommend" width="300">
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
</template>

<script>
	import {getfriend} from '../api'
	
	export default{
		data() {
			return{
				tableData:[],
				currentPage:1,
				pageSize:5,
				total:0
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
		}	
		},
		
		mounted() {
			getfriend().then(({data}) =>{
				console.log(data,"list3")
				this.tableData = data.friendRecommend
				this.total = data.friendRecommend.length
			})
		}
	}
</script>

<style>
</style>