<script setup>
  import { ref } from "vue"
  import Button from "../components/Button.vue"

  const invoice = JSON.parse(localStorage.getItem("invoice"))
  const props = defineProps(["item"])
  const emit = defineEmits(["closeDialog"])
  const description = ref(props.item.description)
  const quantity = ref(props.item.quantity)
  const rate = ref(props.item.rate)

  function calculate () {
    let subTotal = 0 
    let totalPercentage = 0
    let totalCharge = 0

    for (const item of invoice.items) {
      subTotal += (item.quantity * item.rate)
    }

    for (const charge of invoice.charges) {
      totalPercentage += charge.percentage
    }

    totalCharge = (totalPercentage / 100) * subTotal
    invoice.subTotal = subTotal
    invoice.totalAmount = totalCharge + subTotal
  }

  function save() {
    for (const invoiceItem of invoice.items) {
      if (invoiceItem.id === props.item.id) {
        invoiceItem.description = description.value
        invoiceItem.quantity = quantity.value || 1
        invoiceItem.rate = rate.value
        calculate()
        localStorage.setItem("invoice", JSON.stringify(invoice))
      }
    }

    emit('closeDialog')
  }

  function cancel() {
    emit('closeDialog')
  }

  function remove() {
    for (const invoiceItem of invoice.items) {
      if (invoiceItem.id === props.item.id) {
        const index = invoice.items.indexOf(invoiceItem)
        invoice.items.splice(index, 1)
        calculate()
        localStorage.setItem("invoice", JSON.stringify(invoice))
      }
    }

    emit('closeDialog')
  }
</script>

<template>
  <div class="dialog-container">
    <div class="title">Edit item</div>
    <div class="form">
      <div class="field">
        <label for="description">Description</label>
        <input
          id="description"
          v-model="description"
          type="text"
          placeholder="eg. Apple juice"
        >
      </div>
      <div class="field">
        <label for="quantity">Quantity</label>
        <input
          id="quantity"
          v-model="quantity"
          type="number"
          placeholder="eg. 10"
        >
      </div>
      <div class="field">
        <label for="rate">Unit price</label>
        <input
          id="rate"
          v-model="rate"
          type="number"
          placeholder="eg: 5.99"
        >
      </div>
    </div>
    <div class="action-buttons">
      <button @click="cancel" type="button">Cancel</button>
      <button @click="remove" type="button">Remove</button>
      <button @click="save" type="button">Save</button>
    </div>
  </div>
</template>

<style scoped>
  input {
    font-size: 14px;
    background: none;
    border: 0;
    padding: 8px 0;
  }

  label {
    font-size: 10px;
    font-weight: 700;
  }

  .field {
    display: flex;
    flex-direction: column;
    gap: 8px;
    background: var(--tertiary-container);
    padding: 16px;
    border-radius: 8px;
    border-bottom: 2px solid var(--outline);
  }

  .form {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .title {
    font-size: 24px;
    font-weight: 400;
  }

  .dialog-container {
    display: flex;
    flex-direction: column;
    gap: 24px;
    background: var(--tertiary);
    color: var(--on-tertiary);
    border-radius: 24px;
    padding: 24px;
    max-width: 350px;
  }

  .action-buttons {
    display: flex;
    width: 100%;
    justify-content: right;
  }

  button {
    padding: 16px;
    background: none;
    color: var(--accent);
    font-weight: 700;
    font-size: 14px;
  }
</style>
