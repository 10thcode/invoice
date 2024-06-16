<script setup>
  defineProps(["bg"])
</script>
<template>
  <input type="submit" value="Submit" :class="bg">
</template>

<style scoped>
  input {
    padding: 16px 24px;
    border-radius: 100px;
    font-weight: 700;
    letter-spacing: 0.5px;
  }

  .none {
    padding: 0;
    background: none;
    color: var(--accent);
  }

  .accent {
    background: var(--accent);
    color: white;
  }

  .secondary {
    background: var(--secondary);
  }
</style>
