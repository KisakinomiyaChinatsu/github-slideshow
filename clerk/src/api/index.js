import axios from 'axios'

const api = axios.create({
  baseURL: '/api'
})

export const membersApi = {
  getAll: () => api.get('/members'),
  getOne: (id) => api.get(`/members/${id}`),
  update: (id, data) => api.put(`/members/${id}`, data)
}

export const consumptionsApi = {
  getAll: (params) => api.get('/consumptions', { params }),
  create: (data) => api.post('/consumptions', data)
}

export const productsApi = {
  getAll: () => api.get('/products')
}

export const materialsApi = {
  getAll: () => api.get('/materials')
}

export const materialRecordsApi = {
  create: (data) => api.post('/material-records', data)
}
