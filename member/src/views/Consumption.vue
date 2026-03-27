<template>
  <div class="consumption-page">
    <van-nav-bar title="消费记录" left-arrow @click-left="router.back()" />
    
    <van-pull-refresh v-model="refreshing" @refresh="onRefresh">
      <van-list :finished="true" finished-text="没有更多了">
        <van-cell-group inset>
          <van-cell v-for="c in consumptions" :key="c.id">
            <template #title>
              <div>{{ c.product_name }}</div>
              <van-text color="gray" size="small">{{ formatTime(c.consume_time) }}</van-text>
            </template>
            <template #value>
              <span style="color: #ee0a24">-¥{{ c.amount }}</span>
            </template>
          </van-cell>
        </van-cell-group>
        <van-empty v-if="consumptions.length === 0" description="暂无消费记录" />
      </van-list>
    </van-pull-refresh>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { consumptionsApi } from '../api'

const router = useRouter()
const consumptions = ref([])
const refreshing = ref(false)

const loadData = async () => {
  const member = JSON.parse(localStorage.getItem('member') || '{}')
  const res = await consumptionsApi.getAll({ member_id: member.id })
  consumptions.value = res.data
}

const onRefresh = async () => {
  await loadData()
  refreshing.value = false
}

const formatTime = (time) => new Date(time).toLocaleString('zh-CN')

onMounted(loadData)
</script>

<style scoped>
.consumption-page { min-height: 100vh; background: #f5f5f5; }
</style>
