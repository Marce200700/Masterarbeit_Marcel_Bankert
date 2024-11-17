import axios from 'axios';

export default {
  register(user) {
    return axios.post('/api/users/register', user);
  },
  login(user) {
    return axios.post('/api/users/login', user);
  },
  getAllUsers() {
    return axios.get('/api/users');
  },
  deleteUser(id) {
    return axios.delete(`/api/users/${id}`);
  }
};