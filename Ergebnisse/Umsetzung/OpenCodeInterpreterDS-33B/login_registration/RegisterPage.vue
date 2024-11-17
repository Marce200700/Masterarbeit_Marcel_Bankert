<template>
    <div>
        <h2>Register</h2>
        <form @submit.prevent="submit">
            <div class="form-group">
                <label for="firstName">First Name</label>
                <input type="text" class="form-control" id="firstName" v-model="user.firstName" required />
            </div>
            <div class="form-group">
                <label for="lastName">Last Name</label>
                <input type="text" class="form-control" id="lastName" v-model="user.lastName" required />
            </div>
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" class="form-control" id="username" v-model="user.username" required />
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" class="form-control" id="password" v-model="user.password" required />
            </div>
            <button type="submit" class="btn btn-primary">Register</button>
            <p><a href="/login">Login</a></p>
        </form>
    </div>
</template>

<script>
import { accountActions } from '../_store';

export default {
    name: 'RegisterPage',
    data() {
        return {
            user: {
                firstName: '',
                lastName: '',
                username: '',
                password: ''
            }
        };
    },
    methods: {
        submit() {
            this.$store.dispatch(accountActions.register, this.user);
        }
    }
};
</script>