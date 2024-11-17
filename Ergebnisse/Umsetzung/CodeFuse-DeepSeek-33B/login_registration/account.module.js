import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: null,
  },
  mutations: {
    loginSuccess(state, user) {
      state.user = user;
    },
    logout(state) {
      state.user = null;
    },
  },
  actions: {
    login({ commit }, user) {
      return new Promise((resolve, reject) => {
        // Call the login API here
        // If successful, commit the loginSuccess mutation
        // If unsuccessful, reject the promise
      });
    },
    logout({ commit }) {
      // Call the logout API here
      // Commit the logout mutation
    },
  },
});