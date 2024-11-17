<template>
    <div class="home-page">
      <h1>Hi {{ user.firstName }}!</h1>
      <ul>
        <li v-for="user in users" :key="user.id">
          {{ user.firstName }} {{ user.lastName }}
          <a href="#" @click.prevent="deleteUser(user.id)">Delete</a>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
    import { userService } from '../_services';
  
    export default {
      name: 'HomePage',
      data() {
        return {
          user: this.$store.state.account.user,
          users: [],
        };
      },
      created() {
        this.getAllUsers();
      },
      methods: {
        getAllUsers() {
          userService.getAll().then((users) => {
            this.users = users;
          });
        },
        deleteUser(id) {
          userService.delete(id).then(() => {
            this.users = this.users.filter((user) => user.id !== id);
          });
        },
      },
    };
  </script>
  
  <style scoped>
    .home-page {
      padding: 20px;
    }
  </style>