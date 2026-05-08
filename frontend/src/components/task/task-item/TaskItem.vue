<template>
  <div class="task" :class="{ completed: task.completed, editing: isEditing, expanded: isExpanded }">
    <template v-if="isEditing">
      <div class="edit-form">
        <input
          ref="editInput"
          v-model="editName"
          class="edit-input"
          placeholder="Nome da tarefa"
          @keyup.enter="saveEdit"
          @keyup.escape="cancelEdit"
          aria-label="Editar nome da tarefa"
        />
        <textarea
          ref="editTextarea"
          v-model="editDesc"
          class="edit-textarea"
          placeholder="Adicione detalhes, notas ou contexto..."
          rows="2"
          @input="autoResizeEdit"
          aria-label="Editar descrição da tarefa"
        ></textarea>
        <div class="edit-actions">
          <button class="btn-save" @click="saveEdit" aria-label="Salvar edição">
            <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
            Salvar
          </button>
          <button class="btn-cancel" @click="cancelEdit" aria-label="Cancelar edição">
            <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
            Cancelar
          </button>
        </div>
      </div>
    </template>
    <template v-else>
      <div class="task-main" @click="isExpanded = !isExpanded" @dblclick="startEdit">
        <div class="task-header">
          <span class="task-name">{{ task.name }}</span>
        </div>
        <div v-if="isExpanded" class="task-description-wrapper">
          <p v-if="task.description" class="task-description">{{ task.description }}</p>
          <p v-else class="task-description task-description--empty">Sem descrição</p>
        </div>
      </div>
      <div class="actions" @click.stop>
        <button
          class="btn-action btn-complete"
          :class="{ checked: task.completed }"
          @click="$emit('complete', task.id)"
          :aria-label="task.completed ? 'Desmarcar como concluída' : 'Marcar como concluída'"
          :title="task.completed ? 'Desmarcar' : 'Concluir'"
        >
          <svg v-if="!task.completed" xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
          <svg v-else xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7v6h6"></path><path d="M21 17a9 9 0 0 0-9-9 9 9 0 0 0-6 2.3L3 13"></path></svg>
        </button>
        <button
          class="btn-action btn-edit"
          @click="startEdit"
          aria-label="Editar tarefa"
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg>
        </button>
        <button
          class="btn-action btn-delete"
          @click="$emit('delete', task.id)"
          aria-label="Deletar tarefa"
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>
        </button>
      </div>
    </template>
  </div>
</template>

<script setup>
import { ref, nextTick } from 'vue'

const props = defineProps({
  task: { type: Object, required: true }
})

const emit = defineEmits(['delete', 'complete', 'edit'])

const isEditing = ref(false)
const isExpanded = ref(false)
const editName = ref('')
const editDesc = ref('')
const editInput = ref(null)
const editTextarea = ref(null)

function autoResizeEdit() {
  const el = editTextarea.value
  if (!el) return
  el.style.height = 'auto'
  el.style.height = el.scrollHeight + 'px'
}

function startEdit() {
  editName.value = props.task.name
  editDesc.value = props.task.description || ''
  isEditing.value = true
  nextTick(() => {
    editInput.value?.focus()
    autoResizeEdit()
  })
}

function saveEdit() {
  const trimmedName = editName.value.trim()
  if (!trimmedName) return
  const data = {}
  if (trimmedName !== props.task.name) data.name = trimmedName
  const trimmedDesc = editDesc.value.trim()
  if (trimmedDesc !== (props.task.description || '')) data.description = trimmedDesc
  if (Object.keys(data).length) emit('edit', props.task.id, data)
  isEditing.value = false
}

function cancelEdit() {
  isEditing.value = false
}
</script>

<style scoped src="./task-item.css"></style>
