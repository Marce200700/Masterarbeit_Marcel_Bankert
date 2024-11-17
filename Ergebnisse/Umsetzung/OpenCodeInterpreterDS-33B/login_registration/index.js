import Vue from 'vue';
import Vuex from 'vuex';
import { router } from './_helpers';
import { store } from './_store';
import App from './app/App.vue';

Vue.use(Vuex);

new Vue({
    el: '#app',
    router,
    store,
    render: h => h(App)
});