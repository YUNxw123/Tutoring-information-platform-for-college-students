<template>
  <div class="title"> 家教需求 </div>
  <div class="content">
    <div class="content-left">
      <div class="left-search-item">
        <h4>年级分类</h4>
        <a-tree :tree-data="contentData.cData" :selected-keys="contentData.selectedKeys" @select="onSelect" style="min-height: 220px" />
      </div>
      <!--      <div>{{ contentData.selectedKeys }}</div>-->
      <div class="left-search-item"
        ><h4>热门科目</h4>
        <div class="tag-view tag-flex-view">
          <span
            class="tag"
            :class="{ 'tag-select': contentData.selectTagId.includes(item.id) }"
            v-for="item in contentData.tagData"
            :key="item.id"
            @click="clickTag(item.id)"
            >{{ item.title }}</span
          >
        </div>
        <!--        <div>{{ userStore.usder_location }}</div>-->
        <!--        <div>{{ contentData.selectTagId }}</div>-->
      </div>
    </div>
    <div class="content-right">
      <div class="top-select-view flex-view">
        <div class="search-entry">
          <img :src="SearchIcon" class="search-icon" />
          <input placeholder="输入用户名关键词" ref="ss" @keyup.enter="search" />
        </div>
      </div>
      <a-spin :spinning="contentData.loading" style="min-height: 200px">
        <div class="pc-order-list flex-view">
          <div v-for="item in contentData.pageData" :key="item.id" @click="handleDetail(item)" class="order-item item-column-3">
            <div class="img-view">
              <img :src="item.useravatar" v-if="item.userrole == '2'" />
              <img :src="AdminAvatar" v-else />
            </div>
            <div class="info-view">
              <h3 class="order-name" v-if="item.userrole == '2'">{{ item.username }}</h3>
              <h3 class="order-name" v-else>管理员</h3>
              <span>
                <span class="a-price-symbol"></span>
                <span class="a-price">{{ item.price }}元/时</span>&nbsp;
                <span class="a-price">{{ item.location }}</span>
              </span>
            </div>
          </div>
          <div v-if="contentData.pageData.length <= 0 && !contentData.loading" class="no-data" style="">暂无数据</div>
        </div>
      </a-spin>
      <div class="page-view" style="">
        <a-pagination
          v-model="contentData.page"
          size="small"
          @change="changePage"
          :hideOnSinglePage="true"
          :defaultPageSize="contentData.pageSize"
          :total="contentData.total"
          :showSizeChanger="false"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
  import { listApi as listClassificationList } from '/@/api/index/classification';
  import { listApi as listTagList } from '/@/api/index/tag';
  import { listApi as listorderList } from '/@/api/index/order';
  import { BASE_URL } from '/@/store/constants';
  import { useUserStore } from '/@/store';
  import SearchIcon from '/@/assets/images/search-icon.svg';
  import AdminAvatar from '/@/assets/images/admin.png';

  const userStore = useUserStore();
  const router = useRouter();

  const contentData = reactive({
    selectX: 0,
    selectTagId: [],
    cData: [],
    selectedKeys: [],
    tagData: [],
    searchkeyword: '',
    loading: false,

    tabData: ['最新', '最热', '推荐'],
    selectTabIndex: 0,
    tabUnderLeft: 12,

    orderData: [],
    pageData: [],

    page: 1,
    total: 0,
    pageSize: 12,
  });
  const ss = ref();

  onMounted(() => {
    initSider();
    getorderList({});
  });
  const initSider = () => {
    contentData.cData.push({ key: '-1', title: '全部' });
    listClassificationList().then((res) => {
      res.data.forEach((item) => {
        item.key = item.id;
        contentData.cData.push(item);
      });
    });
    listTagList().then((res) => {
      contentData.tagData = res.data;
    });
  };
  const search = () => {
    getorderList({ keyword: ss.value.value });
  };
  const getSelectedKey = () => {
    if (contentData.selectedKeys.length > 0) {
      return contentData.selectedKeys[0];
    } else {
      return -1;
    }
  };
  const onSelect = (selectedKeys) => {
    contentData.selectedKeys = selectedKeys;
    console.log(contentData.selectedKeys[0]);
    if (contentData.selectedKeys.length > 0) {
      let tags = contentData.selectTagId.join(',');
      getorderList({ c: getSelectedKey(), tag: tags });
    }
  };
  const clickTag = (index) => {
    if (contentData.selectTagId.includes(index)) {
      contentData.selectTagId.splice(contentData.selectTagId.indexOf(index), 1);
      let tags = contentData.selectTagId.join(',');
      getorderList({ tag: tags, c: getSelectedKey() });
    } else {
      contentData.selectTagId.push(index);
      let tags = contentData.selectTagId.join(',');
      getorderList({ tag: tags, c: getSelectedKey() });
    }
  };
  const handleDetail = (item) => {
    // 跳转新页面
    let text = router.resolve({ name: 'particulars', query: { id: item.id } });
    window.open(text.href, '_blank');
  };
  // 分页事件
  const changePage = (page) => {
    contentData.page = page;
    let start = (contentData.page - 1) * contentData.pageSize;
    contentData.pageData = contentData.orderData.slice(start, start + contentData.pageSize);
    console.log('第' + contentData.page + '页');
  };
  const getorderList = (data) => {
    contentData.loading = true;
    listorderList(data)
      .then((res) => {
        contentData.loading = false;
        res.data.forEach((item, index) => {
          if (item.useravatar) {
            item.useravatar = BASE_URL + item.useravatar;
          } else {
          }
        });
        console.log(res);
        contentData.orderData = res.data;
        contentData.total = contentData.orderData.length;
        changePage(1);
      })
      .catch((err) => {
        console.log(err);
        contentData.loading = false;
      });
  };
</script>

<style scoped lang="less">
  .title {
    text-align: center;
    font-family: '微软雅黑';
    font-size: 25px;
    color: #3680ea;
  }
  .content {
    display: flex;
    flex-direction: row;
    width: 1100px;
    margin: 5px auto;
  }

  .content-left {
    width: 220px;
    margin-right: 32px;
  }

  .left-search-item {
    overflow: hidden;
    border-bottom: 1px solid #cedce4;
    margin-top: 24px;
    padding-bottom: 24px;
  }

  h4 {
    color: #4d4d4d;
    font-weight: 600;
    font-size: 16px;
    line-height: 24px;
    height: 24px;
  }

  .category-item {
    cursor: pointer;
    color: #333;
    margin: 12px 0 0;
    padding-left: 16px;
  }

  ul {
    margin: 0;
    padding: 0;
  }

  ul {
    list-style-type: none;
  }

  li {
    margin: 4px 0 0;
    display: list-item;
    text-align: -webkit-match-parent;
  }

  .child {
    color: #333;
    padding-left: 16px;
  }

  .child:hover {
    color: #4684e2;
  }

  .select {
    color: #4684e2;
  }

  .flex-view {
    -webkit-box-pack: justify;
    -ms-flex-pack: justify;
    //justify-content: space-between;
    display: flex;
  }

  .name {
    font-size: 14px;
  }

  .name:hover {
    color: #4684e2;
  }

  .count {
    font-size: 14px;
    color: #999;
  }

  .check-item {
    font-size: 0;
    height: 18px;
    line-height: 12px;
    margin: 12px 0 0;
    color: #333;
    cursor: pointer;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
  }

  .check-item input {
    cursor: pointer;
  }

  .check-item label {
    font-size: 14px;
    margin-left: 12px;
    cursor: pointer;
    -webkit-box-flex: 1;
    -ms-flex: 1;
    flex: 1;
  }

  .tag-view {
    -ms-flex-wrap: wrap;
    flex-wrap: wrap;
    margin-top: 4px;
  }

  .tag-flex-view {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
  }

  .tag {
    background: #fff;
    border: 1px solid #a1adc6;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    border-radius: 16px;
    height: 20px;
    line-height: 18px;
    padding: 0 8px;
    margin: 8px 8px 0 0;
    cursor: pointer;
    font-size: 12px;
    color: #152833;
  }

  .tag:hover {
    background: #4684e3;
    color: #fff;
    border: 1px solid #4684e3;
  }

  .tag-select {
    background: #4684e3;
    color: #fff;
    border: 1px solid #4684e3;
  }

  .content-right {
    -webkit-box-flex: 1;
    -ms-flex: 1;
    flex: 1;
    padding-top: 12px;

    .pc-search-view {
      margin: 0 0 24px;
      -webkit-box-align: center;
      -ms-flex-align: center;
      align-items: center;

      .search-icon {
        width: 20px;
        height: 20px;
        -webkit-box-flex: 0;
        -ms-flex: 0 0 20px;
        flex: 0 0 20px;
        margin-right: 16px;
      }

      input {
        outline: none;
        border: 0px;
        -webkit-box-flex: 1;
        -ms-flex: 1;
        flex: 1;
        border-bottom: 1px solid #cedce4;
        color: #152844;
        font-size: 14px;
        height: 22px;
        line-height: 22px;
        -ms-flex-item-align: end;
        align-self: flex-end;
        padding-bottom: 8px;
      }

      .clear-search-icon {
        position: relative;
        left: -20px;
        cursor: pointer;
      }

      button {
        outline: none;
        border: none;
        font-size: 14px;
        color: #fff;
        background: #288dda;
        border-radius: 32px;
        width: 88px;
        height: 32px;
        line-height: 32px;
        margin-left: 2px;
        cursor: pointer;
      }

      .float-count {
        color: #999;
        margin-left: 24px;
      }
    }

    .flex-view {
      display: flex;
    }

    .top-select-view {
      -webkit-box-pack: justify;
      -ms-flex-pack: justify;
      justify-content: space-between;
      -webkit-box-align: center;
      -ms-flex-align: center;
      align-items: center;
      height: 40px;
      line-height: 40px;

      .type-view {
        position: relative;
        font-weight: 400;
        font-size: 18px;
        color: #5f77a6;

        .type-tab {
          margin-right: 32px;
          cursor: pointer;
        }

        .type-tab-select {
          color: #152844;
          font-weight: 600;
          font-size: 20px;
        }

        .tab-underline {
          position: absolute;
          bottom: 0;
          //left: 22px;
          width: 16px;
          height: 4px;
          background: #4684e2;
          -webkit-transition: left 0.3s;
          transition: left 0.3s;
        }
      }

      .order-view {
        position: relative;
        color: #6c6c6c;
        font-size: 14px;

        .title {
          margin-right: 8px;
        }

        .tab {
          color: #999;
          margin-right: 20px;
          cursor: pointer;
        }

        .tab-select {
          color: #152844;
        }

        .tab-underline {
          position: absolute;
          bottom: 0;
          left: 84px;
          width: 16px;
          height: 4px;
          background: #4684e2;
          -webkit-transition: left 0.3s;
          transition: left 0.3s;
        }
      }
    }

    .pc-order-list {
      -ms-flex-wrap: wrap;
      flex-wrap: wrap;

      .order-item {
        min-width: 255px;
        max-width: 255px;
        position: relative;
        flex: 1;
        margin-right: 20px;
        height: fit-content;
        overflow: hidden;
        margin-top: 26px;
        margin-bottom: 36px;
        cursor: pointer;

        .img-view {
          //text-align: center;
          height: 200px;
          width: 200px;

          img {
            height: 200px;
            width: 200px;
            margin: 0 auto;
            background-size: useravatar;
            object-fit: useravatar;
          }
        }

        .info-view {
          //background: #f6f9fb;
          overflow: hidden;
          padding: 0 0px;

          .order-name {
            line-height: 32px;
            margin-top: 12px;
            font-size: 18px;
            color: #0f1111 !important;
            font-style: normal !important;
            text-transform: none !important;
            text-decoration: none !important;
          }

          .price {
            color: #ff7b31;
            font-size: 16px;
            line-height: 20px;
            margin-top: 4px;
            overflow: hidden;
            white-space: nowrap;
          }

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

      .no-data {
        height: 200px;
        line-height: 200px;
        text-align: center;
        width: 100%;
        font-size: 16px;
        color: #152844;
      }
    }

    .page-view {
      width: 100%;
      text-align: center;
      margin-top: 48px;
    }
  }
  .search-entry {
    position: relative;
    width: 400px;
    min-width: 200px;
    height: 32px;
    background: #ecf3fc;
    padding: 0 12px;
    border-radius: 16px;
    font-size: 0;
    cursor: pointer;

    img {
      max-width: 100%;
      height: auto;
    }
    .search-icon {
      width: 18px;
      margin: 0 8px 10px 0;
    }
    input {
      position: absolute;
      top: 4px;
      width: 85%;
      height: 24px;
      border: 0px;
      outline: none;
      color: #000;
      background: #ecf3fc;
      font-size: 14px;
    }
  }
  .a-price-symbol {
    top: -0.5em;
    font-size: 12px;
  }

  .a-price {
    color: #0f1111;
    font-size: 14px;
  }
</style>
