<template>
  <el-form-item>
    <el-select v-model="province" filterable placeholder="请选择省份" style="width: 240px">
      <el-option v-for="index in provinceArr" :value="index" />
    </el-select>
  </el-form-item>
  <el-form-item>
    <el-select v-model="city" filterable placeholder="请选择市" style="width: 240px">
      <el-option v-for="index in cityArr" :value="index" />
    </el-select>
  </el-form-item>
  <el-form-item>
    <el-select v-model="area" filterable placeholder="请选择区" style="width: 240px">
      <el-option v-for="index in areaArr" :value="index" />
    </el-select>
  </el-form-item>
</template>

<script setup>
  import { ref, computed, watch } from 'vue';
  // 详细地址(省市区 详细地址)
  import areaObj from '/@/assets/area.json';
  // 省
  const provinceArr = Object.keys(areaObj);
  const province = ref(provinceArr[0]);
  // 市
  const cityArr = computed(() => {
    return Object.keys(areaObj[province.value]);
  });
  const city = ref(cityArr.value[0]);
  // 监听省份变化
  watch(province, (newVal) => {
    city.value = Object.keys(areaObj[newVal])[0];
  });
  // 区
  const areaArr = computed(() => {
    return areaObj[province.value][city.value];
  });
  const area = ref(areaArr.value[0]);
  // 监听市变化
  watch(city, (newVal) => {
    area.value = areaObj[province.value][newVal][0];
  });
  // 详细地址
  const detailArea = ref('');
  defineExpose({
    area: area,
  });
  const props = defineProps({
    area: Object,
  });
</script>

<style></style>
