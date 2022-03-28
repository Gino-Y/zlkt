<template>
  <div id="home">
      <h1>首页</h1>
      <div class="zl-chart" id="board-post-count"></div>
      <div class="zl-chart" id="day7-post-count"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';
import { ElMessage } from 'element-plus';
export default {
    name: "Home",
    mounted() {
      this.loadBoardPostCountChat();
      this.load7DayPostCountChat();
    },
    methods: {
      loadBoardPostCountChat(){
        this.$http.getBoardPostCount().then(res => {
          if(res['code'] != 200){
            ElMessage.error(res['message']);
            return;
          }
          var data = res['data'];
          var board_names = data['board_names'];
          var post_counts = data['post_counts'];
          var chartDom = document.getElementById('board-post-count');
          var myChart = echarts.init(chartDom);
          // board_names = ['Python','Flask','Django', '爬虫', '前端']
          // post_counts = [
          //   {value: 206,itemStyle: {color: '#3FB17C'}},
          //   {value: 178,itemStyle: {color: '#5C7BD9'}},
          //   {value: 108,itemStyle: {color: '#9FE080'}},
          //   {value: 138,itemStyle: {color: '#FFDC60'}},
          //   {value: 68,itemStyle: {color: '#FF915A'}},
          // ]
          var option;
          option = {
            title: {
              text: "板块帖子数",
              x: "center",
              y: "bottom"
            },
            tooltip: {
              trigger: 'axis'
            },
            xAxis: {
              type: 'category',
              data: board_names
            },
            yAxis: {
              type: 'value'
            },
            series: [
              {
                data: post_counts,
                type: 'bar'
              }
            ]
          };
          option && myChart.setOption(option);
        })
      },
      load7DayPostCountChat(){
        this.$http.getDay7PostCount().then(res => {
          if(res['code'] != 200){
            ElMessage.error(res['message']);
            return;
          }
          var data = res['data'];
          var dates = data['dates']
          var counts = data['counts']
          var chartDom = document.getElementById('day7-post-count');
          var myChart = echarts.init(chartDom);
          var option;

          option = {
            title: {
              text: "近7天帖子数",
              x: "center",
              y: "bottom"
            },
            tooltip: {
              trigger: 'axis'
            },
            xAxis: {
              type: 'category',
              boundaryGap: false,
              data: dates
            },
            yAxis: {
              type: 'value'
            },
            series: [
              {
                data: counts,
                type: 'line',
                areaStyle: {}
              },
            ]
          };
          option && myChart.setOption(option);
        })
      }
    }
}
</script>

<style scoped>
.zl-chart{
  height: 300px;
  width: 100%;
}
</style>