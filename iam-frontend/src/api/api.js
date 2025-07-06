import axios from "axios";

const API_BASE = "http://localhost:8000";

export const login = (username, password) => {
  const form = new URLSearchParams();
  form.append("username", username);
  form.append("password", password);

  return axios.post("http://localhost:8000/auth/login", form, {
    headers: {
      "Content-Type": "application/x-www-form-urlencoded"
    }
  });
};


export const getUsers = () => axios.get(`${API_BASE}/users`);
export const getRoles = () => axios.get(`${API_BASE}/roles`);
export const getPermissions = () => axios.get(`${API_BASE}/permissions`);
export const addUser = (userData) => axios.post(`${API_BASE}/users`, userData);
