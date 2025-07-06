import axios from "axios";

const API_BASE = "http://localhost:8000";

export const login = (username, password) =>
  axios.post(`${API_BASE}/login`, { username, password });

export const getUsers = () => axios.get(`${API_BASE}/users`);
export const getRoles = () => axios.get(`${API_BASE}/roles`);
export const getPermissions = () => axios.get(`${API_BASE}/permissions`);
export const addUser = (userData) => axios.post(`${API_BASE}/users`, userData);