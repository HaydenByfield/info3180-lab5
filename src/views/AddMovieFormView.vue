<script setup>
import MovieForm from '../components/MovieForm.vue';
import { onMounted, ref } from 'vue'

const movies = ref([])

onMounted(async () =>{
    try {
        let response = await fetch('/api/v1/movies')
        let data = await response.json()
        movies.value = data.movies
        console.log(data)
    } catch (error) {
        console.error(error);
    }
})

const updateMovie = (movie) => {
    movies.value.push(movie)
}
</script>

<template>
    <main class="container">
        <MovieForm @add-movie="updateMovie"/>
        
    </main>
</template>
