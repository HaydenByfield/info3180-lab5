<script setup>
    import { ref, onMounted } from 'vue'
    // Using Composite API management
    const props = defineProps(['movies'])
    const emit = defineEmits(['add-movie'])
    let m_title = ref('')
    let m_desc = ref("")
    let m_poster = ref(null)
    let message = ref ('')
    let csrf_token = ref('')

    const getCsrfToken = async () => {
        try{
            let response = await fetch('/api/v1/csrf-token')
            let data = await response.json();
            csrf_token.value = data.csrf_token
            console.log(data)

        } catch(error){
            console.log(error)
        }
    }
    onMounted(() => {
        getCsrfToken();
    })
    const handleFile = (event) => {
       m_poster.value = event.target.files[0];
    };
    const saveMovie = async() => {
        let movieForm = document.getElementById('m-form')
        let formData = new FormData(movieForm);
        formData.append('m_title', m_title.value);
        formData.append('m_desc', m_desc.value);
        formData.append('m_poster', m_poster.value);
        try {
            let response = await fetch('/api/v1/movies',{
            method: 'POST',
            body: formData,
            headers:{
                'X-CSRFToken': csrf_token.value
            }
            });

            let data = await response.json();
            message.value = data.message;
            console.log(data)

            emit('add-movie', {m_title: data.m_title, m_desc: data.description, m_poster: data.m_poster})

            m_title.value = '';
            m_desc.value = '';
            m_poster.value = null;

        } catch (error) {
            console.error(error);
        }
    } 
</script>
<template>
    <div class="container">
        <form @submit.prevent="saveMovie" id="m-form">
            <div class="form-group">
                <label class="form-label">Movie Title</label>
                <input type="text" v-model="m_title" placeholder="Please enter a title" class="form-submit" required/>
            </div>

            <div class="form-group">
                <label class="form-label">Movie Description</label>
                <textarea v-model="m_desc" placeholder="Please enter a description" class="form-submit" required></textarea>
            </div>

            <div class="form-group">
                <label class="form-label">Movie Poster</label>
                <input type="file" @change="handleFile" class="form-submit" required/>
            </div>

            <button type="submit">Add Movie</button>
            <p v-if="message">{{ message }}</p>
        </form>
    </div>
</template>

<style scoped>
.container {
    max-width: 500px;
    margin: 40px auto;
    padding: 20px;
}

#m-form {
    display: flex;
    flex-direction: column;
    gap: 20px;
    background: #ffffff;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.form-group {
    display: flex;
    flex-direction: column;
}

.form-label {
    font-weight: 600;
    margin-bottom: 6px;
    color: #333;
}

.form-submit {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 8px;
    font-size: 14px;
    transition: border 0.2s ease, box-shadow 0.2s ease;
}

.form-submit:focus {
    border-color: #4CAF50;
    box-shadow: 0 0 5px rgba(76, 175, 80, 0.3);
    outline: none;
}

input[type="file"] {
    padding: 6px;
}

button {
    padding: 12px;
    background: #4CAF50;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 16px;
    cursor: pointer;
    transition: background 0.2s ease;
}

button:hover {
    background: #43a047;
}

p {
    text-align: center;
    font-size: 14px;
    color: #4CAF50;
}
</style>