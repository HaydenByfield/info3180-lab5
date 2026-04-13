<script setup>
import { onMounted, ref } from 'vue'

let movies = ref('')

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
    <ul class="movie-grid">
        <li v-for="movie in movies" :key="movie.m_id" class="movie-card">
            <img :src="'/uploads/' + movie.m_poster" class="movie-img" />

            <div class="movie-content">
                <h3>{{ movie.m_title }}</h3>
                <p>{{ movie.m_desc }}</p>
            </div>
        </li>
    </ul>
</template>

<style scoped>
.movie-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr); /* 2 per row */
    gap: 20px;
    list-style: none;
    padding: 0;
}

.movie-card {
    display: flex;
    gap: 15px;
    background: #ffffff;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    align-items: flex-start;
    transition: transform 0.2s ease;
}

.movie-card:hover {
    transform: translateY(-3px);
}

.movie-img {
    width: 120px;
    height: 160px;
    object-fit: cover;
    border-radius: 8px;
}

.movie-content {
    display: flex;
    flex-direction: column;
}

.movie-content h3 {
    margin: 0 0 8px 0;
    font-size: 18px;
    color: #333;
}

.movie-content p {
    margin: 0;
    font-size: 14px;
    color: #555;
}
</style>