<script setup>
  import Collapsible from "../components/Collapsible.vue"
  import { ref, watch } from 'vue'

  let invoice = JSON.parse(localStorage.getItem("invoice"))
  let cache = JSON.parse(localStorage.getItem("cache"))
  const name = ref(invoice.business.name)
  const description = ref(invoice.business.description)
  const address = ref(invoice.business.address)
  const phone = ref(invoice.business.phone)

  watch(
    [name, description, address, phone],
    ([newName, newDescription, newAddress, newPhone]) => {
      invoice = JSON.parse(localStorage.getItem("invoice"))
      cache = JSON.parse(localStorage.getItem("cache"))
      const business = { 
        "name": newName,
        "description": newDescription,
        "address": newAddress,
        "phone": newPhone
      }
      invoice.business = business
      cache.business = business
      localStorage.setItem("cache", JSON.stringify(cache))
      localStorage.setItem("invoice", JSON.stringify(invoice))
  });
</script>

<template>
  <Collapsible
    leadingIcon="business"
    title="Business Details"
  >
  <div class="form">
    <div class="field">
      <label for="businessName" >Name</label>
      <input
        v-model="name"
        id="businessName"
        type="text"
        placeholder="eg. Black Genius Company LTD"
      >
    </div>
    <div class="field">
      <label for="businessDescription" >Description</label>
      <input
        v-model="description"
        id="businessDescription"
        type="text"
        placeholder="eg. We provide software solutions for businesses and individuals"
      >
    </div>
    <div class="field">
      <label for="businessAddress">Address</label>
      <input
        v-model="address"
        id="businessAddress"
        type="text"
        placeholder="eg. 221B Baker Street, Blackville"
      >
    </div>
    <div class="field">
      <label for="businessPhone">Phone</label>
      <input
        v-model="phone"
        id="businessPhone"
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
