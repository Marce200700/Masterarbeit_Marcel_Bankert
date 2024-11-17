import { accountService } from '../_services';

const state = {
  user: null,
};

const getters = {
  user: (state) => state.user,
};

const actions = {
  async login({ commit }, { username, password }) {
    try {
      const user = await accountService.login(username, password);
      commit('setUser', user);
    } catch (error) {
      // Handle error, e.g., dispatch an error action
    }
  },
  async logout({ commit }) {
    try {
      await accountService.logout();
      commit('setUser', null);
    } catch (error) {
      // Handle error, e.g., dispatch an error action
    }
  },
};

const mutations = {
  setUser(state, user) {
    state.user = user;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};