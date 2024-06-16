<script setup>
  import { ref } from "vue"
  import Collapsible from "../components/Collapsible.vue"
  import Button from "../components/Button.vue"
  import AddItemDialog from "../components/AddItemDialog.vue"
  import EditItemDialog from "../components/EditItemDialog.vue"

  const invoice = JSON.parse(localStorage.getItem("invoice"))
  const emit = defineEmits(["calculate"])
  defineProps(["currency"])

  const isAddDialogOpen = ref(false)
  const isEditDialogOpen = ref(false)
  const items = ref(invoice.items || [])
  let editItem = {}

  function openAddDialog() {
    isAddDialogOpen.value = !isAddDialogOpen.value
    document.body.style.overflow = "hidden"
  }

  function closeAddDialog() {
    items.value = JSON.parse(localStorage.getItem("invoice")).items
    isAddDialogOpen.value = !isAddDialogOpen.value
    document.body.style.overflow = "auto"
    emit("calculate")
  }

  function openEditDialog(item) {
    editItem = item
    isEditDialogOpen.value = !isEditDialogOpen.value
    document.body.style.overflow = "hidden"
  }

  function closeEditDialog() {
    items.value = JSON.parse(localStorage.getItem("invoice")).items
    isEditDialogOpen.value = !isEditDialogOpen.value
    document.body.style.overflow = "auto"
    emit("calculate")
  }
</script>

<template>
  <Collapsible
    leadingIcon="list_alt"
    title="Item List"
    :opened="true"
  >
    <div v-if="items.length" class="container">
      <div
        v-for="item in items"
        key="item.id"
        @click="openEditDialog(item)"
        class="list-item">
        <div class="list-item-icon">
          <span class="material-symbols-outlined">local_mall</span>
        </div>
        <div class="list-item-details">
          <div class="bold">{{ item.description }}</div>
          <div>Quantity: <span class="bold">{{ item.quantity }}</span></div>
          <div>
            Unit price:
            <span class="bold">
              {{ Number(item.rate).toFixed(2) }} {{currency}}
            </span>
          </div>
          <div>
            Total:
            <span class="bold">
              {{ (item.rate * item.quantity).toFixed(2) }} {{ currency }}
            </span>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="info">No item added to this invoice.</div>
    <div v-if="isEditDialogOpen" class="dialog">
      <EditItemDialog
        :item="editItem"
        class="item-dialog"
        @closeDialog="closeEditDialog"
      />
    </div>
    <Button
      @click="openAddDialog"
      class="add-button"
      leadingIcon="add"
      bg="none">
        Add item
    </Button>
    <div v-if="isAddDialogOpen" class="dialog">
      <AddItemDialog
        class="item-dialog"
        @closeDialog="closeAddDialog"
      />
    </div>
  </Collapsible>
</template>

<style scoped>
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
