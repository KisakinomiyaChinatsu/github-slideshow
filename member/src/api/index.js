import axios from 'axios'

const api = axios.create({
  baseURL: '/api'
})

export const membersApi = {
  getAll: () => api.get('/members'),
  getByPhone: (phone) => api.get('/members')
}

export const consumptionsApi = {
  getAll: (params) => api.get('/consumptions', { params })
}
