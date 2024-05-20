<template>
  <div class="main-bar-views">
    <div class="main-bar-view">
      <div class="left-view">
        <div class="local">
          <img :src="locaImage" />
        </div>
        <span id="current_city" style="font-size: 16px">{{ area[area.length - 1] }}</span>
        <a target="__black" type="a-link" style="line-height: 32px; width: 60px" @click="showcity">切换城市</a>
      </div>
      <div class="right-view">
        <a href="/admin" target="__black" type="a-link" style="line-height: 32px; width: 60px">后台入口</a>
        <template v-if="userStore.user_token">
          <a-dropdown>
            <a class="ant-dropdown-link" @click="(e) => e.preventDefault()">
              <img :src="tData.form.avatar" class="self-img" v-if="tData.form.avatar" />
              <img :src="AvatarIcon" class="self-img" v-else />
            </a>
            <template #overlay>
              <a-menu>
                <a-menu-item>
                  <a @click="goUserCenter('userInfoEditView')">个人设置</a>
                </a-menu-item>
                <a-menu-item>
                  <a @click="quit()">退出</a>
                </a-menu-item>
              </a-menu>
            </template>
          </a-dropdown>
        </template>
        <template v-else>
          <a-button @click="goRegister()">未注册，请先注册哟</a-button>
          <button class="login btn hidden-sm" @click="goLogin()">登录</button>
        </template>

        <div class="right-icon" @click="msgVisible = true">
          <img :src="MessageIcon" />
          <span class="msg-point" v-if="userStore.user_token"></span>
        </div>
        <div>
          <a-drawer title="我的消息" placement="right" :closable="true" :maskClosable="true" :visible="msgVisible" @close="onClose">
            <a-spin :spinning="loading" style="min-height: 200px">
              <div class="list-content">
                <div class="notification-view">
                  <div class="list" v-if="userStore.user_token">
                    <div class="notification-item flex-view" v-for="item in msgData">
                      <!---->
                      <div class="content-box">
                        <div class="header">
                          <span class="title-txt">{{ item.title }}</span>
                          <br />
                          <span class="time">{{ item.create_time }}</span>
                        </div>
                        <div class="head-text"> </div>
                        <div class="content">
                          <p>{{ item.content }}</p>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="list" v-else>
                    <a-button @click="goLogin()">未登录，请先登录哟</a-button>
                  </div>
                </div>
              </div>
            </a-spin>
          </a-drawer>
        </div>
      </div>
    </div>
  </div>
  <div class="header_cents">
    <div class="header_cent clearfix">
      <img :src="LogoImage" />
      <div class="header_nav" style="font-size: 16px">
        <span><a href="/index">首页</a></span>
        <span class="teachers"><a href="/index/tutor">师资力量</a></span>
        <span class="help"><a href="/index/demand">家教需求</a></span>
        <span class="find"><a type="link" @click="handleJoin('d')">找老师</a></span>
        <span class="students"><a type="link" @click="handleJoin('t')">做家教</a></span>
        <span class="tariff"><a href="/">资费说明</a></span>
      </div>
    </div>
  </div>
  <div>
    <a-modal
      :visible="showSelect"
      :forceRender="true"
      :title="请选择城市"
      width="880px"
      ok-text="确认"
      cancel-text="取消"
      @cancel="showcity"
      @ok="handleOk"
    >
      <a-cascader v-model:value="area" :options="city" placeholder="请选择地区" style="width: 300px" />
    </a-modal>
  </div>
</template>

<script setup lang="ts">
  import { listApi } from '/@/api/index/notice';
  import { useUserStore } from '/@/store';
  import locaImage from '/@/assets/images/icon_loca.png';
  import LogoImage from '/@/assets/images/logo.png';
  import AvatarIcon from '/@/assets/images/avatar.jpg';
  import MessageIcon from '/@/assets/images/message-icon.svg';
  import { message } from 'ant-design-vue';
  import { ref } from 'vue';
  import { detailApi } from '/@/api/index/user';
  import { BASE_URL } from '/@/store/constants';
  import city from '/@/assets/cities.json';

  const router = useRouter();
  const route = useRoute();
  const userStore = useUserStore();

  const keywordRef = ref();

  const area = ref(['广东省', '东莞市']);
  const showSelect = ref(false);

  let loading = ref(false);
  let msgVisible = ref(false);
  let msgData = ref([] as any);
  let tData = reactive({
    form: {
      avatar: undefined,
      avatarFile: undefined,
    },
  });
  onMounted(() => {
    if (userStore.user_id) {
      getUserInfo();
      getMessageList();
    }
  });
  const getUserInfo = () => {
    let userId = userStore.user_id;
    detailApi({ id: userId })
      .then((res) => {
        tData.form = res.data;
        if (tData.form.avatar) {
          tData.form.avatar = BASE_URL + tData.form.avatar;
        }
      })
      .catch((err) => {
        console.log(err);
      });
  };
  const showcity = () => {
    showSelect.value = !showSelect.value;
  };
  const handleOk = () => {
    showcity();
    userStore.user_location = area;
  };
  const getMessageList = () => {
    loading.value = true;
    listApi({
      uid: userStore.user_id,
    })
      .then((res) => {
        msgData.value = res.data;
        loading.value = false;
      })
      .catch((err) => {
        console.log(err);
        loading.value = false;
      });
  };
  const search = () => {
    const keyword = keywordRef.value.value;
    if (route.name === 'search') {
      router.push({ name: 'search', query: { keyword: keyword } });
    } else {
      let text = router.resolve({ name: 'search', query: { keyword: keyword } });
      window.open(text.href, '_blank');
    }
  };
  const goLogin = () => {
    router.push({ name: 'login' });
  };
  const goRegister = () => {
    router.push({ name: 'register' });
  };

  const goUserCenter = (menuName) => {
    router.push({ name: menuName });
  };
  const quit = () => {
    userStore.logout().then((res) => {
      router.push({ name: 'portal' });
    });
  };
  const onClose = () => {
    msgVisible.value = false;
  };

  function handleJoin(type) {
    let userId = userStore.user_id;
    if (userId) {
      if (type == 't') {
        router.push({ name: 'jiajiaoEditView' });
      } else {
        router.push({ name: 'demandView' });
      }
    } else {
      message.warn('请先登录！');
    }
  }
</script>

<style scoped lang="less">
  * {
    font-family: '微软雅黑';
  }
  .main-bar-views {
    height: 50px;
    width: 100%;
    background: #ffffff;
    border-bottom: 1px solid #cedce4;
    z-index: 16;
    display: flex;
    flex-direction: row;
    align-items: center; /*垂直居中*/
  }
  .main-bar-view {
    width: 1200px;
    margin: 0 auto;
    display: flex;
    flex-direction: row;
    align-items: center; /*垂直居中*/
  }
  .left-view {
    padding-left: 15px;
    flex: 1;
    display: flex;
    flex-direction: row;
    gap: 20px;
    justify-content: flex-start;
  }
  .local {
    position: relative;
    width: 24px;
    margin: 6px 0 0 4px;
    cursor: pointer;
    display: inline-block;
    font-size: 0;
  }
  .local img {
    width: 15px;
    height: 20px;
  }

  #current_city {
    display: flex;
    justify-content: center; //水平
    align-items: center;
  }

  .right-view {
    padding-right: 36px;
    flex: 1;
    display: flex;
    flex-direction: row;
    gap: 20px;
    justify-content: flex-end; /* 内容右对齐 */

    .username {
      height: 32px;
      line-height: 32px;
      text-align: center;
    }
    button {
      outline: none;
      border: none;
      cursor: pointer;
    }
    img {
      cursor: pointer;
    }
    .right-icon {
      position: relative;
      width: 24px;
      margin: 4px 0 0 4px;
      cursor: pointer;
      display: inline-block;
      font-size: 0;
      span {
        position: absolute;
        right: -15px;
        top: -3px;
        font-size: 12px;
        color: #fff;
        background: #4684e2;
        border-radius: 8px;
        padding: 0 4px;
        height: 16px;
        line-height: 16px;
        font-weight: 600;
        min-width: 20px;
        text-align: center;
      }
      .msg-point {
        position: absolute;
        right: -4px;
        top: 0;
        min-width: 8px;
        width: 8px;
        height: 8px;
        background: #4684e2;
        border-radius: 50%;
      }
    }

    .self-img {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      vertical-align: middle;
      cursor: pointer;
    }
    .btn {
      background: #4684e2;
      font-size: 14px;
      color: #fff;
      border-radius: 32px;
      text-align: center;
      width: 66px;
      height: 32px;
      line-height: 32px;
      vertical-align: middle;
    }
  }

  .content-list {
    flex: 1;

    .list-title {
      color: #152844;
      font-weight: 600;
      font-size: 18px;
      //line-height: 24px;
      height: 48px;
      margin-bottom: 4px;
      border-bottom: 1px solid #cedce4;
    }
  }

  .notification-item {
    padding-top: 16px;

    .avatar {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      margin-right: 8px;
    }

    .content-box {
      -webkit-box-flex: 1;
      -ms-flex: 1;
      flex: 1;
      border-bottom: 1px dashed #e9e9e9;
      padding: 4px 0 16px;
    }

    .header {
      margin-bottom: 12px;
    }

    .title-txt {
      color: #315c9e;
      font-weight: 500;
      font-size: 14px;
    }

    .time {
      color: #a1adc5;
      font-size: 14px;
    }

    .head-text {
      color: #152844;
      font-weight: 500;
      font-size: 14px;
      line-height: 22px;

      .name {
        margin-right: 8px;
      }
    }

    .content {
      margin-top: 4px;
      color: #484848;
      font-size: 14px;
      line-height: 22px;
    }
  }
  .header_cents {
    width: 100%;
    height: 74px;
    display: flex;
    flex-direction: row;
    align-items: center; /*垂直居中*/
  }

  .header_cent {
    width: 1200px;
    margin: 0 auto;
    display: flex;
    flex-direction: row;
    align-items: center; /*垂直居中*/
  }
  .header > img {
    display: flex;
    flex-direction: row;
    align-items: center; /*垂直居中*/
    justify-content: flex-start;
  }
  .header_nav {
    padding-right: 36px;
    flex: 1;
    display: flex;
    flex-direction: row;
    gap: 20px;
    justify-content: flex-end; /* 内容右对齐 */
  }
  .header_nav a {
    color: #333333;
  }
  //.selectcity{
  //  position: absolute;
  //  top: 10px;
  //  left: 360px;
  //  z-index: 100;
  //}
</style>
