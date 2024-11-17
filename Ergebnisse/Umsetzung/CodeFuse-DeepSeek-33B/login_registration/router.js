import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('../home/HomePage.vue'),
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../login/LoginPage.vue'),
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('../register/RegisterPage.vue'),
  },
];

const router = new VueRouter({
  mode: 'history',
  routes,
});

export default router;