<script setup>
  import Button from '../components/Button.vue'
  import { useRouter } from "vue-router"
</script>

<template>
  <div class="hero">
    <div class="hero-title">Invoice</div>
    <div class="hero-content">
      A simple web application for businesses and
      individuals to create and manage invoices efficiently.
    </div>
    <Button
      @click="$router.push('/docs')"
      class="hero-button"
      bg="secondary">Read more</Button>
  </div>
</template>

<style scoped>
  .hero {
    background: url('https://ik.imagekit.io/prezzgh/invoice/hero_background.jpg?updatedAt=1717805134229');
    background-repeat: no-repeat;
    background-size: cover;
    width: 100vw;
    display: flex;
    flex-direction: column;
    gap: 16px;
    align-items: center;
    justify-content: center;
  }

  .hero-title, .hero-content {
    color: white;
    font-weight: 700;
  }

  .hero-title {
    font-size: 36px;
    margin-top: 40px;
  }

  .hero-content {
    font-size: 14px;
    margin: 0 40px;
    text-align: center;
    max-width: 500px;
  }

  .hero-button {
    margin-bottom: 40px;
  }
</style>
