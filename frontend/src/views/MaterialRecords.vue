<template>
  <div>
    <el-card>
      <template #header>
        <div style="display: flex; justify-content: space-between; align-items: center">
          <span>物品记录管理</span>
          <el-button type="primary" @click="dialogVisible = true">新增记录</el-button>
        </div>
      </template>
      <el-table :data="tableData" stripe>
        <el-table-column prop="id" label="ID" width="80" />
        <el-table-column prop="material.name" label="物品" />
        <el-table-column prop="operation_type" label="类型" width="100">
          <template #default="{ row }">
            <el-tag :type="row.operation_type === 'in' ? 'success' : 'warning'">
              {{ row.operation_type === 'in' ? '入库' : '出库' }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="quantity" label="数量" width="100" />
        <el-table-column prop="operator" label="经手人" width="120" />
        <el-table-column prop="record_time" label="时间" width="180" />
        <el-table-column prop="remark" label="备注" />
      </el-table>
    </el-card>

    <el-dialog v-model="dialogVisible" title="新增物品记录" width="500px">
      <el-form :model="form" label-width="80px">
        <el-form-item label="物品">
          <el-select v-model="form.material_id" style="width: 100%">
            <el-option v-for="m in materials" :key="m.id" :label="m.name" :value="m.id" />
          </el-select>
        </el-form-item>
        <el-form-item label="操作类型">
          <el-select v-model="form.operation_type" style="width: 100%">
            <el-option label="入库" value="in" />
            <el-option label="出库" value="out" />
          </el-select>
        </el-form-item>
        <el-form-item label="数量">
          <el-input-number v-model="form.quantity" :min="1" style="width: 100%" />
        </el-form-item>
        <el-form-item label="经手人">
          <el-input v-model="form.operator" />
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
import { materialRecordsApi, materialsApi } from '../api'
import { ElMessage } from 'element-plus'

const tableData = ref([])
const materials = ref([])
const dialogVisible = ref(false)
const form = ref({ material_id: null, operation_type: 'in', quantity: 1, operator: '', remark: '' })

const loadData = async () => {
  const [recRes, matRes] = await Promise.all([materialRecordsApi.getAll(), materialsApi.getAll()])
  tableData.value = recRes.data
  materials.value = matRes.data
}

const handleSave = async () => {
  try {
    await materialRecordsApi.create(form.value)
    dialogVisible.value = false
    loadData()
    ElMessage.success('操作成功')
  } catch (e) {
    ElMessage.error(e.response?.data?.detail || '操作失败')
  }
}

onMounted(loadData)
</script>
