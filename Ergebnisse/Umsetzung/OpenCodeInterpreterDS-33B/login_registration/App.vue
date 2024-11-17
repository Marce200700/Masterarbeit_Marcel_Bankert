<template>
    <div id="app">
        <div class="container">
            <alert></alert>
            <router-view></router-view>
        </div>
    </div>
</template>

<script>
import Alert from './alert';

export default {
    name: 'App',
    components: {
        Alert
    }
};
</script>

<style scoped>
.container {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
}
</style>