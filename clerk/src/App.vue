<template>
  <el-container style="height: 100vh">
    <el-header style="background: #409EFF; color: #fff; line-height: 60px">
      <div style="display: flex; justify-content: space-between; align-items: center">
        <h2 style="margin: 0">店员操作端</h2>
        <span>店员: {{ clerkName }}</span>
      </div>
    </el-header>
    <el-container>
      <el-aside width="200px" style="background: #f5f5f5">
        <el-menu :default-active="$route.path" router style="border: none">
          <el-menu-item index="/home">
            <el-icon><House /></el-icon>
            <span>首页</span>
          </el-menu-item>
          <el-menu-item index="/search-member">
            <el-icon><Search /></el-icon>
            <span>会员查询</span>
          </el-menu-item>
          <el-menu-item index="/new-consumption">
            <el-icon><ShoppingCart /></el-icon>
            <span>消费开单</span>
          </el-menu-item>
          <el-menu-item index="/stock">
            <el-icon><Box /></el-icon>
            <span>库存查询</span>
          </el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
        <router-view />
      </el-main>
    </el-container>
  </el-container>
</template>

<script setup>
import { ref } from 'vue'
import { House, Search, ShoppingCart, Box } from '@element-plus/icons-vue'

const clerkName = ref('店员001')
</script>
