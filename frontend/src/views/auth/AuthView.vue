<template>
  <div class="auth-container">
    <div class="auth-card">
      <h1>Minhas <span>Tarefas</span></h1>
      <p class="auth-subtitle">{{ isLogin ? 'Entre na sua conta' : 'Crie sua conta' }}</p>

      <form @submit.prevent="submit" class="auth-form">
        <input
          v-if="!isLogin"
          v-model="name"
          type="text"
          placeholder="Seu nome"
          aria-label="Nome"
          required
        />
        <input
          v-model="email"
          type="email"
          placeholder="Email"
          aria-label="Email"
          required
        />
        <input
          v-model="password"
          type="password"
          placeholder="Senha"
          aria-label="Senha"
          required
          minlength="6"
        />
        <button type="submit" :disabled="loading">
          {{ loading ? 'Aguarde...' : isLogin ? 'Entrar' : 'Cadastrar' }}
        </button>
      </form>

      <p v-if="error" class="error">{{ error }}</p>

      <p class="auth-toggle">
        {{ isLogin ? 'Não tem conta?' : 'Já tem conta?' }}
        <a href="#" @click.prevent="toggleMode">
          {{ isLogin ? 'Cadastre-se' : 'Faça login' }}
        </a>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuth } from '../../composables/useAuth.js'
import { loginUser, registerUser } from '../../services/authService.js'

const router = useRouter()
const { setAuth } = useAuth()

const isLogin = ref(true)
const name = ref('')
const email = ref('')
const password = ref('')
const error = ref(null)
const loading = ref(false)

function toggleMode() {
  isLogin.value = !isLogin.value
  error.value = null
}

async function submit() {
  error.value = null
  loading.value = true
  try {
    const data = isLogin.value
      ? await loginUser(email.value, password.value)
      : await registerUser(name.value, email.value, password.value)
    setAuth(data)
    router.push('/')
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}
</script>

<style scoped src="./auth-view.css"></style>
