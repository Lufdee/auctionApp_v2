import { createWebHistory, createRouter } from 'vue-router'

import Home from '../components/Home.vue'
import Profile from '../components/Profile.vue'
import NewItem from '../components/NewItem.vue'

const routes = [
	{
		path: '/',
		name: 'Home',
		component: Home,
	},
	{
		path: '/profile',
		name: 'Profile',
		component: Profile,
	},
	{
		path: '/newitem',
		name: 'NewItem',
		component: NewItem,
	}
]
const router = createRouter({
	history: createWebHistory(),
	routes, //same --- > routes:routes
})
export default router