<script setup>
  import { ref } from "vue"
  import Collapsible from "../components/Collapsible.vue"
  import Button from "../components/Button.vue"
  import AddExtraChargeDialog from "../components/AddExtraChargeDialog.vue"
  import EditExtraChargeDialog from "../components/EditExtraChargeDialog.vue"

  const invoice = JSON.parse(localStorage.getItem("invoice"))
  const emit = defineEmits(["calculate"])
  defineProps(["currency", "subTotal"])

  const isAddDialogOpen = ref(false)
  const isEditDialogOpen = ref(false)
  const charges = ref(invoice.charges || [])
  let editCharge = {}

  function openAddDialog() {
    isAddDialogOpen.value = !isAddDialogOpen.value
    document.body.style.overflow = "hidden"
  }

  function closeAddDialog() {
    charges.value = JSON.parse(localStorage.getItem("invoice")).charges
    isAddDialogOpen.value = !isAddDialogOpen.value
    document.body.style.overflow = "auto"
    emit("calculate")
  }

  function openEditDialog(charge) {
    editCharge = charge
    isEditDialogOpen.value = !isEditDialogOpen.value
    document.body.style.overflow = "hidden"
  }

  function closeEditDialog() {
    charges.value = JSON.parse(localStorage.getItem("invoice")).charges
    isEditDialogOpen.value = !isEditDialogOpen.value
    document.body.style.overflow = "auto"
    emit("calculate")
  }
</script>

<template>
  <Collapsible
    leadingIcon="attach_money"
    title="Extra Charges"
  >
    <div v-if="charges.length" class="container">
      <div
        v-for="charge in charges"
        key="charge.id"
        @click="openEditDialog(charge)"
        class="list-item">
        <div class="list-item-icon">
          <span class="material-symbols-outlined">percent</span>
        </div>
        <div class="list-item-details">
          <div class="bold">{{ charge.description }}</div>
          <div>
            Percentage: <span class="bold">{{ charge.percentage }}%</span>
          </div>
          <div>
            Total:
            <span class="bold">
              {{ ((charge.percentage / 100) * subTotal).toFixed(2) }}
              {{ currency }}
            </span>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="info">No extra charge added to this invoice.</div>
    <div v-if="isEditDialogOpen" class="dialog">
      <EditExtraChargeDialog
        :charge="editCharge"
        class="item-dialog"
        @closeDialog="closeEditDialog"
      />
    </div>
    <Button
      @click="openAddDialog"
      class="add-button"
      leadingIcon="add"
      bg="none">
        Add extra charge
    </Button>
    <div v-if="isAddDialogOpen" class="dialog">
      <AddExtraChargeDialog
        class="item-dialog"
        @closeDialog="closeAddDialog"
      />
    </div>
  </Collapsible>

</template>

<style>
  .dialog {
    position: fixed;
    top: 0;
    left: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
    width: 100%;
    background: var(--dialog-background); 
  }

  .item-dialog {
    width: 100%;
    margin: 32px;
  }

  .add-button {
    margin: 32px 0;
  }

  .info {
    margin-top: 32px;
  }

  .list-item {
    cursor: pointer;
    padding: 16px;
    display: flex;
    background: var(--secondary);
    border: 1px solid var(--outline);
    border-radius: 12px;
  }

  .list-item {
    padding: 16px;
    display: flex;
    background: var(--secondary);
    border: 1px solid var(--outline);
    border-radius: 12px;
    gap: 16px;
  }

  .list-item-details {
    display: flex;
    flex-direction: column;
    gap: 8px;
    font-size: 14px;
  }

  .bold {
    font-weight: 700;
  }

  .container {
    padding: 0 16px;
    display: flex;
    flex-direction: column;
    gap: 16px;
  }
</style>
