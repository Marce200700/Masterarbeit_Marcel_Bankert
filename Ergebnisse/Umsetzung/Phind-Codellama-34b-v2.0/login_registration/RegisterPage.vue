<template>
    <div>
      <h1>Register</h1>
      <form @submit.prevent="register">
        <div>
          <label for="firstName">First Name</label>
          <input type="text" id="firstName" v-model="firstName" required />
        </div>
        <div>
          <label for="lastName">Last Name</label>
          <input type="text" id="lastName" v-model="lastName" required />
        </div>
        <div>
          <label for="username">Username</label>
          <input type="text" id="username" v-model="username" required />
        </div>
        <div>
          <label for="password">Password</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <div>
          <button type="submit">Register</button>
        </div>
        <div v-if="error" class="invalid-feedback">{{ error }}</div>
      </form>
      <p>
        Already have an account? <router-link to="/login">Login</router-link>
      </p>
    </div>
  </template>
  
  <script>
  import { mapState, mapActions } from 'vuex';
  
  export default {
    name: 'RegisterPage',
    data() {
      return {
        firstName: '',
        lastName: '',
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
      ...mapActions('account', ['register']),
    },
  };
  </script>