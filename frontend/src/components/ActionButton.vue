<template>
    <div class="fab">
      <div class="fab-text">Create invoice</div>
      <span class="fab-icon material-symbols-outlined">receipt_long</span>
    </div>
</template>

<style scoped>
  .fab {
    background: var(--accent);
    color: white;
    font-size: 14px;
    font-weight: 700;
    display: flex;
    gap: 8px;
    justify-content: center;
    padding: 10px 0;
    border-radius: 12px;
    align-items: center;
    width: 100%;
  }

  .fab-icon {
    margin: 16px 0;
  }

  @media (min-width: 768px) {
    .fab {
      max-width: 500px;
      margin: auto;
    }
  }
</style>
