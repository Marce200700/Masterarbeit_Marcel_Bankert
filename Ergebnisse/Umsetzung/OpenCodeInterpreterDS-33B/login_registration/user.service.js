import axios from 'axios';

export const userService = {
    login,
    logout,
    register,
    getAll,
    getById,
    update,
    delete: _delete
};

function login(username, password) {
    return axios.post('/users/authenticate', { username, password }).then(handleResponse).then(user => {
        // login successful if there's a jwt token in the response
        if (user.token) {
            // store user details and jwt token in local storage to keep user logged in between page refreshes
            localStorage.setItem('user', JSON.stringify(user));
        }

        return user;
    });
}

function logout() {
    // remove user from local storage to log user out
    localStorage.removeItem('user');
}

function register(user) {
    return axios.post('/users/register', user);
}

function getAll() {
    return axios.get('/users').then(handleResponse);
}

function getById(id) {
    return axios.get(`/users/${id}`).then(handleResponse);
}

function update(user) {
    return axios.put(`/users/${user.id}`, user).then(handleResponse);
}

// prefixed function name with underscore because delete is a reserved word in javascript
function _delete(id) {
    return axios.delete(`/users/${id}`).then(handleResponse);
}

// helper functions

function handleResponse(response) {
    if (!(response && response.data)) {
        return Promise.reject(response.statusText);
    }

    return response.data;
}