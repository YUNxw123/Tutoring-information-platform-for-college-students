<template>
  <div class="content-list">
    <div class="list-title"
      >我的需求
      <a-button class="add" type="primary" @click="handleAdd">新增需求</a-button>
    </div>

    <div role="tablist" class="list-tabs-view flex-view"> </div>
    <div class="list-content">
      <div class="collect-order-view">
        <a-spin :spinning="loading" style="min-height: 200px">
          <div class="order-list flex-view">
            <div class="order-item item-column-3" v-for="(item, index) in orderData" :key="index">
              <div class="remove" @click="handleRemove(item)">删除</div>
              <div class="img-view" @click="handleClickItem(item)">
                <img :src="item.useravatar" />
              </div>
              <div class="info-view">
                <h3 class="order-name">分类：{{ item.classification_title }}</h3>
                <p class="authors">状态：{{ item.status }}</p>
                <p class="translators">创建时间：{{ item.create_time }}</p>
                <p class="translators" v-if="item.over_time">结束时间：{{ item.over_time }}</p>
              </div>
            </div>
            <template v-if="!orderData || orderData.length <= 0">
              <a-empty style="width: 100%; margin-top: 200px" />
            </template>
          </div>
        </a-spin>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { message } from 'ant-design-vue';
  import { listApi, deleteApi } from '/@/api/index/order';
  import { BASE_URL } from '/@/store/constants';
  import { useUserStore } from '/@/store';

  const router = useRouter();
  const route = useRoute();
  const userStore = useUserStore();

  let orderData = ref([]);

  onMounted(() => {
    getorderList();
  });

  const loading = ref(false);

  const handleClickItem = (record) => {
    router.push({ name: 'demandEditView', query: { id: record.id } });
  };
  const handleAdd = () => {
    router.push({ name: 'demandEditView', query: { id: 0 } });
  };
  const handleRemove = (record) => {
    let username = userStore.user_name;
    deleteApi({ id: record.id })
      .then((res) => {
        message.success('移除成功');
        getorderList();
      })
      .catch((err) => {
        console.log(err);
      });
  };
  const getorderList = () => {
    loading.value = true;
    let username = userStore.user_name;
    listApi({ username: username })
      .then((res) => {
        res.data.forEach((item) => {
          item.useravatar = BASE_URL + item.useravatar;
          if (item.status) {
            if (item.status == '1') {
              item.status = '下架';
            } else if (item.status == '2') {
              item.status = '待审核';
            } else if (item.status == '3') {
              item.status = '已结束';
            } else {
              item.status = '上架';
            }
          }
        });
        orderData.value = res.data;
        loading.value = false;
      })
      .catch((err) => {
        console.log(err.msg);
        loading.value = false;
      });
  };
</script>
<style scoped lang="less">
  .flex-view {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
  }

  .content-list {
    -webkit-box-flex: 1;
    -ms-flex: 1;
    flex: 1;

    .list-title {
      color: #152844;
      font-weight: 600;
      font-size: 18px;
      line-height: 24px;
      height: 24px;
      margin-bottom: 4px;
      .add {
        margin-left: 20px;
      }
    }

    .list-tabs-view {
      position: relative;
      border-bottom: 1px solid #cedce4;
      height: 12px;
      line-height: 42px;
    }
  }

  .order-list {
    -ms-flex-wrap: wrap;
    flex-wrap: wrap;
    -webkit-box-pack: start;
    -ms-flex-pack: start;
    justify-content: flex-start;

    .order-item {
      position: relative;
      -webkit-box-flex: 1;
      -ms-flex: 1;
      flex: 1;
      margin-right: 20px;
      min-width: 255px;
      max-width: 255px;
      height: fit-content;
      border-radius: 4px;
      overflow: hidden;
      margin-top: 16px;
      cursor: pointer;

      .remove {
        position: absolute;
        right: 8px;
        top: 8px;
        width: 48px;
        height: 20px;
        text-align: center;
        line-height: 20px;
        color: #fff;
        background: #a1adc5;
        border-radius: 32px;
        cursor: pointer;
      }

      .img-view {
        background: #eaf1f5;
        font-size: 0;
        text-align: center;
        height: 156px;
        padding: 8px 0;

        img {
          max-width: 100%;
          height: 100%;
          display: block;
          margin: 0 auto;
          border-radius: 4px;
          -webkit-box-sizing: border-box;
          box-sizing: border-box;
        }
      }

      .info-view {
        background: #f6f9fb;
        text-align: center;
        height: 108px;
        overflow: hidden;
        padding: 0 16px;

        h3 {
          color: #1c355a;
          font-weight: 500;
          font-size: 16px;
          line-height: 20px;
          overflow: hidden;
          text-overflow: ellipsis;
          display: -webkit-box;
          -webkit-line-clamp: 2;
          -webkit-box-orient: vertical;
          margin: 12px 0 8px;
        }

        .authors,
        .translators {
          color: #6f6f6f;
          font-size: 12px;
          line-height: 14px;
          margin-top: 4px;
          overflow: hidden;
          text-overflow: ellipsis;
          white-space: nowrap;
        }
      }
    }
  }
</style>
