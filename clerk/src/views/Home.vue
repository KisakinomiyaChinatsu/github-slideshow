<template>
  <div>
    <el-card>
      <template #header>
        <h3>今日概览</h3>
      </template>
      <el-row :gutter="20">
        <el-col :span="8">
          <el-statistic title="会员总数" :value="stats.members" />
        </el-col>
        <el-col :span="8">
          <el-statistic title="订单总数" :value="stats.orders" />
        </el-col>
        <el-col :span="8">
          <el-statistic title="销售总额" :value="stats.sales" prefix="¥" />
        </el-col>
      </el-row>
    </el-card>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { membersApi, consumptionsApi } from '../api'

const stats = ref({ members: 0, orders: 0, sales: 0 })

onMounted(async () => {
  const [memRes, conRes] = await Promise.all([membersApi.getAll(), consumptionsApi.getAll()])
  stats.value.members = memRes.data.length
  stats.value.orders = conRes.data.length
  stats.value.sales = conRes.data.reduce((sum, c) => sum + c.amount, 0)
})
</script>
