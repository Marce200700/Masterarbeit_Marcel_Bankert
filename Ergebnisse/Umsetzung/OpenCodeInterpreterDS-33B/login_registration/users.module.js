import { userService } from '../_services';

const state = {
    users: []
};

const actions = {
    getAll({ commit }) {
        userService.getAll().then(
            users => commit('getAllSuccess', users),
            error => {
                commit('getAllFailure');
                throw error;
            }
        );
    },

    deleteUser({ commit }, id) {
        userService.delete(id).then(
            () => commit('deleteUserSuccess', id),
            error => {
                commit('deleteUserFailure');
                throw error;
            }
        );
    }
};

const mutations = {
    getAllSuccess(state, users) {
        state.users = users;
    },

    getAllFailure(state) {
        state.users = [];
    },

    deleteUserSuccess(state, id) {
        state.users = state.users.filter(user => user.id !== id);
    },

    deleteUserFailure(state) {
        // revert state if delete failed
    }
};

export const users = {
    namespaced: true,
    state,
    actions,
    mutations
};