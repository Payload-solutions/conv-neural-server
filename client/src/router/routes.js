import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)


const routes = [
    {
        path:'/',
        component:() => import('../views/Home.vue'),
        name: "home"
    },
    {
        path:'/image-train',
        component:() => import('../components/ImageTrain.vue'),
        name: "image-train"
    },
    {
        path:'/planet',
        component:() => import('../components/PlanetChart.vue'),
        name: "planet"
    },
    {
        path:'/stats',
        component:() => import('../components/Statistics.vue'),
        name: "stats"
    },
    {
        path:'*',
        component: ()=> import('../views/NotFound.vue')
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router;
