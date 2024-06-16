<script setup>
  import Button from "../components/Button.vue"
  import PageTitle from "../components/PageTitle.vue"
  import InvoiceDetails from "../components/InvoiceDetails.vue"
  import BusinessDetails from "../components/BusinessDetails.vue"
  import CustomerDetails from "../components/CustomerDetails.vue"
  import ItemList from "../components/ItemList.vue"
  import ExtraCharges from "../components/ExtraCharges.vue"
  import Loading from '../components/Loading.vue'
  import { useRouter } from "vue-router"
  import { ref, onMounted } from "vue"
  import { useAuth0 } from '@auth0/auth0-vue'

  const { isAuthenticated, getAccessTokenSilently } = useAuth0()
  const cache = JSON.parse(localStorage.getItem("cache"))
  const totalAmount = ref(0)
  const subTotal = ref(0)
  const currency = ref(cache.currency)
  const isLoading = ref(false)

  function uuid() {
    return "1080001000000000".replace(/[018]/g, c => (+c ^ crypto.getRandomValues(
      new Uint8Array(1))[0] & 15 >> +c / 4).toString(16)
    )
  }

  const invoice = JSON.stringify({
    "id": uuid(),
    "subTotal": 0,
    "totalAmount": 0,
    "currency": cache.currency,
    "customer": {},
    "business": cache.business,
    "items": [],
    "charges": [],
    "datetime": "",
    "lastModified": ""
  })
  localStorage.setItem("invoice", invoice)

  const router = useRouter();

  function changeCurrency() {
    currency.value = JSON.parse(localStorage.getItem("invoice")).currency
  }

  function calculate() {
    totalAmount.value = JSON.parse(localStorage.getItem("invoice")).totalAmount
    subTotal.value = JSON.parse(localStorage.getItem("invoice")).subTotal
  }

  async function submitForm() {
    const invoice = JSON.parse(localStorage.getItem("invoice"))
    const invoices = JSON.parse(localStorage.getItem("invoices"))
    const now = new Date()

    invoice.datetime = now.toLocaleString()
    invoice.lastModified = now.toLocaleString()
    invoices.unshift(invoice)
    localStorage.setItem("invoices", JSON.stringify(invoices))

    if (await isAuthenticated.value) {
      isLoading.value = true;
      try {
        const token = await getAccessTokenSilently();
        const response = await fetch(`${import.meta.env.VITE_API_URL}/api/v1/invoices/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: 'Bearer ' + token
          },
          body: JSON.stringify(invoice)
        });
        if (!response.ok) {
          throw new Error("Server error")
        }
        const data = await response.json();
      } catch (error) {
        router.push("/error") 
      } finally {
        isLoading.value = false;
      }
    }
    
    localStorage.removeItem("invoice")
    router.push(`/invoices/${invoice.id}`)
  }
</script>

<template>
  <PageTitle>Create Invoice</PageTitle>
  <Loading v-show="isLoading" />
  <div class="parrent-container">
    <div class="form-container">
      <div class="form-container-item">
        <InvoiceDetails @changeCurrency="changeCurrency"/>
        <BusinessDetails />
        <CustomerDetails />
      </div>
      <div class="form-container-item">
        <ItemList @calculate="calculate" :currency="currency"/>
        <div class="sub-total">
          <span class="material-symbols-outlined">equal</span>
          <div class="text">
            {{ (subTotal).toFixed(2) }} {{ currency }}
          </div>
        </div>
        <ExtraCharges
          @calculate="calculate"
          :currency="currency"
          :subTotal="subTotal"/>
        <div class="sub-total">
          <span class="material-symbols-outlined">calculate</span>
          <div class="text">
            {{ (totalAmount).toFixed(2) }} {{ currency }}
          </div>
        </div>
      </div>
    </div>
    <div class="action-buttons">
      <Button @click="$router.push('/')" bg="none">Cancel</Button>
      <Button @click="submitForm" bg="accent">Create</Button>
    </div>
  </div>
</template>

<style scoped>
  .action-buttons {
    display: flex;
    gap: 32px;
    margin: 32px 16px;
    justify-content: right;
  }

  .sub-total {
    display: flex;
    padding: 16px;
    gap: 16px;
    background: none;
    align-items: center;
    color: #4285F4;
    letter-spacing: 0.5px;
  }

  .text {
    width: 100%;
    text-align: left;
    font-size: 16px;
    font-weight: 700;
  }

  @media (min-width: 640px) {
    .form-container {
      padding: 0 16px;
    }
  }

  @media (min-width: 768px) {
    .form-container {
      padding: 0 48px;
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 32px;
    }

    .form-container-item {
      border: 1px solid var(--outline);
      margin-top: 32px;
      border-radius: 12px;
      padding: 16px;
    }

    .action-buttons {
      padding-right: 32px;
    }
  }

  @media (min-width: 1024px) {
    .action-buttons {
      padding-right: 0px;
    }

    .form-container {
      padding: 0;
    }

    .parrent-container {
      padding: 0 112px;
      display: grid;
      grid-template-columns: 4fr 1fr;
      gap: 32px
    }

    .action-buttons {
      flex-direction: column-reverse;
    }
  }
</style>
