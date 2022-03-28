<template>

  <div class="login-container">
    <el-form ref="form" :model="form" class="login-main">
      <h1 style="text-align: center">知了在线聊天系统</h1>
      <el-form-item>
        <el-input v-model="form.username" placeholder="请输入用户名"></el-input>
      </el-form-item>
      <el-form-item style="text-align: right">
        <el-button type="primary" @click="onSubmit">登录</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import {ElMessage, ElNotification} from "element-plus";
export default {
  name: "Login",
  data() {
    return {
      form: {
        username: ""
      }
    };
  },
  mounted() {

	},
  methods: {
    onSubmit() {}
  }
};
</script>

<style scoped>
html,
body {
  height: 100%;
}
.login-container {
  width: 100vw;
  height: 100vh;
  background-image: url("../assets/login_bg.png");
  background-size: cover;
  overflow: hidden;
}

.login-container .login-main {
  border-radius: 5px;
  background-clip: padding-box;
  margin: 280px auto;
  width: 350px;
  padding: 35px 35px 15px;
  background: #fff;
  border: 1px solid #eaeaea;
  -webkit-box-shadow: 0 0 25px #cac6c6;
  box-shadow: 0 0 25px #cac6c6;
}
</style>
