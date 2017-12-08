<template>
    <div id="app">
        <djws-navbar></djws-navbar>
        <djws-shiksha-content></djws-shiksha-content>
        <djws-footer></djws-footer>
    </div>
</template>

<script>
    import DjWebShikshaNavBar from './component/DjWebShiksha/DjWebShikshaNavBar.vue'
    import DjWebShikshaContent from './component/DjWebShiksha/DjWebShikshaContent.vue'
    import DjWebShikshaFooter from './component/DjWebShiksha/DjWebShikshaFooter.vue'

    export default {
        name: 'app',
        components: {
            'djws-navbar': DjWebShikshaNavBar,
            'djws-shiksha-content': DjWebShikshaContent,
            'djws-footer': DjWebShikshaFooter
        },
    }
</script>
<style lang="scss">
    #app {
        color: lightgreen;
        font-size: 1rem;
    }
</style>
