import { createStore } from 'vuex';

export default createStore({
  state: {
    user: null,
  },
  getters: {
    getUser: (state) => state.user,
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
  },
  actions: {
    login({ commit }, user) {
      // call the login API here
      // if successful, commit the user data
      commit('setUser', user);
    },
    logout({ commit }) {
      // call the logout API here
      // if successful, commit null to the user data
      commit('setUser', null);
    },
  },
  modules: {},
});