import { authHeader } from '../_helpers';
import { userService } from '../_services';

const state = {
    user: null
};

const actions = {
    login({ commit }, { username, password }) {
        return userService.login(username, password).then(
            user => {
                commit('loginSuccess', user);
                return user;
            },
            error => {
                commit('loginFailure');
                throw error;
            }
        );
    },

    logout({ commit }) {
        userService.logout();
        commit('logout');
    },

    register({ commit }, user) {
        return userService.register(user).then(
            user => {
                commit('registerSuccess');
                return user;
            },
            error => {
                commit('registerFailure');
                throw error;
            }
        );
    }
};

const mutations = {
    loginSuccess(state, user) {
        state.user = user;
    },

    loginFailure(state) {
        state.user = null;
    },

    registerSuccess(state) {
        state.user = null;
    },

    registerFailure(state) {
        state.user = null;
    },

    logout(state) {
        state.user = null;
    }
};

export const account = {
    namespaced: true,
    state,
    actions,
    mutations
};