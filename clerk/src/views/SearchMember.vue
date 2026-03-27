<template>
  <div>
    <el-card>
      <el-input v-model="keyword" placeholder="输入会员姓名或手机号搜索" clearable @change="search">
        <template #append>
          <el-button :icon="Search" @click="search" />
        </template>
      </el-input>
    </el-card>
    
    <el-card v-if="member" style="margin-top: 20px">
      <template #header>
        <span>会员信息</span>
      </template>
      <el-descriptions :column="2" border>
        <el-descriptions-item label="姓名">{{ member.name }}</el-descriptions-item>
        <el-descriptions-item label="手机号">{{ member.phone }}</el-descriptions-item>
        <el-descriptions-item label="会员等级">{{ member.level }}</el-descriptions-item>
        <el-descriptions-item label="积分">{{ member.points }}</el-descriptions-item>
      </el-descriptions>
    </el-card>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { Search } from '@element-plus/icons-vue'
import { membersApi } from '../api'
import { ElMessage } from 'element-plus'

const keyword = ref('')
const member = ref(null)

const search = async () => {
  if (!keyword.value) return
  const res = await membersApi.getAll()
  const found = res.data.find(m => 
    m.name.includes(keyword.value) || m.phone.includes(keyword.value)
  )
  if (found) {
    member.value = found
  } else {
    member.value = null
    ElMessage.info('未找到该会员')
  }
}
</script>
