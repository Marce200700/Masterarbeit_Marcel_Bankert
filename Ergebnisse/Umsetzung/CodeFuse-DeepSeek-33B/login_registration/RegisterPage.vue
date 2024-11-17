<template>
    <div class="register-page">
      <h1>Register</h1>
      <form @submit.prevent="handleSubmit">
        <div class="form-group">
          <label for="firstName">First Name</label>
          <input
            type="text"
            class="form-control"
            id="firstName"
            v-model="firstName"
            required
          />
        </div>
        <div class="form-group">
          <label for="lastName">Last Name</label>
          <input
            type="text"
            class="form-control"
            id="lastName"
            v-model="lastName"
            required
          />
        </div>
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
          <button type="submit" class="btn btn-primary">Register</button>
          <a href="#" @click.prevent="$router.push('/login')">Login</a>
        </div>
      </form>
    </div>
  </template>
  
  <script>
    import { userService } from '../_services';
  
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
      methods: {
        handleSubmit() {
          userService.register(this.firstName, this.lastName, this.username, this.password).then(() => {
            this.$router.push('/login');
          });
        },
      },
    };
  </script>
  
  <style scoped>
    .register-page {
      padding: 20px;
    }
  </style>