<template>
  <el-container style="height: 100vh">
    <el-aside width="200px" style="background: #545c64">
      <el-menu
        :default-active="$route.path"
        router
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b"
      >
        <el-menu-item index="/members">
          <span>会员信息</span>
        </el-menu-item>
        <el-menu-item index="/consumptions">
          <span>消费记录</span>
        </el-menu-item>
        <el-menu-item index="/categories">
          <span>产品类别</span>
        </el-menu-item>
        <el-menu-item index="/products">
          <span>产品详情</span>
        </el-menu-item>
        <el-menu-item index="/materials">
          <span>物品信息</span>
        </el-menu-item>
        <el-menu-item index="/material-records">
          <span>物品记录</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
    <el-container>
      <el-header style="background: #fff; box-shadow: 0 1px 4px rgba(0,0,0,0.1)">
        <h2 style="margin: 0; line-height: 60px">业务管理系统</h2>
      </el-header>
      <el-main>
        <router-view />
      </el-main>
    </el-container>
  </el-container>
</template>

<script setup>
</script>
