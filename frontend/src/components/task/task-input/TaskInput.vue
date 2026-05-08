<template>
  <div class="add-container">
    <div class="add-wrapper">
      <div class="add-main">
        <input
          v-model="name"
          type="text"
          placeholder="O que precisa ser feito?"
          @keyup.enter="submit"
          aria-label="Nome da tarefa"
        />
      </div>
      <div class="add-desc">
        <textarea
          ref="descRef"
          v-model="description"
          placeholder="Detalhes, notas ou contexto..."
          rows="1"
          @input="autoResize"
          aria-label="Descrição da tarefa"
        ></textarea>
      </div>
      <div class="add-footer">
        <button @click="submit">Adicionar</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, nextTick } from 'vue'

const emit = defineEmits(['add'])
const name = ref('')
const description = ref('')
const descRef = ref(null)

function autoResize() {
  const el = descRef.value
  if (!el) return
  el.style.height = 'auto'
  el.style.height = el.scrollHeight + 'px'
}

function submit() {
  const trimmed = name.value.trim()
  if (trimmed) {
    emit('add', trimmed, description.value.trim())
    name.value = ''
    description.value = ''
    nextTick(() => {
      if (descRef.value) descRef.value.style.height = 'auto'
    })
  }
}
</script>

<style scoped src="./task-input.css"></style>
