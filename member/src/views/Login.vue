<template>
  <div class="login-page">
    <div class="logo">会员端</div>
    <van-cell-group inset style="margin: 20px">
      <van-field v-model="phone" label="手机号" placeholder="请输入手机号" />
    </van-cell-group>
    <div style="padding: 0 20px">
      <van-button type="primary" block @click="login">登录</van-button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { membersApi } from '../api'
import { showToast } from 'vant'

const router = useRouter()
const phone = ref('')

const login = async () => {
  if (!phone.value) {
    showToast('请输入手机号')
    return
  }
  const res = await membersApi.getAll()
  const member = res.data.find(m => m.phone === phone.value)
  if (member) {
    localStorage.setItem('member', JSON.stringify(member))
    router.push('/home')
  } else {
    showToast('未找到该会员')
  }
}
</script>

<style scoped>
.login-page {
  padding-top: 100px;
  text-align: center;
}
.logo {
  font-size: 32px;
  font-weight: bold;
  color: #1989fa;
  margin-bottom: 50px;
}
</style>
