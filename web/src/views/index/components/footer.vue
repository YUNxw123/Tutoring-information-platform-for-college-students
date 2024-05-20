<template>
  <div class="footer">
    <div class="footer_con">
      <div class="gotop" @click="toTop">
        <img :src="GotopImage" />
        <p>回到顶部</p>
      </div>
    </div>
    <div class="footr">
      <div class="footer_ifo">
        <p>
          Copyright 2024.大学生家教信息平台的设计与实现 All rights reserved.
          <a href="http://beian.miit.gov.cn/" target="_blank" style="color: #fff; font-size: 12px">湘ICP备********号</a>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
  import LogoImage from '/@/assets/images/logo.png';
  import GotopImage from '/@/assets/images/bai_xiala.png';
  const toTop = () => {
    document.documentElement.scrollTop = 0;
  };
</script>

<style scoped lang="less">
  .footer {
    height: 68px;
    width: 100%;
    background: rgba(255, 255, 255, 0.5);
    border-top: 1px solid #cedce4;
  }
  .footer_con {
    height: 38px;
    width: 1200px;
    margin: 0 auto;
  }
  .gotop {
    height: 42px;
    width: 80px;
    float: right;
    color: #3680ea;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  .gotop img {
    height: 10px;
    margin-top: 5px;
    background: rgba(54, 128, 234, 0.9);
    transform: rotateX(180deg);
  }
  .gotop p {
    color: #3680ea;
    text-align: center;
    margin: auto;
  }

  .footr {
    width: 100%;
    background: rgba(83, 83, 83, 0.5);
  }
  .footer_ifo {
    width: 1200px;
    margin: 0 auto;
  }
  .footer_ifo p {
    font-size: 12px;
    color: #ffffff;
    text-align: center;
    line-height: 30px;
  }
</style>
