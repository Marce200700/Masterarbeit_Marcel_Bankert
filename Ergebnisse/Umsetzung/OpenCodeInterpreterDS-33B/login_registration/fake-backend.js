// fake-backend.js

// This file is used to simulate a backend server for testing purposes.
// It provides a simple in-memory database and a set of API endpoints to interact with that database.

// Import the necessary modules
import axios from 'axios';

// Define the in-memory database
let users = JSON.parse(localStorage.getItem('users')) || [];

// Define the API endpoints
export const fakeBackend = {
  register: (user) => {
    // Simulate a delay to mimic network latency
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        // Check if the username already exists
        if (users.find(u => u.username === user.username)) {
          reject('Username "' + user.username + '" is already taken');
        } else {
          // Add the new user to the database
          users.push(user);
          localStorage.setItem('users', JSON.stringify(users));
          resolve(user);
        }
      }, 500);
    });
  },

  login: (username, password) => {
    // Simulate a delay to mimic network latency
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        // Find the user with the given username and password
        const user = users.find(u => u.username === username && u.password === password);

        // If the user is found, resolve with the user object
        if (user) {
          resolve(user);
        } else {
          // If the user is not found, reject with an error message
          reject('Username or password is incorrect');
        }
      }, 500);
    });
  },

  getAllUsers: () => {
    // Simulate a delay to mimic network latency
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        // Resolve with the list of all users
        resolve(users);
      }, 500);
    });
  },

  deleteUser: (username) => {
    // Simulate a delay to mimic network latency
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        // Find the user with the given username
        const userIndex = users.findIndex(u => u.username === username);

        // If the user is found, remove it from the database
        if (userIndex !== -1) {
          users.splice(userIndex, 1);
          localStorage.setItem('users', JSON.stringify(users));
          resolve();
        } else {
          // If the user is not found, reject with an error message
          reject('User not found');
        }
      }, 500);
    });
  }
};