import './assets/css/main.css'

import { createApp, ref } from 'vue'
import { createAuth0 } from '@auth0/auth0-vue'
import { useRouter } from 'vue-router'

import App from './App.vue'
import router from './router'

const DOMAIN = import.meta.env.VITE_AUTH0_DOMAIN
const CLIENT_ID = import.meta.env.VITE_AUTH0_CLIENT_ID
const AUDIENCE = import.meta.env.VITE_AUTH0_AUDIENCE
const app = createApp(App)

app.config.errorHandler = (err, vm, info) => {
  router.push('/error')
}

window.addEventListener('unhandledrejection', (event) => {
  router.push('/error')
})

app.use(
  createAuth0({
    domain: DOMAIN,
    clientId: CLIENT_ID,
    authorizationParams: {
      redirect_uri: window.location.origin,
      audience: AUDIENCE,
    },
    cacheLocation: 'localstorage',
  })
)

app.use(router)
app.mount('#app')
