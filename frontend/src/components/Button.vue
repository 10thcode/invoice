<script setup>
  defineProps(["bg"])
</script>
<template>
  <button :class="bg">
    <slot />
  </button>
</template>

<style scoped>
  button {
    border-radius: 100px;
    font-weight: 700;
    letter-spacing: 0.5px;
    cursor: pointer;
  }

  .green {
    padding: 16px 24px;
    background: #069470;
    color: white;
  }

  .accent {
    padding: 16px 24px;
    background: var(--accent);
    color: white;
  }

  .secondary {
    padding: 16px 24px;
    background: var(--secondary);
  }
</style>
