<template>
    <div class="login-page">
      <h1>Login</h1>
      <form @submit.prevent="handleSubmit">
        <div class="form-group">
          <label for="username">Username</label>
          <input
            type="text"
            class="form-control"
            id="username"
            v-model="username"
            required
          />
        </div>
        <div class="form-group">
          <label for="password">Password</label>
          <input
            type="password"
            class="form-control"
            id="password"
            v-model="password"
            required
          />
        </div>
        <div class="form-group">
          <button type="submit" class="btn btn-primary">Login</button>
          <a href="#" @click.prevent="$router.push('/register')">Register</a>
        </div>
      </form>
    </div>
  </template>
  
  <script>
    import { userService } from '../_services';
  
    export default {
      name: 'LoginPage',
      data() {
        return {
          username: '',
          password: '',
        };
      },
      methods: {
        handleSubmit() {
          userService.login(this.username, this.password).then(() => {
            this.$router.push('/');
          });
        },
      },
    };
  </script>
  
  <style scoped>
    .login-page {
      padding: 20px;
    }
  </style>