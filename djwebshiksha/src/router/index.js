// import Vue from 'vue';
// import Router from 'vue-router'
// import App from '../App.vue'
// // import DjWebShikshaContent from '../components/DjWebShiksha/DjWebShikshaContent.vue'
// // import Sidebar from '../components/Sidebar.vue'
// // import MainContent from '../components/MainContent.vue'
//
// Vue.use(Router);
// export const routes = new Router({
//     routes: [
//         {
//             path: '/',
//             name: 'App',
//         }
//     ]
// })

const routes = [
    {
        name:'home',
        path: '/',
        component: require('../App.vue'),
    },
    {
        name:'sitemap',
        path: '/sitemap',
        component: require('../components/SiteMap.vue'),
    },
];