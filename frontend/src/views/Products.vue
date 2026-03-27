<template>
  <div>
    <el-card>
      <template #header>
        <div style="display: flex; justify-content: space-between; align-items: center">
          <span>产品详情管理</span>
          <el-button type="primary" @click="dialogVisible = true">新增产品</el-button>
        </div>
      </template>
      <el-table :data="tableData" stripe>
        <el-table-column prop="code" label="编号" width="120" />
        <el-table-column prop="name" label="产品名称" />
        <el-table-column prop="category.name" label="类别" width="120" />
        <el-table-column prop="price" label="价格" width="100" />
        <el-table-column prop="stock" label="库存" width="100" />
        <el-table-column prop="description" label="描述" />
        <el-table-column label="操作" width="150">
          <template #default="{ row }">
            <el-button size="small" @click="handleEdit(row)">编辑</el-button>
            <el-button size="small" type="danger" @click="handleDelete(row.id)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <el-dialog v-model="dialogVisible" :title="isEdit ? '编辑产品' : '新增产品'" width="500px">
      <el-form :model="form" label-width="80px">
        <el-form-item label="编号">
          <el-input v-model="form.code" :disabled="isEdit" />
        </el-form-item>
        <el-form-item label="名称">
          <el-input v-model="form.name" />
        </el-form-item>
        <el-form-item label="类别">
          <el-select v-model="form.category_id" style="width: 100%">
            <el-option v-for="c in categories" :key="c.id" :label="c.name" :value="c.id" />
          </el-select>
        </el-form-item>
        <el-form-item label="价格">
          <el-input-number v-model="form.price" :min="0" style="width: 100%" />
        </el-form-item>
        <el-form-item label="库存">
          <el-input-number v-model="form.stock" :min="0" />
        </el-form-item>
        <el-form-item label="描述">
          <el-input v-model="form.description" type="textarea" />
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
import { productsApi, categoriesApi } from '../api'
import { ElMessage } from 'element-plus'

const tableData = ref([])
const categories = ref([])
const dialogVisible = ref(false)
const isEdit = ref(false)
const editId = ref(null)
const form = ref({ code: '', name: '', category_id: null, price: 0, stock: 0, description: '' })

const loadData = async () => {
  const [prodRes, catRes] = await Promise.all([productsApi.getAll(), categoriesApi.getAll()])
  tableData.value = prodRes.data
  categories.value = catRes.data
}

const handleSave = async () => {
  try {
    if (isEdit.value) {
      await productsApi.update(editId.value, form.value)
    } else {
      await productsApi.create(form.value)
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
  await productsApi.delete(id)
  loadData()
  ElMessage.success('删除成功')
}

onMounted(loadData)
</script>
