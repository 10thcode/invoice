<script setup>
  import PageTitle from '../components/PageTitle.vue'
  import Hero from '../components/Hero.vue'
  import ActionButton from '../components/ActionButton.vue'
  import InvoiceCard from '../components/InvoiceCard.vue'
  import Loading from '../components/Loading.vue'
  import { RouterLink, useRouter } from 'vue-router'
  import { ref, watch, onMounted } from "vue"
  import { useAuth0 } from '@auth0/auth0-vue'

  const router = useRouter()
  const { getAccessTokenSilently, isAuthenticated } = useAuth0()
  const search = ref("")
  const message = ref("No invoice created.")
  const isLoading = ref(false)

  if (!localStorage.getItem("invoices")) {
    localStorage.setItem("invoices", "[]")
  }

  if (!localStorage.getItem("cache")) {
    const cache = {
      "currency": "",
      "business": {}
    }
    localStorage.setItem("cache", JSON.stringify(cache))
  }

  const allInvoices = JSON.parse(localStorage.getItem("invoices"))
  const invoices = ref(allInvoices)

  watch(isAuthenticated, async (newValue) => {
    if (isAuthenticated.value) {
      isLoading.value = true;
      try {
        const token = await getAccessTokenSilently()
        const response = await fetch(`${import.meta.env.VITE_API_URL}/api/v1/invoices/`, {
          method: "GET",
          headers: {
            Authorization: 'Bearer ' + token
          }
        });
        if (!response.ok) {
          throw new Error("Server error")
        }

        const data = await response.json();
        localStorage.setItem("invoices", JSON.stringify(data))
        invoices.value = JSON.parse(localStorage.getItem("invoices"))
      } catch (error) {
        router.push('/error')
      } finally {
        isLoading.value = false;
      }
    }
  });

  watch([search], ([newSearch]) => {
    invoices.value = []
    for (const invoice of allInvoices) {
      if (invoice.id.startsWith(newSearch)) {
        invoices.value.push(invoice) 
      } 
    }
    message.value = "No invoice found"
  })
</script>

<template>
  <PageTitle>Home</PageTitle>
  <Hero />
  <Loading v-show="isLoading" />
  <section class="fab-section">
    <RouterLink to="/invoices/new">
      <ActionButton />
    </RouterLink>
  </section>
  <section class="invoices-section">
    <div class="section-title">All invoices</div>
    <input
      v-model="search"
      class="search-bar"
      type="search"
      placeholder="Search by invoice number">
    <div v-if="invoices.length" class="card-list">
        <InvoiceCard 
          v-for="invoice in invoices"
          @click="$router.push(`/invoices/${invoice.id}`)"
          :invoiceNumber="invoice.id"
          :customerName="invoice.customer.name"
          :date="invoice.datetime"
          :subTotal="invoice.totalAmount"
          :currency="invoice.currency"
        />
    </div>
    <div v-else class="info">{{ message }}</div>
  </section>
</template>

<style scoped>
  .search-bar {
    border: 0;
    background: var(--tertiary);
    color: var(--on-tertiary);
    border-radius: 100px;
    padding: 16px 24px;
    font-size: 16px;
    letter-spacing: 0.5px;
    width: 100%;
  }

  .fab-section {
    padding: 32px 16px;
  }

  .invoices-section {
    padding: 0 16px;
    display: flex;
    flex-direction: column;
    gap: 32px;
  }

  .section-title {
    font-size: 24px;
    font-weight: 300;
  }

  .card-list {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
  }

  @media (min-width: 640px) {
    .fab-section {
      padding: 32px;
    }

    .invoices-section {
      padding: 0 32px; 
    }
  }

  @media (min-width: 768px) {
    .card-list {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
    }

    .invoices-section {
      padding: 0 64px; 
    }

    .search-bar {
      max-width: 500px;
      margin: auto;
    }

    .section-title {
      text-align: center;
    }
  }

  @media (min-width: 1024px) {
    .card-list {
      grid-template-columns: repeat(3, 1fr);
    }

    .invoices-section {
      padding: 0 128px; 
    }
  }

  .invoices-section {
    padding-bottom: 64px;
  }
</style>
