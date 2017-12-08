<template>
    <div id="sitemap">
        <div class="post sitemap">
            <h2>Sitemap</h2>
            <ul>
                {% for obj in object_list%}
                <li><a href="{% url 'posts:list' %}">{{obj}}</a>- <i>{{obj.publish}}</i></li>
                {%endfor%}
            </ul>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'sitemap',
    }
</script>
<style lang="scss">

</style>
