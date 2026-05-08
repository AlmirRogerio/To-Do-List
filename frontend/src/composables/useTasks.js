import { ref, onMounted } from 'vue'
import { getTasks, createTask, updateTask, deleteTask } from '../services/taskService.js'

export function sortTasks(tasks) {
  return [...tasks].sort((a, b) => {
    if (a.completed === b.completed) return 0
    return a.completed ? 1 : -1
  })
}

export function useTasks() {
  const tasks = ref([])
  const error = ref(null)

  async function loadTasks() {
    try {
      const data = await getTasks()
      tasks.value = sortTasks(data)
    } catch (e) {
      error.value = e.message
    }
  }

  async function addTask(name, description = '') {
    try {
      await createTask(name, description)
      await loadTasks()
    } catch (e) {
      error.value = e.message
    }
  }

  async function removeTask(id) {
    try {
      await deleteTask(id)
      tasks.value = tasks.value.filter(t => t.id !== id)
    } catch (e) {
      error.value = e.message
    }
  }

  async function toggleTask(id) {
    try {
      const task = tasks.value.find(t => t.id === id)
      await updateTask(id, { completed: !task?.completed })
      await loadTasks()
    } catch (e) {
      error.value = e.message
    }
  }

  async function editTask(id, data) {
    try {
      await updateTask(id, data)
      await loadTasks()
    } catch (e) {
      error.value = e.message
    }
  }

  onMounted(loadTasks)

  return { tasks, error, loadTasks, addTask, removeTask, toggleTask, editTask }
}
