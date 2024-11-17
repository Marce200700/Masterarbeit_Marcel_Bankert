// auth-header.js
import { getCurrentUser } from './_helpers/auth-header';

export const authHeader = () => {
  const currentUser = getCurrentUser();
  if (currentUser && currentUser.token) {
    return { Authorization: `Bearer ${currentUser.token}` };
  } else {
    return {};
  }
};