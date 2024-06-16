<script setup>
  defineProps([
    "invoiceNumber", 
    "customerName",
    "date",
    "subTotal",
    "currency"
  ])
</script>

<template>
    <div class="card invioce-card">
      <div>
        <span class="material-symbols-outlined">receipt_long</span>
      </div>
      <div class="invioce-details">
        <div class="bold">{{ invoiceNumber }}</div>
        <div>{{ customerName }}</div>
        <div>{{ date }}</div>
        <div class="bold">{{ (subTotal).toFixed(2) }} {{ currency }}</div>
      </div>
    </div>
</template>

<style scoped>
  .card {
    cursor: pointer;
    display: flex;
    gap: 16px;
    background: var(--secondary);
    border-radius: 12px;
    border: 1px solid var(--outline);
    padding: 16px;
  }

  .bold {
    font-weight: 700;
  }

  .invioce-details {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  @media (max-width: 768px) {
    .card {
      width: 100%;
    }
  }
</style>
