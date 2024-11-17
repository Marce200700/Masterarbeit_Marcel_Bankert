import { createStore } from 'vuex';

export default createStore({
  state: {
    users: [],
  },
  getters: {
    getUsers: (state) => state.users,
  },
  mutations: {
    setUsers(state, users) {
      state.users = users;
    },
  },
  actions: {
    async fetchUsers({ commit }) {
      const response = await this.dispatch('userService/getUsers');
      commit('setUsers', response.data);
    },
  },
  modules: {},
});