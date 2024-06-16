<script setup>

</script>

<template>
  <input type="search" placeholder="Search by invoice number">
</template>

<style scoped>
  .search-bar {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  input {
    border: 0;
    background: var(--tertiary);
    color: var(--on-tertiary);
    border-radius: 100px;
    padding: 16px 24px;
    font-size: 16px;
    letter-spacing: 0.5px;
    width: 100%;
  }
</style>
