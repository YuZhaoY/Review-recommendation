<template>
	<el-card>
		<h3>商户经营推荐</h3>
		<el-table  :data="tableData.slice((currentPage - 1) * pageSize, currentPage*pageSize)" border style="width: 100%">
			<el-table-column prop="Business_Referrals" label="Business_Referrals" >
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
	import {getBusinessRe} from '../api'
	
	export default{
		data() {
			return{
				tabledata:[],
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
			getBusinessRe().then(({data}) =>{
				console.log(data,"list111")
				this.tabledata = data.businessReferrals
				console.log(this.tabledata )
				this.total = data.businessReferrals.length

			})
		}
	}
</script>

<style>
</style>