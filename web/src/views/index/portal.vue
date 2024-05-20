<template>
  <div class="portal">
    <Header />
    <Swiper />
    <Content />
    <Footer />
  </div>
</template>
<script>
  import Header from '/@/views/index/components/header.vue';
  import Footer from '/@/views/index/components/footer.vue';
  import Content from '/@/views/index/components/content.vue';
  import Swiper from '/@/views/index/components/swiper.vue';

  export default {
    components: {
      Footer,
      Header,
      Content,
      Swiper,
    },
    data() {
      return {};
    },
  };
</script>
<style scoped lang="less">
</style>
