import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Convert from '../views/Convert.vue'
import Contact from '../views/Contact.vue'
import Processing from '../views/Processing.vue'
import AfterRecognition from '../views/AfterRecognition.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/convert',
    name: 'Convert',
    component: Convert
  },
  {
    path: '/contact',
    name: 'Contact',
    component: Contact
  },
  {
    path: '/processing',
    name: 'Processing',
    component: Processing
  },
  {
    path: '/afterRecognition',
    name: 'AfterRecognition',
    component: AfterRecognition
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
