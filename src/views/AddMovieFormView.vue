<script setup>
import MovieForm from '../components/MovieForm.vue';

</script>

<template>
    <main class="container">
        <MovieForm @add-movie="updateMovie"/>
        
    </main>
</template>
