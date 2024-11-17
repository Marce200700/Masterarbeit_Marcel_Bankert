<template>
    <div>
      <h1>Hi, {{ firstName }}!</h1>
      <ul>
        <li v-for="user in users" :key="user.id">
          {{ user.firstName }} {{ user.lastName }}
          <button @click="deleteUser(user.id)">Delete</button>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import { mapState, mapActions } from 'vuex';
  
  export default {
    name: 'HomePage',
    computed: {
      ...mapState({
        users: (state) => state.users.all,
        firstName: (state) => state.account.user.firstName,
      }),
    },
    methods: {
      ...mapActions('users', ['deleteUser']),
    },
    created() {
      this.$store.dispatch('users/getAllUsers');
    },
  };
  </script>