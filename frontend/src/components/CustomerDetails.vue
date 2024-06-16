<script setup>
  import Collapsible from "../components/Collapsible.vue"
  import { ref, watch } from 'vue'

  let invoice = JSON.parse(localStorage.getItem("invoice"))
  const customerName = ref(invoice.customer.name)
  const customerAddress = ref(invoice.customer.address)
  const customerPhone = ref(invoice.customer.phone)

  watch(
    [customerName, customerAddress, customerPhone],
    ([newName, newAddress, newPhone]) => {
      invoice = JSON.parse(localStorage.getItem("invoice"))
      const customer = { 
        "name": newName,
        "address": newAddress,
        "phone": newPhone
      }
      invoice.customer = customer;
      localStorage.setItem("invoice", JSON.stringify(invoice))
  });
</script>

<template>
  <Collapsible
    leadingIcon="person_outline"
    title="Customer Details"
  >
  <div class="form">
    <div class="field">
      <label for="customerName" >Name</label>
      <input
        v-model="customerName"
        id="customerName"
        type="text"
        placeholder="eg. Black Genius"
      >
    </div>
    <div class="field">
      <label for="customerAddress">Address</label>
      <input
        v-model="customerAddress"
        id="customerAddress"
        type="text"
        placeholder="eg. 221B Baker Street, Blackville"
      >
    </div>
    <div class="field">
      <label for="customerPhone">Phone</label>
      <input
        v-model="customerPhone"
        id="customerPhone"
        type="text"
        placeholder="eg. +233000000000"
      >
    </div>
  </div>
  </Collapsible>
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
    color: var(--on-tertiary);
    background: var(--tertiary);
    padding: 16px;
    border-radius: 8px;
    border-bottom: 2px solid var(--outline);
  }

  .form {
    display: flex;
    flex-direction: column;
    gap: 8px;
    padding: 16px;
  }
</style>
