<template>
  <div>
    <el-card>
      <template #header>
        <div style="display: flex; justify-content: space-between; align-items: center">
          <span>会员信息管理</span>
          <el-button type="primary" @click="dialogVisible = true">新增会员</el-button>
        </div>
      </template>
      <el-table :data="tableData" stripe>
        <el-table-column prop="code" label="编号" width="120" />
        <el-table-column prop="name" label="姓名" />
        <el-table-column prop="phone" label="手机号" width="150" />
        <el-table-column prop="level" label="会员等级" width="120" />
        <el-table-column prop="points" label="积分" width="100" />
        <el-table-column prop="remark" label="备注" />
        <el-table-column label="操作" width="150">
          <template #default="{ row }">
            <el-button size="small" @click="handleEdit(row)">编辑</el-button>
            <el-button size="small" type="danger" @click="handleDelete(row.id)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <el-dialog v-model="dialogVisible" :title="isEdit ? '编辑会员' : '新增会员'" width="500px">
      <el-form :model="form" label-width="80px">
        <el-form-item label="编号">
          <el-input v-model="form.code" :disabled="isEdit" />
        </el-form-item>
        <el-form-item label="姓名">
          <el-input v-model="form.name" />
        </el-form-item>
        <el-form-item label="手机号">
          <el-input v-model="form.phone" />
        </el-form-item>
        <el-form-item label="会员等级">
          <el-select v-model="form.level" style="width: 100%">
            <el-option label="普通会员" value="普通会员" />
            <el-option label="银卡会员" value="银卡会员" />
            <el-option label="金卡会员" value="金卡会员" />
            <el-option label="钻石会员" value="钻石会员" />
          </el-select>
        </el-form-item>
        <el-form-item label="积分">
          <el-input-number v-model="form.points" :min="0" />
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
import { membersApi } from '../api'
import { ElMessage } from 'element-plus'

const tableData = ref([])
const dialogVisible = ref(false)
const isEdit = ref(false)
const editId = ref(null)
const form = ref({
  code: '',
  name: '',
  phone: '',
  level: '普通会员',
  points: 0,
  remark: ''
})

const loadData = async () => {
  const res = await membersApi.getAll()
  tableData.value = res.data
}

const handleSave = async () => {
  try {
    if (isEdit.value) {
      await membersApi.update(editId.value, form.value)
    } else {
      await membersApi.create(form.value)
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
  await membersApi.delete(id)
  loadData()
  ElMessage.success('删除成功')
}

onMounted(loadData)
</script>
