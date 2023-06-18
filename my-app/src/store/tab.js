import Cookie from "js-cookie"

export default {
	state: {
		isCollapse: false, //控制菜单的展开与收起
		tabsList: [{
			path: '/',
			name: 'home',
			label: "首页",
			icon: "s-home",
			url: "Home/Home,"
		}, ], //面包屑的数据
		menu0: [{
				path: '/home',
				name: 'home',
				label: '首页',
				icon: 's-home',
				url: 'Home.vue'
			},
			{
				path: '/mall',
				name: 'mall',
				label: '图形界面分析',
				icon: 'video-play',
				url: 'Mall.vue'
			},
			{
				path: '/word',
				name: 'word',
				label: "词云",
				icon: "thumb",
				url: "Word.vue"
			},
			{
				path: '/list',
				name: 'list',
				label: "表单",
				icon: "thumb",
				url: "List.vue"
			},
			{
				path: '/list1',
				name: 'list1',
				label: "列表1",
				icon: "thumb",
				url: "List1.vue"
			},
			{
				path: '/list2',
				name: 'list2',
				label: "列表2",
				icon: "thumb",
				url: "List2.vue"
			},
			{
				path: '/list3',
				name: 'list3',
				label: "列表3",
				icon: "thumb",
				url: "List3.vue"
			},
			{
				path: '/list4',
				name: 'list4',
				label: "列表4",
				icon: "thumb",
				url: "List4.vue"
			},
			{
				path: '/list5',
				name: 'list5',
				label: "列表5",
				icon: "thumb",
				url: "List5.vue"
			},
			{
				path: '/list6',
				name: 'list6',
				label: "列表6",
				icon: "thumb",
				url: "List6.vue"
			}
		],
		menu1: [{
				path: '/home',
				name: 'home',
				label: '首页',
				icon: 's-home',
				url: 'Home.vue'
			},
			{
				path: '/mall',
				name: 'mall',
				label: '图形界面分析',
				icon: 'video-play',
				url: 'Mall.vue'
			}
		],
		menu:[]
	},
	mutations: {
		collapseMenu(state) {
			//修改菜单的展开收起
			state.isCollapse = !state.isCollapse
		},
		//更新面包屑数据
		selectMenu(state, val) {
			console.log(val, 'val')
			//判断添加的数据是否为首页
			if (val.name !== 'home') {
				const index = state.tabsList.findIndex(item => item.name === val.name)
				//如果不存在
				if (index === -1) {
					state.tabsList.push(val)
				}
			}
		},
		//设置menu的数据
		setMenu(state, val) {
			if(val === 0){
				Cookie.set('menu', JSON.stringify(state.menu0))
			}else{
				Cookie.set('menu', JSON.stringify(state.menu1))
			}
			
		},
		//动态注册路由
		addMenu(state, router) {
			//判断当前缓存中是否有数据
			if (!Cookie.get('menu')) {
				return
			}
			console.log("parse123")
			const menu = JSON.parse(Cookie.get('menu'))
			state.menu = menu
			//组装动态路由的数据
			const menuArray = []
			menu.forEach(item => {
				if (item.children) {
					item.children = item.children.map(item => {
						item.component = () => import(`../Views/${item.url}`)
						return item
					})
					//...相当于全部添加进去
					menuArray.push(...item.children)
				} else {
					item.component = () => import(`../Views/${item.url}`)
					menuArray.push(item)
				}
			})
			console.log(menuArray, "menuArray")

			menuArray.forEach(item => {
				router.addRoute('Main', item)
			})
		}
	}
}
