import { createModule } from 'vuex-simple';

const state = {
  alert: null,
};

const getters = {
  alert: (state) => state.alert,
};

const mutations = {
  setAlert(state, alert) {
    state.alert = alert;
  },
};

const actions = {
  setAlert({ commit }, alert) {
    commit('setAlert', alert);
  },
};

export default createModule({
  state,
  getters,
  mutations,
  actions,
});