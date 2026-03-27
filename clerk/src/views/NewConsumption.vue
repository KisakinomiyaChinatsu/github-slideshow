<template>
  <div>
    <el-card>
      <template #header>
        <span>消费开单</span>
      </template>
      <el-form :model="form" label-width="100px">
        <el-form-item label="会员">
          <el-select v-model="form.member_id" placeholder="请选择会员" style="width: 100%">
            <el-option v-for="m in members" :key="m.id" :label="m.name + ' - ' + m.phone" :value="m.id" />
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
        <el-form-item>
          <el-button type="primary" @click="submit">提交订单</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { membersApi, consumptionsApi } from '../api'
import { ElMessage } from 'element-plus'

const members = ref([])
const form = ref({
  member_id: null,
  product_name: '',
  amount: 0,
  quantity: 1,
  remark: ''
})

onMounted(async () => {
  const res = await membersApi.getAll()
  members.value = res.data
})

const submit = async () => {
  if (!form.value.member_id) {
    ElMessage.warning('请选择会员')
    return
  }
  await consumptionsApi.create(form.value)
  ElMessage.success('订单提交成功')
  form.value = { member_id: null, product_name: '', amount: 0, quantity: 1, remark: '' }
}
</script>
