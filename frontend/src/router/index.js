import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import CreateInvoice from '../views/CreateInvoice.vue'
import EditInvoice from '../views/EditInvoice.vue'
import Invoice from '../views/Invoice.vue'
import Documentation from '../views/Documentation.vue'
import Account from '../views/Account.vue'
import Logout from '../views/Logout.vue'
import Login from '../views/Login.vue'
import NotFound from '../views/NotFound.vue'
import Error from '../views/Error.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/invoices/new',
      name: 'createInvoice',
      component: CreateInvoice
    },
    {
      path: '/invoices/:id',
      name: 'invoice',
      component: Invoice
    },
    {
      path: '/invoices/:id/edit',
      name: 'editInvoice',
      component: EditInvoice
    },
    {
      path: '/docs',
      name: 'documentation',
      component: Documentation
    },
    {
      path: '/account',
      name: 'account',
      component: Account
    },
    {
      path: '/account/logout',
      name: 'logout',
      component: Logout
    },
    {
      path: '/account/login',
      name: 'login',
      component: Login
    },
    { path: '/error', 
      name: "error",
      component: Error
    },
    { path: '/:pathMatch(.*)*', 
      name: "notFound",
      component: NotFound
    },
  ]
})

export default router
