import Vue from 'vue'
import VueRouter from 'vue-router'
import HomePage from '../home/HomePage.vue'
import LoginPage from '../login/LoginPage.vue'
import RegisterPage from '../register/RegisterPage.vue'

Vue.use(VueRouter)

const routes = [
  { path: '/', component: HomePage },
  { path: '/login', component: LoginPage },
  { path: '/register', component: RegisterPage }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
