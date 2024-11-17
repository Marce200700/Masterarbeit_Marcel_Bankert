import { accountService } from '../_services';

const state = {
  user: null,
};

const getters = {
  user: (state) => state.user,
};

const actions = {
  async login({ commit }, { username, password }) {
    const user = await accountService.login(username, password);
    commit('setUser', user);
  },
  async logout({ commit }) {
    await accountService.logout();
    commit('setUser', null);
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