import http from '../utils/request.js'

//请求首页数据
export const getData = () => {
	//返回一个promise对象
	return http.get('/home/getData')
}

export const getNewUser = () => {
	//返回一个promise对象
	return http.get('/getRegisterAnnually')
}

export const getUser = (params)=>{
	//返回用户列表
	return http.get('/user/getUser',params)
}

export const addUser = (data)=>{
	
	return http.post('/user/add',data)
}

export const editUser = (data)=>{
	
	return http.post('/user/edit',data)
}

export const delUser = (data)=>{

	return http.post('/user/del',data)
}

//登录密码
export const getMenu= (data) =>{
	return http.post('/login',data)
}

//词云
export const getWord = (param) =>{
	return http.get('/word_count',param)
}

//表格：
export const getList = (params) =>{
	return http.get('/getCritic',params)
}

//对于星级、距离、开门否的排序
export const getListOne = (params) =>{
	return http.get('/orderbyDistance',params)
}

export const getListTwo = (params) =>{
	return http.get('/orderbyStars',params)
}

export const getListThree = (params) =>{
	return http.get('/isOpen',params)
}

//排行榜表单
export const getPopular = (params) =>{
	return http.get('/getPopular',params)
}

//
export const getFake = (params) =>{
	return http.get('/getFake',params)
}

export const getEmotions = (params) =>{
	return http.get('/getEmotions',params)
}

export const getBusinessRe = (params) =>{
	return http.get('/business_referrals',params)
}

export const getCategories = (params) =>{
	return http.get('/categories_number',params)
}

export const getfriend = (params) =>{
	return http.get('/friend_recommend',params)
}

export const getMostBusiness = (params) =>{
	return http.get('/most_business',params)
}

export const getMostCategory = (params) =>{
	return http.get('/most_category',params)
}

export const getMostFivestars = (params) =>{
	return http.get('/most_fivestars',params)
}

export const getNegative = (params) =>{
	return http.get('/most_negative_star',params)
}

export const postBestCatelog = (data) =>{
	return http.post('/best_category',data)
}

export const postCityBest = (data) =>{
	return http.post('/city_best_business',data)
}

export const postRecentWeek = (data) =>{
	return http.post('/recent_weekstars',data)
}

export const postReviewNum = (data) =>{
	return http.post('/review_number',data)
}

export const getUserrecs = (data) =>{
	return http.get('/getUserrecs',data)
}

export const getNumber = (data) =>{
	return http.get('/getNumber',data)
}