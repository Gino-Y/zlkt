<script>
import {ElMessage} from "element-plus";
export default {
  name: "chat-text",
  computed: {
    current_session(){
      return this.$store.state.current_session
    }
  },
  data() {
    return {
      content: "",
    };
  },
  methods: {
    onKeyup(e) {
      if (e.ctrlKey && e.keyCode === 13 && this.content.length) {
        if(!this.current_session){
          ElMessage.info("请先选中聊天对象！");
          return
        }
        const content = this.content;
        this.$socket.emitSendMessage(
          {to: this.current_session.user.sid, message: this.content},
          (result) => {
            if(result['code'] == 200){
              this.$store.commit("SEND_MESSAGE", content);
            }
          }
        )
        this.content = "";
      }
    },
  },
};
</script>

<template>
  <div class="text">
    <textarea
      placeholder="按 Ctrl + Enter 发送"
      v-model="content"
      @keyup="onKeyup"
    ></textarea>
  </div>
</template>

<style lang="less" scoped>
.text {
  height: 160px;
  border-top: solid 1px #ddd;

  textarea {
    padding: 10px;
    height: 100%;
    width: 100%;
    border: none;
    outline: none;
    font-family: "Micrsofot Yahei";
    resize: none;
  }
}
</style>
