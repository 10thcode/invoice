<script setup>
  import { ref } from 'vue'
  import Button from "../components/Button.vue"

  const invoice = JSON.parse(localStorage.getItem("invoice"))
  const props = defineProps(["charge"])
  const emit = defineEmits(["closeDialog"])
  const description = ref(props.charge.description)
  const percentage = ref(props.charge.percentage)

  function calculate () {
    const subTotal = Number(invoice.subTotal)
    let totalPercentage = 0
    let totalCharge = 0

    for (const charge of invoice.charges) {
      totalPercentage += charge.percentage
    }

    totalCharge = (totalPercentage / 100) * subTotal
    invoice.totalAmount = totalCharge + subTotal
  }

  function save() {
    for (const invoiceCharge of invoice.charges) {
      if (invoiceCharge.id === props.charge.id) {
        invoiceCharge.description = description.value
        invoiceCharge.percentage = percentage.value
        calculate()
        localStorage.setItem("invoice", JSON.stringify(invoice))
      }
    }

    emit('closeDialog')
  }

  function cancel() {
    emit('closeDialog',)
  }

  function remove() {
    for (const invoiceCharge of invoice.charges) {
      if (invoiceCharge.id === props.charge.id) {
        const index = invoice.charges.indexOf(invoiceCharge)
        invoice.charges.splice(index, 1)
        calculate()

        localStorage.setItem("invoice", JSON.stringify(invoice))
      }
    }

    emit('closeDialog')
  }
</script>

<template>
  <div class="dialog-container">
    <div class="title">Edit extra charge</div>
    <div class="form">
      <div class="field">
        <label for="description">Description</label>
        <input
          id="description"
          v-model="description"
          type="text"
          placeholder="eg. VAT"
        >
      </div>
      <div class="field">
        <label for="percentage">Percentage</label>
        <input
          id="percentage"
          v-model="percentage"
          type="number"
          placeholder="eg. 15"
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
