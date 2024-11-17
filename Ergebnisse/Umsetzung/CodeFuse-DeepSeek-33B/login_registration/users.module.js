import Vue from 'vue';
import Vuex from 'vuex';
import userService from '../_services/user.service';

Vue.use(Vuex);

const user = JSON.parse(localStorage.getItem('user'));
const initialState = user
  ? { status: { loggedIn: true }, user }
  : { status: {}, user: null };

export const users = {
  namespaced: true,
  state: initialState,
  actions: {
    login({ commit }, user) {
      return new Promise((resolve, reject) => {
        userService.login(user)
          .then(
            user => {
              commit('loginSuccess', user);
              resolve(user);
            },
            error => {
              commit('loginFailure');
              reject(error);
            }
          );
      });
    },
    logout({ commit }) {
      userService.logout();
      commit('logout');
    },
    register({ commit }, user) {
      return new Promise((resolve, reject) => {
        userService.register(user)
          .then(
            user => {
              commit('registerSuccess');
              resolve(user);
            },
            error => {
              commit('registerFailure');
              reject(error);
            }
          );
      });
    },
    getAll({ commit }) {
      return new Promise((resolve, reject) => {
        userService.getAll()
          .then(
            users => {
              commit('getAllSuccess', users);
              resolve(users);
            },
            error => {
              commit('getAllFailure');
              reject(error);
            }
          );
      });
    },
    getById({ commit }, id) {
      return new Promise((resolve, reject) => {
        userService.getById(id)
          .then(
            user => {
              commit('getByIdSuccess', user);
              resolve(user);
            },
            error => {
              commit('getByIdFailure');
              reject(error);
            }
          );
      });
    },
    deleteUser({ commit }, id) {
      return new Promise((resolve, reject) => {
        userService.deleteUser(id)
          .then(
            () => {
              commit('deleteUserSuccess');
              resolve();
            },
            error => {
              commit('deleteUserFailure');
              reject(error);
            }
          );
      });
    }
  },
  mutations: {
    loginSuccess(state, user) {
      state.status = { loggedIn: true };
      state.user = user;
    },
    loginFailure(state) {
      state.status = {};
      state.user = null;
    },
    logout(state) {
      state.status = {};
      state.user = null;
    },
    registerSuccess(state) {
      state.status = {};
      state.user = null;
    },
    registerFailure(state) {
      state.status = {};
      state.user = null;
    },
    getAllSuccess(state, users) {
      state.all = users;
    },
    getAllFailure(state) {
      state.all = [];
    },
    getByIdSuccess(state, user) {
      state.user = user;
    },
    getByIdFailure(state) {
      state.user = null;
    },
    deleteUserSuccess(state) {
      state.user = null;
    },
    deleteUserFailure(state) {
      state.user = null;
    }
  }
};