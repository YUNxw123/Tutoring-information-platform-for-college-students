<template>
  <!--    轮播背景图-->
  <el-carousel :interval="2000" class="swipers">
    <el-carousel-item v-for="item in SwiperImgList" :key="item" class="swiper">
      <a :href="item.link"><img :src="item.imageUrl" alt="img" /></a>
    </el-carousel-item>
  </el-carousel>
  <div class="banner_nav">
    <span></span>
    <p id="banner_navp">找老师 <i @click="NavClick"></i></p>
    <ul id="banner_navul" v-show="showDetail">
      <li>
        <h3 class="title">年级</h3>
        <div>
          <a v-for="item in cData" :key="item.id" @click="handlec(item.id)">{{ item.title }}{{ item.tag }}</a>
        </div>
      </li>
      <li>
        <h3 class="title">科目</h3>
        <div>
          <a v-for="item in tagData" :key="item.id" @click="handlet(item.id)">{{ item.title }}</a>
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
  import { ref } from 'vue';
  import { listApi as listClassificationList } from '/@/api/index/classification';
  import { listApi as listTagList } from '/@/api/index/tag';
  import { listApi as lisAdList } from '/@/api/index/ad';
  import { BASE_URL } from '/@/store/constants';

  // let SwiperImgList = ref(['/src/assets/images/swiper1.jpg', '/src/assets/images/swiper2.jpg', '/src/assets/images/swiper3.jpg']);
  const SwiperImgList = ref();
  const showDetail = ref(true);
  const tagData = ref();
  const cData = ref();
  const router = useRouter();

  onMounted(() => {
    getadList();
    getCDataList();
    getTagDataList();
  });
  const getadList = () => {
    lisAdList({})
      .then((res) => {
        console.log(res);
        res.data.forEach((item: any) => {
          if (item.image) {
            item.imageUrl = BASE_URL + item.image;
          }
        });
        SwiperImgList.value = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const NavClick = () => {
    showDetail.value = !showDetail.value;
  };
  const getCDataList = () => {
    listClassificationList({}).then((res) => {
      cData.value = res.data.slice(0, 20);
    });
  };
  const getTagDataList = () => {
    listTagList({}).then((res) => {
      res.data.forEach((item, index) => {
        item.index = index + 1;
      });
      tagData.value = res.data.slice(0, 30);
    });
  };
  const handlec = (item) => {
    // 跳转新页面
    router.push({ name: 'tutor', state: { cc: item } });
  };
  const handlet = (item) => {
    // 跳转新页面
    router.push({ name: 'tutor', state: { tt: item } });
  };
</script>

<style scoped>
  * {
    font-family: 微软雅黑;
  }
  .swipers {
    position: relative;
    height: 455px;
    width: 100%;
    font-size: 0;
    text-align: center;
  }
  .swiper {
    height: 455px;
    text-align: center;
  }
  .swiper img {
    height: 455px;
    max-width: 100%;
    vertical-align: bottom;
  }
  .banner_nav {
    width: 240px;
    overflow: hidden;
    position: absolute;
    top: 124px;
    left: 50%;
    margin-left: -600px;
    z-index: 11;
  }
  .banner_nav p {
    width: 100%;
    color: #ffffff;
    height: 45px;
    background: #3680ea;
    text-align: center;
    font-size: 18px;
    line-height: 45px;
    position: relative;
    z-index: 10;
    cursor: pointer;
    margin-bottom: 0em;
  }
  .banner_nav p i {
    float: right;
    width: 20px;
    height: 45px;
    background: url(/src/assets/images/bai_xiala.png) no-repeat 0px 20px;
    margin-right: 20px;
  }
  .banner_nav ul {
    list-style: none;
    display: block;
    position: relative;
    z-index: 10;
    height: 411px;
    margin-bottom: 0em;
    background: rgba(250, 250, 250, 0.6);
  }
  .banner_nav ul li {
    list-style: none;
    line-height: 26px;
    padding: 20px 0;
    border-top: 1px solid #ffffff;
    margin-top: -1px;
  }
  .banner_nav ul li a {
    color: #5e5e5e;
    font-size: 16px;
  }
  .title {
    display: block;
    width: 90%;
    margin: 0 auto;
  }
  .banner_nav ul li div {
    display: block;
    width: 90%;
    margin: 0 auto;
  }
  .banner_nav ul li div a {
    margin-right: 10px;
  }
</style>
