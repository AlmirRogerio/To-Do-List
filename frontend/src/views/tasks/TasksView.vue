<template>
  <div id="app">
    <header class="app-header">
      <div class="header-top">
        <div>
          <h1>Minhas <span>Tarefas</span></h1>
          <p>Olá, {{ user?.name }}!</p>
        </div>
        <button class="btn-logout" @click="handleLogout" aria-label="Sair">Sair</button>
      </div>
    </header>

    <TaskInput @add="addTask" />

    <div v-if="tasks.length" class="task-counter">
      <span>{{ pending }} pending</span>
      <span class="count">{{ tasks.length }} total</span>
    </div>

    <TransitionGroup name="task" tag="div" class="tasks-container">
      <TaskItem
        v-for="task in tasks"
        :key="task.id"
        :task="task"
        @delete="removeTask"
        @complete="toggleTask"
        @edit="editTask"
      />
    </TransitionGroup>

    <div v-if="!tasks.length" class="tasks-empty">
      Nenhuma tarefa ainda. Adicione uma acima.
    </div>

    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import TaskInput from '../../components/task/task-input/TaskInput.vue'
import TaskItem from '../../components/task/task-item/TaskItem.vue'
import { useTasks } from '../../composables/useTasks.js'
import { useAuth } from '../../composables/useAuth.js'

const router = useRouter()
const { user, logout } = useAuth()
const { tasks, error, addTask, removeTask, toggleTask, editTask } = useTasks()

const pending = computed(() => tasks.value.filter(t => !t.completed).length)

function handleLogout() {
  logout()
  router.push('/login')
}
</script>

<style src="./tasks-view.css"></style>
