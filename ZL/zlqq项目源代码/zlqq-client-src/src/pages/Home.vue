<template>
<h1 style="text-align: center;padding: 10px;">知了传课在线聊天系统</h1>
  <div class="home-container">
    <template v-if="$store.state.user">
      <div class="sidebar">
        <card></card>
        <list></list>
      </div>
      <div class="main">
        <message></message>
        <chat-text></chat-text>
      </div>
    </template>
  </div>
</template>

<script>
import card from "@/components/card";
import list from "@/components/list";
import ChatText from "@/components/text";
import message from "@/components/message";

export default {
  name: "Home",
  created() {},
  mounted() {
    if (!this.$store.getters.logined) {
      this.$router.push({ name: "login" });
      return;
    }
  },
  components: {
    card,
    list,
    [ChatText.name]: ChatText,
    message,
  },
};
</script>

<style>
body,
html {
  height: 100%;
  overflow: hidden;
}
body {
  font: 14px/1.4em "Helvetica Neue", Helvetica, "Microsoft Yahei", Arial,
    sans-serif;
  background: #f5f5f5 url('../assets/chat_bg.jpg') no-repeat center;
  background-size: cover;
}
ul {
  list-style: none;
}
</style>

<style scoped lang="less">
.home-container {
  margin: 20px auto;
  width: 800px;
  height: 600px;

  overflow: hidden;
  border-radius: 3px;

  .sidebar,
  .main {
    height: 100%;
  }
  .sidebar {
    float: left;
    width: 200px;
    color: #f4f4f4;
    background-color: #2e3238;
  }
  .main {
    position: relative;
    overflow: hidden;
    background-color: #eee;
  }
  .text {
    position: absolute;
    width: 100%;
    bottom: 0;
    left: 0;
  }
  .message {
    height: ~"calc(100% - 160px)";
  }
}
</style>