<script setup>
  import PageTitle from "../components/PageTitle.vue"
  import Button from "../components/Button.vue"
  import Loading from '../components/Loading.vue'
  import { useRoute, useRouter } from "vue-router"
  import { useAuth0 } from '@auth0/auth0-vue'
  import { ref } from "vue"

  const { isAuthenticated, getAccessTokenSilently } = useAuth0()
  const route = useRoute()
  const router = useRouter()
  const invoices = JSON.parse(localStorage.getItem("invoices"))
  const isLoading = ref(false)
  let invoice

  for (const item of invoices) {
    if (item.id === route.params.id) {
      invoice = item
    }
  }

  async function deleteInvoice () {
    for (const item of invoices) {
      if (item.id === route.params.id) {
        const index = invoices.indexOf(item)
        invoices.splice(index, 1)
        if (await isAuthenticated.value) {
          isLoading.value = true;
          try {
            const token = await getAccessTokenSilently();
            const response = await fetch(`${import.meta.env.VITE_API_URL}/api/v1/invoices/${route.params.id}`, {
              method: "DELETE",
              headers: {
                Authorization: 'Bearer ' + token
              },
            });
            if (!response.ok) {
              throw new Error("Server error")
            }
          } catch (error) {
            router.push("/error")
          } finally {
            isLoading.value = false;
          }
        }
      }
    }
    localStorage.setItem("invoices", JSON.stringify(invoices))
    router.push("/")
  }

  function edit () {
    router.push(`/invoices/${invoice.id}/edit`)
  }

  function download () {
    const element = document.getElementById('element-to-print');
    const opt = {
      margin:       1,
      filename:     `INV-${invoice.id}.pdf`,
      image:        { type: 'jpeg', quality: 0.98 },
      html2canvas:  { scale: 2 },
      jsPDF:        {
        unit: 'in',
        format: 'letter',
        orientation: 'portrait'
      }
    }

    try {
      html2pdf(element, opt);
    } catch (error) {
      router.push("/error")
    }
  }
</script>

<template>
  <PageTitle>Invoice</PageTitle>
  <Loading v-show="isLoading" />
  <div class="grid-container">
    <div id="element-to-print" class="grid-container-item">
      <div class="details-container">
        <div class="invoice">INVOICE</div>
        <div class="details">
          <div class="icon">
            <span class="material-symbols-outlined">receipt_long</span>
          </div>
          <div class="text">
            <div class="title">{{ invoice.id }}</div>
            <div>{{ invoice.datetime }}</div>
          </div>
        </div>
        <div v-show="Object.keys(invoice.business).length !== 0" class="details">
          <div class="icon">
            <span class="material-symbols-outlined">business</span>
          </div>
          <div class="text">
            <div class="title">
              {{ invoice.business.name }}
            </div>
            <div>{{ invoice.business.description }}</div>
            <div>{{ invoice.business.phone }}</div>
            <div>{{ invoice.business.address }}</div>
          </div>
        </div>
        <div v-show="Object.keys(invoice.customer).length !== 0" class="details">
          <div class="icon">
            <span class="material-symbols-outlined">person_outline</span>
          </div>
          <div class="text">
            <div class="title">{{ invoice.customer.name }}</div>
            <div>{{ invoice.customer.phone }}</div>
            <div>{{ invoice.customer.address }}</div>
          </div>
        </div>
      </div>
      <div class="container">
        <div class="sub-heading">Items</div>
        <div v-if="invoice.items.length" class="list-container">
          <div
            v-for="item in invoice.items"
            class="list-item">
            <div class="list-item-icon">
              <span class="material-symbols-outlined">local_mall</span>
            </div>
            <div class="list-item-details">
              <div class="bold">{{ item.description }}</div>
              <div>Quantity: <span class="bold">{{ item.quantity }}</span></div>
              <div>Unit price:
                <span class="bold">
                  {{ Number(item.rate).toFixed(2) }} {{invoice.currency}}
                </span>
              </div>
              <div>Total:
                <span class="bold">
                  {{ (item.rate * item.quantity).toFixed(2) }} {{invoice.currency}}
                </span>
              </div>
            </div>
          </div>
        </div>
        <div v-else class="info">No item</div>
      </div>
      <div class="sub-total">
        <span class="material-symbols-outlined">equal</span>
        <div class="text">
          {{ (invoice.subTotal).toFixed(2) }} {{ invoice.currency }}
        </div>
      </div>
      <div class="container">
        <div class="sub-heading">Extra charges</div>
        <div v-if="invoice.charges.length" class="list-container">
          <div
            v-for="charge in invoice.charges"
            class="list-item">
            <div class="list-item-icon">
              <span class="material-symbols-outlined">percent</span>
            </div>
            <div class="list-item-details">
              <div class="bold">{{ charge.description }}</div>
              <div>Percentage: <span class="bold">{{ charge.percentage }}</span></div>
              <div>Total:
                <span class="bold">
                  {{ ((charge.percentage / 100) * invoice.subTotal).toFixed(2) }}
                  {{ invoice.currency }}
                </span>
              </div>
            </div>
          </div>
        </div>
        <div v-else class="info">No extra charge</div>
      </div>
      <div class="sub-total">
        <span class="material-symbols-outlined">calculate</span>
        <div class="text">
          {{ (invoice.totalAmount).toFixed(2) }} {{invoice.currency}}
        </div>
      </div>
    </div>
    <div class="grid-container-item">
      <div class="action-buttons">
        <Button @click="deleteInvoice" bg="none">Delete</Button>
        <Button @click="edit" bg="none">Edit</Button>
        <Button @click="$router.push('/')" bg="none">Done</Button>
        <Button @click="download" bg="green">Download</Button>
      </div>
    </div>
  </div>
</template>

<style scoped>
  .invoice {
    font-size: 40px;;
  }

  .list-item {
    background: white;
  }

  .sub-total {
    font-size: 24px;
    font-weight: 700;
    display: flex;
    padding: 32px 16px;
    gap: 16px;
    background: none;
    align-items: center;
    letter-spacing: 0.5px;
    
  }

  .action-buttons {
    margin: 32px 16px;
    display: flex;
    gap: 32px;
    justify-content: right;
  }

  .amount {
    font-weight: 700;
    font-size: 24px;
  }

  .sub-heading {
    font-size: 24px;
    font-weight: 300;
    margin-bottom: 8px;
  }

  .invoice-container {
    background: var(--secondary);
    margin: 16px;
    border: 1px solid var(--outline);
    border-radius: 12px;
  }

  .invoice-header {
    font-size: 36px;
    font-weight: 700;
    padding: 32px 16px;
    border-bottom: 1px solid var(--outline);
  }

  .details-container {
    display: flex;
    flex-direction: column;
    padding: 32px 16px;
    gap: 32px;
  }

  .details {
    display: flex;
    gap: 16px;
  }

  .text {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .title {
    font-weight: 700;
  }

  .warning-section {
    margin-top: 32px;
    padding: 16px;
  }

  .info {
    margin: 0;
  }

  .list-container {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  @media (min-width: 640px) {
    .grid-container {
      padding: 0 16px;
    }
  }

  @media (min-width: 768px) {
    .grid-container {
      padding: 0 48px;
    }

    .details-container {
      display: grid;
      grid-template-columns: 1fr 1fr;
      grid-template-rows: 3fr 5fr;
    }

    .list-container {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
    }
  }

  @media (min-width: 1024px) {
    .grid-container {
      padding: 0 112px;
      display: grid;
      grid-template-columns: 4fr 1fr;
      gap: 64px
    }

    .none {
      padding: 16px 24px;
      color: var(--accent);
      background: white;
      border: 1px solid var(--accent);
    }

    .action-buttons {
      flex-direction: column-reverse;
    }
  }
</style>
