<script setup>
  import { RouterLink } from 'vue-router'
  import { onMounted } from 'vue'
  import { useAuth0 } from '@auth0/auth0-vue'

  const { isAuthenticated } = useAuth0()
</script>

<template>
  <header>
    <div class="topbar">
      <div class="home icon" @click="$router.push('/')">
        <span class="material-symbols-outlined">home</span>
      </div>
      <div class="appname">
        <h1>Invoice</h1>
      </div>
      <div
        @click="isAuthenticated ? $router.push('/account') : $router.push('/account/login')"
        class="account icon">
        <span class="material-symbols-outlined">{{ isAuthenticated ? "account_circle" : "login" }}</span>
      </div>
    </div>
  </header>
</template>

<style scoped>
  .home, .account{
    cursor: pointer;
  }

  .topbar {
    background: var(--secondary);
    padding: 16px;
    display: flex;
    gap: 16px;
  }

  .appname {
    font-size: 20px;
    font-weight: 900;
    width: 100%;
  }

  @media (min-width: 640px) {
    .topbar {
      padding: 16px 32px;
    }
  }

  @media (min-width: 768px) {
    .topbar {
      padding: 16px 64px;
    }
  }

  @media (min-width: 1024px) {
    .topbar {
      padding: 16px 128px;
    }
  }
  
</style>
