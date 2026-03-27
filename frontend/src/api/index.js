import axios from 'axios'

const api = axios.create({
  baseURL: '/api'
})

export const membersApi = {
  getAll: () => api.get('/members'),
  create: (data) => api.post('/members', data),
  update: (id, data) => api.put(`/members/${id}`, data),
  delete: (id) => api.delete(`/members/${id}`)
}

export const consumptionsApi = {
  getAll: () => api.get('/consumptions'),
  create: (data) => api.post('/consumptions', data),
  getOne: (id) => api.get(`/consumptions/${id}`)
}

export const categoriesApi = {
  getAll: () => api.get('/categories'),
  create: (data) => api.post('/categories', data),
  update: (id, data) => api.put(`/categories/${id}`, data),
  delete: (id) => api.delete(`/categories/${id}`)
}

export const productsApi = {
  getAll: () => api.get('/products'),
  create: (data) => api.post('/products', data),
  update: (id, data) => api.put(`/products/${id}`, data),
  delete: (id) => api.delete(`/products/${id}`)
}

export const materialsApi = {
  getAll: () => api.get('/materials'),
  create: (data) => api.post('/materials', data),
  update: (id, data) => api.put(`/materials/${id}`, data),
  delete: (id) => api.delete(`/materials/${id}`)
}

export const materialRecordsApi = {
  getAll: () => api.get('/material-records'),
  create: (data) => api.post('/material-records', data)
}
