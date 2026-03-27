<template>
  <div>
    <el-card>
      <template #header>
        <div style="display: flex; justify-content: space-between; align-items: center">
          <span>消费记录管理</span>
          <el-button type="primary" @click="dialogVisible = true">新增消费</el-button>
        </div>
      </template>
      <el-table :data="tableData" stripe>
        <el-table-column prop="id" label="ID" width="80" />
        <el-table-column prop="member.name" label="会员" />
        <el-table-column prop="product_name" label="商品" />
        <el-table-column prop="amount" label="金额" width="100" />
        <el-table-column prop="quantity" label="数量" width="80" />
        <el-table-column prop="consume_time" label="消费时间" width="180" />
        <el-table-column prop="remark" label="备注" />
      </el-table>
    </el-card>

    <el-dialog v-model="dialogVisible" title="新增消费记录" width="500px">
      <el-form :model="form" label-width="80px">
        <el-form-item label="会员">
          <el-select v-model="form.member_id" style="width: 100%">
            <el-option v-for="m in members" :key="m.id" :label="m.name" :value="m.id" />
          </el-select>
        </el-form-item>
        <el-form-item label="商品名称">
          <el-input v-model="form.product_name" />
        </el-form-item>
        <el-form-item label="金额">
          <el-input-number v-model="form.amount" :min="0" style="width: 100%" />
        </el-form-item>
        <el-form-item label="数量">
          <el-input-number v-model="form.quantity" :min="1" />
        </el-form-item>
        <el-form-item label="备注">
          <el-input v-model="form.remark" type="textarea" />
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="handleSave">保存</el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { consumptionsApi, membersApi } from '../api'
import { ElMessage } from 'element-plus'

const tableData = ref([])
const members = ref([])
const dialogVisible = ref(false)
const form = ref({
  member_id: null,
  product_name: '',
  amount: 0,
  quantity: 1,
  remark: ''
})

const loadData = async () => {
  const [consRes, memRes] = await Promise.all([consumptionsApi.getAll(), membersApi.getAll()])
  tableData.value = consRes.data
  members.value = memRes.data
}

const handleSave = async () => {
  await consumptionsApi.create(form.value)
  dialogVisible.value = false
  loadData()
  ElMessage.success('操作成功')
}

onMounted(loadData)
</script>
