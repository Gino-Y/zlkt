<script>
export default {
  name: "list",
	mounted(){},
  methods: {}
};
</script>

<template>
  <div class="list">
    <ul>
      <li class="active">
        <img class="avatar"  width="30" height="30" alt="张三" src="">
        <el-badge :value="2" class="item" :hidden="false">
          <p class="name">张三(192.168.0.1)</p>
        </el-badge>
      </li>
    </ul>
  </div>
</template>

<style scoped lang="less">
.list {
  li {
    padding: 12px 15px;
    border-bottom: 1px solid #292c33;
    cursor: pointer;
    transition: background-color 0.1s;

    &:hover {
      background-color: rgba(255, 255, 255, 0.03);
    }
    &.active {
      background-color: rgba(255, 255, 255, 0.1);
    }
    .unread-count{
      padding: 2px 5px;
    }
  }
  .avatar,
  .name {
    vertical-align: middle;
  }
  .avatar {
    border-radius: 2px;
  }
  .name {
    display: inline-block;
    margin: 0 0 0 15px;
  }
}
</style>
