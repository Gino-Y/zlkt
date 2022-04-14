<template>
  <div>
    <el-space direction="vertical" :size="20" style="width: 100%">
      <h1>轮播图管理</h1>
      <div style="text-align: right">
        <el-button type="primary">
          <el-icon><plus /></el-icon>
          添加轮播图
        </el-button>
      </div>
    </el-space>
  </div>
</template>

<script>
import { Plus } from "@element-plus/icons";
export default {
  name: "Banner",
  components: {
    Plus
  },
  mounted() {}
};
</script>

<style scoped>
.el-space {
  display: block;
}
</style>
