<template>
  <div class="tutor">
    <Header />
    <Content :cc="cc" :tt="tt" />
    <Footer />
  </div>
</template>
<script setup lang="ts">
  import Header from '/@/views/index/components/header.vue';
  import Footer from '/@/views/index/components/footer.vue';
  import Content from '/@/views/index/components/tutor-information.vue';
  import { ref, onMounted } from 'vue';
  let cc = ref();
  let tt = ref();
  onMounted(() => {
    cc.value = history.state.cc;
    tt.value = history.state.tt;
  });
</script>
<style scoped lang="less"></style>
