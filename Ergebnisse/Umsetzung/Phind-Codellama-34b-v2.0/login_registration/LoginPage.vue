<template>
    <div>
      <h1>Login</h1>
      <form @submit.prevent="login">
        <div>
          <label for="username">Username</label>
          <input type="text" id="username" v-model="username" required />
        </div>
        <div>
          <label for="password">Password</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <div>
          <button type="submit">Login</button>
        </div>
        <div v-if="error" class="invalid-feedback">{{ error }}</div>
      </form>
      <p>
        Don't have an account? <router-link to="/register">Register</router-link>
      </p>
    </div>
  </template>
  
  <script>
  import { mapState, mapActions } from 'vuex';
  
  export default {
    name: 'LoginPage',
    data() {
      return {
        username: '',
        password: '',
      };
    },
    computed: {
      ...mapState({
        error: (state) => state.alert.error,
      }),
    },
    methods: {
      ...mapActions('account', ['login']),
    },
  };
  </script>