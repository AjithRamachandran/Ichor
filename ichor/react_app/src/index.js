import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter as Router, Route } from 'react-router-dom'

import axios from 'axios'
import 'bootstrap/dist/css/bootstrap.min.css'

import LoginPage from './pages/Login.jsx'
import HomePage from './pages/Home.jsx'
import SignupPage from './Pages/Signup.jsx'

import './assets/style.scss'

axios.defaults.withCredentials = true
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

ReactDOM.render(
  <Router>
    <Route component={LoginPage} path='/login' exact></Route>
    <Route component={SignupPage} path='/signup' exact></Route>
    <Route component={HomePage} path='/' exact></Route>
  </Router>,
  document.getElementById('root')
);
