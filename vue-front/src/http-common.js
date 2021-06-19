import axios from "axios";

export default axios.create({
  // baseURL: 'http://34.64.197.76/api',
  baseURL: 'http://localhost:8000',
  headers: {
    "Content-type": "application/json"
  }
});