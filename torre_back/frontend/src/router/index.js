import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Opportunities from '@/components/Opportunity/Opportunities'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Indez',
      component: Index
    },
    {
      path: '/opportunities',
      name: 'Opportunities',
      component: Opportunities
    }
    
  ],
  mode:'history'
})
