<template>
    <div>
        <h1>Hi {{user.firstName}} {{user.lastName}}</h1>
        <p>You're logged in with Vue & Vuex!!</p>
        <p><a href="/login">Logout</a></p>
        <h3>All registered users:</h3>
        <ul>
            <li v-for="user in users" :key="user.id">
                {{user.firstName}} {{user.lastName}}
                <a href="#" @click.prevent="deleteUser(user.id)">Delete</a>
            </li>
        </ul>
    </div>
</template>

<script>
import { userActions } from '../_store';

export default {
    name: 'HomePage',
    computed: {
        user() {
            return this.$store.state.account.user;
        },
        users() {
            return this.$store.state.users.users;
        }
    },
    methods: {
        deleteUser(id) {
            this.$store.dispatch(userActions.deleteUser, id);
        }
    },
    created() {
        this.$store.dispatch(userActions.getAll);
    }
};
</script>