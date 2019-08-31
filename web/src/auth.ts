/* globals localStorage */
import axios from 'axios'

export default {
    login(username: string, pass: string, cb: (value: boolean) => void) {
      cb = arguments[arguments.length - 1]
      if (localStorage.token) {
        if (cb) { cb(true) }
        return
      }
      request(username, pass, (res: any) => {
        if (res.authenticated) {
          localStorage.token = res.token
          if (cb) { cb(true) }
        } else {
          if (cb) { cb(false) }
        }
      })
    },

    getToken() {
      return localStorage.token
    },

    logout(cb: () => void) {
      delete localStorage.token
      if (cb) { cb() }
    },

    loggedIn() {
      return !!localStorage.token
    },
}

function request(user: string, pass: string, cb: (value: any) => void) {
    axios
    .post(
        '/signin/',
        {
            username: user,
            password: pass,
        },
    ).then(
        (response) => {
            cb({
              authenticated: true,
              token: response.data.token,
            })
        },
    ).catch((error: any) => {
        cb({
            authenticated: false,
        })
    })
}

