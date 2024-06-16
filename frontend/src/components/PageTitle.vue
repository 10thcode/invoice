<template>
  <div class="page-title">
    <slot />
  </div>
</template>

<style scoped>
  .page-title {
    font-weight: 300;
    padding: 16px;
    font-size: 24px;
    background: var(--secondary);
  }

  @media (min-width: 640px) {
    .page-title {
      padding: 16px 32px;
    }
  }

  @media (min-width: 768px) {
    .page-title {
      padding: 16px 64px;
    }
  }

  @media (min-width: 1024px) {
    .page-title {
      padding: 16px 128px;
    }
  }
</style>
