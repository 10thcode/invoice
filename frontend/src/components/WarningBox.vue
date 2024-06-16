<script setup>
  
</script>

<template>
  <div class="warning-box">
    <div class="warning-icon">
        <span class="material-symbols-outlined">warning_amber</span>
    </div>
    <div class="warning-content">
      <div class="warning-title">Warning</div>
      <div class="warning-text">
        For the best experience, please log in
        to save your progress and ensure your
        data is not lost.
      </div>
      <div class="warning-link">Login</div>
    </div>
  </div>
</template>

<style scoped>
  .warning-box {
    border: 1px solid var(--warning);
    border-radius: 24px;
    background: var(--warning-container);
    color: var(--warning);
    display: flex;
    padding: 32px;
    gap: 16px;
  }

  .warning-content {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .warning-title {
    font-size: 16px;
    font-weight: 700;
  }

  .warning-link {
    color: var(--accent);
    font-weight: 700;
    font-size: 14px;
  }
</style>
