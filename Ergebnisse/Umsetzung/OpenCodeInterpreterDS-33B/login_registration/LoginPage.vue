<template>
    <div>
        <h2>Login</h2>
        <form @submit.prevent="submit">
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" class="form-control" id="username" v-model="username" required />
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" class="form-control" id="password" v-model="password" required />
            </div>
            <button type="submit" class="btn btn-primary">Login</button>
            <p><a href="/register">Register</a></p>
        </form>
    </div>
</template>

<script>
import { accountActions } from '../_store';

export default {
    name: 'LoginPage',
    data() {
        return {
            username: '',
            password: ''
        };
    },
    methods: {
        submit() {
            this.$store.dispatch(accountActions.login, { username: this.username, password: this.password });
        }
    }
};
</script>