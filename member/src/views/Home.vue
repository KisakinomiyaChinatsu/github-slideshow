<template>
  <div class="home-page">
    <div class="header">
      <div class="user-info" v-if="member">
        <div class="name">{{ member.name }}</div>
        <div class="level">{{ member.level }}</div>
      </div>
      <van-button size="small" @click="logout">退出</van-button>
    </div>
    
    <van-cell-group inset style="margin: 15px 10px">
      <van-cell title="会员等级" :value="member?.level" />
      <van-cell title="当前积分" :value="member?.points" />
      <van-cell title="手机号" :value="member?.phone" />
    </van-cell-group>
    
    <van-pull-refresh v-model="refreshing" @refresh="onRefresh">
      <van-list
        :finished="true"
        finished-text="没有更多了"
      >
        <van-cell-group inset title="最近消费" style="margin: 0 10px">
          <van-cell v-for="c in consumptions" :key="c.id" :title="c.product_name" :value="'¥' + c.amount" :label="formatTime(c.consume_time)" />
        </van-cell-group>
        <van-empty v-if="consumptions.length === 0" description="暂无消费记录" />
      </van-list>
    </van-pull-refresh>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { membersApi, consumptionsApi } from '../api'

const router = useRouter()
const member = ref(null)
const consumptions = ref([])
const refreshing = ref(false)

const loadData = async () => {
  member.value = JSON.parse(localStorage.getItem('member') || '{}')
  const res = await consumptionsApi.getAll({ member_id: member.value.id })
  consumptions.value = res.data.slice(0, 10)
}

const onRefresh = async () => {
  await loadData()
  refreshing.value = false
}

const formatTime = (time) => {
  return new Date(time).toLocaleString('zh-CN')
}

const logout = () => {
  localStorage.removeItem('member')
  router.push('/login')
}

onMounted(loadData)
</script>

<style scoped>
.home-page { min-height: 100vh; background: #f5f5f5; }
.header {
  background: linear-gradient(135deg, #1989fa 0%, #0d47a1 100%);
  color: #fff;
  padding: 30px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.name { font-size: 24px; font-weight: bold; }
.level { font-size: 14px; opacity: 0.8; margin-top: 5px; }
</style>
