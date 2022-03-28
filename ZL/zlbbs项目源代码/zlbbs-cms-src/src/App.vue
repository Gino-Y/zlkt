<template>
  <div class="frame">
    <el-container class="frame-container">
      <el-header class="header">
        <a href="/" class="brand"><strong>知了</strong>管理系统</a>
        <div class="header-content">
          <div class="greet">欢迎，{{$auth.user.username}}[{{$auth.user.role.name}}]</div>
          <div class="signout">回到首页</div>
        </div>
      </el-header>
      <el-container>
        <el-aside width="200px" class="aside">
          <el-row class="menu-row">
            <el-col :span="24">
              <el-menu
                :default-active="defaultIndex"
                background-color="#545c64"
                active-text-color="#fff"
                text-color="#ddd"
                :router="true"
              >
                <el-menu-item index="1" :route="{name: 'home'}">
                  <template #title>
                    <el-icon><house /></el-icon>
                    <span>首页</span>
                  </template>
                </el-menu-item>

                <el-menu-item index="2" :route="{name: 'banner'}" v-if="has_permission('banner')">
                  <template #title>
                    <el-icon><picture-rounded /></el-icon>
                    <span>轮播图</span>
                  </template>
                </el-menu-item>

                <el-menu-item index="3" :route="{name: 'post'}" v-if="has_permission('post')">
                  <template #title>
                    <el-icon><postcard /></el-icon>
                    <span>帖子管理</span>
                  </template>
                </el-menu-item>

                <el-menu-item index="4" :route="{name: 'comment'}" v-if="has_permission('comment')">
                  <template #title>
                    <el-icon><comment /></el-icon>
                    <span>评论管理</span>
                  </template>
                </el-menu-item>

                <el-menu-item index="5" :route="{name: 'user'}" v-if="has_permission('user')">
                  <template #title>
                    <el-icon><user /></el-icon>
                    <span>用户管理</span>
                  </template>
                </el-menu-item>
              </el-menu>
            </el-col>
          </el-row>
        </el-aside>
        <el-container>
          <el-main class="main">
            <router-view></router-view>
          </el-main>
          <el-footer class="footer">这是Footer</el-footer>
        </el-container>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import {House, PictureRounded, Postcard, Comment,User} from "@element-plus/icons"
export default {
  name: "App",
  components: {
    House,
    PictureRounded,
    Postcard,
    Comment,
    User
  },
  data(){
    return {
    }
  },
  computed: {
    defaultIndex(){
      // http://127.0.0.1:8080/#/post
      const path = this.$route.path;
      let index = "1";
      if(path.indexOf("banner") >= 0){
        index = "2"
      }else if(path.indexOf('post') >= 0){
        index = "3"
      }else if(path.indexOf("comment") >= 0){
        index = "4"
      }else if(path.indexOf("user") >= 0){
        index = "5"
      }else{
        index = "1"
      }
      return index;
    }
  },
  mounted(){
    if(!this.$auth.is_staff){
      window.location = this.$http.server_host;
    }
  },
  methods: {
    has_permission(permission){
      return this.$auth.user.permissions.indexOf(permission) >= 0
    }
  }
};
</script>

<style scoped>
.frame-container {
  height: 100vh;
}
.header {
  height: 60px;
  background: #00a65a;
  display: flex;
}

.header .brand {
  width: 200px;
  margin-left: -20px;
  background-color: #008d4c;
  font-size: 20px;
  color: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
}
.header .header-content {
  flex: 1;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-left: 20px;
  color: #fff;
}

.header-content .signout {
    cursor: pointer;
  }

.aside {
  background-color: #545c64;
}

.aside .el-menu .is-active {
  background-color: #434a50 !important;
}

.footer {
  background: gray;
}
</style>

<style scoped>
.el-menu{
  border-right: none;
}
</style>

<style>
* {
  margin: 0;
  padding: 0;
  border: 0;
  text-decoration: none;
  vertical-align: baseline;
}
</style>