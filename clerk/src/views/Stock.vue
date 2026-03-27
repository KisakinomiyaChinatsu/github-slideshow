<template>
  <div>
    <el-card>
      <template #header>
        <span>库存查询</span>
      </template>
      <el-table :data="products" stripe>
        <el-table-column prop="name" label="产品名称" />
        <el-table-column prop="category.name" label="类别" />
        <el-table-column prop="stock" label="库存" />
        <el-table-column prop="price" label="价格" />
      </el-table>
    </el-card>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { productsApi } from '../api'

const products = ref([])

onMounted(async () => {
  const res = await productsApi.getAll()
  products.value = res.data
})
</script>
