<template>
  <div>
    <el-space direction="vertical" :size="20">
      <h1>帖子管理</h1>
      <el-table :data="posts" style="width: 100%">
        <el-table-column label="标题">
          <template #default="scope">
            <a :href="$http.server_host + '/post/detail/' + scope.row.id" target="_blank">{{
              scope.row.title
            }}</a>
          </template>
        </el-table-column>
        <el-table-column prop="create_time" label="发布时间" width="180" />
        <el-table-column prop="board.name" label="所属板块" />
        <el-table-column prop="author.username" label="作者" />
        <el-table-column label="操作">
          <template #default="scope">
            <el-button
              type="danger"
              circle
              size="mini"
              @click="onDeletePostClick(scope.$index)"
            >
              <el-icon><delete /></el-icon>
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-space>

    <!-- 删除轮播图确认对话框 -->
  <el-dialog
    v-model="confirmDialogVisible"
    title="提示"
    width="30%"
  >
    <span>如果删除帖子，该帖子下所有的评论也会被删除，您确定要删除吗？</span>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="confirmDialogVisible = false">取消</el-button>
        <el-button type="primary" @click="onConfirmDeletePostClick">确定</el-button>
      </span>
    </template>
  </el-dialog>
  </div>
</template>

<script>
import {Delete} from "@element-plus/icons";
import { ElMessage } from 'element-plus';
export default {
  name: "Post",
  data() {
    return {
      deletingIndex: 0,
      confirmDialogVisible: false,
      posts: []
    };
  },
  mounted() {
  },
  methods: {
    onDeletePostClick(index) {
      this.confirmDialogVisible = true;
      console.log(index)
    },
    onConfirmDeletePostClick(){
    }
  },
  components: {
    Delete
  }
};
</script>

<style scoped>
.el-space {
  display: block;
}
</style>
