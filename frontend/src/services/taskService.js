import { authHeaders } from './authService.js'

export async function getTasks() {
  const res = await fetch('/tasks/', { headers: authHeaders() })
  if (!res.ok) throw new Error('Erro ao carregar tarefas')
  return res.json()
}

export async function createTask(name, description = '') {
  const res = await fetch('/tasks/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', ...authHeaders() },
    body: JSON.stringify({ name, description })
  })
  if (!res.ok) throw new Error('Erro ao criar tarefa')
  return res.json()
}

export async function updateTask(id, data) {
  const res = await fetch(`/tasks/${id}`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json', ...authHeaders() },
    body: JSON.stringify(data)
  })
  if (!res.ok) throw new Error('Erro ao atualizar tarefa')
  return res.json()
}

export async function deleteTask(id) {
  const res = await fetch(`/tasks/${id}`, {
    method: 'DELETE',
    headers: authHeaders()
  })
  if (!res.ok) throw new Error('Erro ao deletar tarefa')
  return res.json()
}
