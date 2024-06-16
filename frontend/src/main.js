import './assets/css/main.css'

import { createApp, ref } from 'vue'
import { createAuth0 } from '@auth0/auth0-vue'
import { useRouter } from 'vue-router'

import App from './App.vue'
import router from './router'

const DOMAIN = ref('')
const CLIENT_ID = ref('')
const AUDIENCE = ref('')

const fetchConfig = async () => {
  try {
    let response = await fetch(`${import.meta.env.VITE_API_URL}/keys/domain`, {
      method: 'GET',
    })

    if (!response.ok) {
      throw new Error('Server error')
    }
    DOMAIN.value = await response.text()

    response = await fetch(`${import.meta.env.VITE_API_URL}/keys/client`, {
      method: 'GET',
    })

    if (!response.ok) {
      throw new Error('Server error')
    }
    CLIENT_ID.value = await response.text()

    response = await fetch(`${import.meta.env.VITE_API_URL}/keys/audience`, {
      method: 'GET',
    })

    if (!response.ok) {
      throw new Error('Server error')
    }
    AUDIENCE.value = await response.text()
  } catch (error) {
    router.push('/error')
    throw error
  }
}

const initApp = async () => {
  await fetchConfig()

  const app = createApp(App)

  app.config.errorHandler = (err, vm, info) => {
    router.push('/error')
  }

  window.addEventListener('unhandledrejection', (event) => {
    router.push('/error')
  })

  app.use(
    createAuth0({
      domain: DOMAIN.value,
      clientId: CLIENT_ID.value,
      authorizationParams: {
        redirect_uri: window.location.origin,
        audience: AUDIENCE.value,
      },
      cacheLocation: 'localstorage',
    })
  )

  app.use(router)
  app.mount('#app')
}

initApp()
