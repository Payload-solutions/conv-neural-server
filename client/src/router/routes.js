import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)


const routes = [
    {
        path:'/',
        component:() => import(/* webpackChunkName: "about" */ '../components/Home.vue'),
        name: "home"
    },
    {
        path:'/image-train',
        component:() => import(/* webpackChunkName: "about" */ '../components/ImageTrain.vue'),
        name: "image-train"
    },
    {
        path:'/planet',
        component:() => import(/* webpackChunkName: "about" */ '../components/PlanetChart.vue'),
        name: "planet"
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router;
