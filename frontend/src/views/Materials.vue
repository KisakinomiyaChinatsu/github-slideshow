<template>
  <div>
    <el-card>
      <template #header>
        <div style="display: flex; justify-content: space-between; align-items: center">
          <span>物品信息管理</span>
          <el-button type="primary" @click="dialogVisible = true">新增物品</el-button>
        </div>
      </template>
      <el-table :data="tableData" stripe>
        <el-table-column prop="code" label="编号" width="120" />
        <el-table-column prop="name" label="物品名称" />
        <el-table-column prop="spec" label="规格" width="120" />
        <el-table-column prop="unit" label="单位" width="80" />
        <el-table-column prop="current_stock" label="当前库存" width="100" />
        <el-table-column prop="remark" label="备注" />
        <el-table-column label="操作" width="150">
          <template #default="{ row }">
            <el-button size="small" @click="handleEdit(row)">编辑</el-button>
            <el-button size="small" type="danger" @click="handleDelete(row.id)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <el-dialog v-model="dialogVisible" :title="isEdit ? '编辑物品' : '新增物品'" width="500px">
      <el-form :model="form" label-width="80px">
        <el-form-item label="编号">
          <el-input v-model="form.code" :disabled="isEdit" />
        </el-form-item>
        <el-form-item label="名称">
          <el-input v-model="form.name" />
        </el-form-item>
        <el-form-item label="规格">
          <el-input v-model="form.spec" />
        </el-form-item>
        <el-form-item label="单位">
          <el-input v-model="form.unit" />
        </el-form-item>
        <el-form-item label="库存">
          <el-input-number v-model="form.current_stock" :min="0" />
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
import { materialsApi } from '../api'
import { ElMessage } from 'element-plus'

const tableData = ref([])
const dialogVisible = ref(false)
const isEdit = ref(false)
const editId = ref(null)
const form = ref({ code: '', name: '', spec: '', unit: '', current_stock: 0, remark: '' })

const loadData = async () => {
  const res = await materialsApi.getAll()
  tableData.value = res.data
}

const handleSave = async () => {
  try {
    if (isEdit.value) {
      await materialsApi.update(editId.value, form.value)
    } else {
      await materialsApi.create(form.value)
    }
    dialogVisible.value = false
    loadData()
    ElMessage.success('操作成功')
  } catch (e) {
    ElMessage.error(e.response?.data?.detail || '操作失败')
  }
}

const handleEdit = (row) => {
  isEdit.value = true
  editId.value = row.id
  form.value = { ...row }
  dialogVisible.value = true
}

const handleDelete = async (id) => {
  await materialsApi.delete(id)
  loadData()
  ElMessage.success('删除成功')
}

onMounted(loadData)
</script>
