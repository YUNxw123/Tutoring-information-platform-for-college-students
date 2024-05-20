<template>
  <div class="content-list">
    <div class="list-title">发布需求</div>
    <a-spin :spinning="loading" style="min-height: 200px">
      <div class="list-content">
        <div class="edit-view">
          <div class="item flex-view">
            <div class="label">用户头像</div>
            <div class="right-box avatar-box flex-view">
              <img v-if="uData.form && uData.form.avatar" :src="uData.form.avatar" class="avatar" />
              <img v-else :src="AvatarIcon" class="avatar" />
            </div>
          </div>
          <div class="item flex-view">
            <div class="label">用户名</div>
            <div class="right-box" v-if="uData.form.nickname">{{ uData.form.nickname }} </div>
            <div class="right-box" v-else
              >{{ uData.form.username }}
              <p class="tip">默认为您用户资料填写的昵称，昵称未存在将显示用户名</p>
            </div>
          </div>
          <div class="item flex-view">
            <div class="label">手机号</div>
            <div class="right-box" v-if="tData.form.mobile">
              <input type="text" v-model="tData.form.mobile" placeholder="请输入手机号" maxlength="100" class="input-dom web-input" />
            </div>
            <div class="right-box" v-else>
              <input type="text" v-model="uData.form.mobile" placeholder="请输入手机号" maxlength="100" class="input-dom web-input" />
              <p class="tip">默认为您用户资料填写的电话号码，您也可以选择重新输入</p>
            </div>
          </div>
          <div class="item flex-view">
            <div class="label">家教性别要求</div>
            <div class="right-box">
              <a-radio-group v-model:value="tData.form.sex" class="radio-group">
                <a-radio key="M" value="M" class="radio">男</a-radio>
                <a-radio key="F" value="F" class="radio">女</a-radio>
                <a-radio key="N" value="N" class="radio">无要求</a-radio>
              </a-radio-group>
            </div>
          </div>
          <div class="item flex-view">
            <div class="label">地区</div>
            <div class="right-box">
              <a-cascader v-model:value="tData.form.location" :options="city" placeholder="请选择地区" style="width: 300px" />
            </div>
          </div>
          <div class="item flex-view">
            <div class="label">预期小时价格</div>
            <div class="right-box">
              <input type="number" v-model="tData.form.price" placeholder="请输入价格" maxlength="100" class="input-dom web-input" />
            </div>
          </div>
          <div class="item flex-view">
            <div class="label">年级</div>
            <div class="right-box">
              <a-select
                placeholder="请选择"
                allowClear
                :options="cData"
                style="width: 200px"
                :field-names="{ label: 'title', value: 'id' }"
                v-model:value="tData.form.classification"
              />
            </div>
            <div class="label">科目</div>
            <div class="right-box" style="width: 200px !important">
              <a-select
                placeholder="请选择"
                allowClear
                mode="multiple"
                :options="tagData"
                style="width: 200px"
                :field-names="{ label: 'title', value: 'id' }"
                v-model:value="tData.form.tag"
              />
            </div>
          </div>
          <div class="item flex-view">
            <div class="label">需求简介</div>
            <div class="right-box">
              <textarea v-model="tData.form.description" placeholder="可以简单补充您的需求" maxlength="200" class="intro"> </textarea>
              <p class="tip">限制200字以内</p>
            </div>
          </div>
          <button class="save mg" @click="submit()">保存</button>
          <button class="save mg" @click="over()">结束</button>
        </div>
      </div>
    </a-spin>
  </div>
</template>

<script setup>
  import { message } from 'ant-design-vue';
  import { listUserorderApi, updateApi, createApi } from '/@/api/index/order';
  import { listApi as listClassificationApi } from '/@/api/admin/classification';
  import { listApi as listTagApi } from '/@/api/admin/tag';
  import { BASE_URL } from '/@/store/constants';
  import { useUserStore } from '/@/store';
  import AvatarIcon from '/@/assets/images/avatar.jpg';
  import city from '/@/assets/cities.json';
  import { detailApi } from '/@/api/index/user';
  import { useRoute, useRouter } from 'vue-router';

  const router = useRouter();
  const route = useRoute();
  const userStore = useUserStore();
  let orderId = ref('');
  let loading = ref(false);
  let tData = reactive({
    form: {
      classification: undefined,
      tag: [],
      price: undefined,
      mobile: undefined,
      sex: undefined,
      status: undefined,
      location: undefined,
      description: undefined,
    },
  });
  let uData = reactive({
    form: {
      avatar: undefined,
      avatarFile: undefined,
      nickname: undefined,
      email: undefined,
      mobile: undefined,
      description: undefined,
    },
  });
  let cData = ref([]);
  let tagData = ref([]);

  onMounted(() => {
    orderId.value = route.query.id.trim();
    getUserInfo();
    getCDataList();
    getTagDataList();
    getUserorder();
  });

  const getUserInfo = () => {
    loading.value = true;
    let userId = userStore.user_id;
    detailApi({ id: userId })
      .then((res) => {
        uData.form = res.data;
        if (uData.form.avatar) {
          uData.form.avatar = BASE_URL + uData.form.avatar;
        }
        loading.value = false;
      })
      .catch((err) => {
        console.log(err);
        loading.value = false;
      });
  };
  const getCDataList = () => {
    listClassificationApi({}).then((res) => {
      cData.value = res.data;
    });
  };
  const getTagDataList = () => {
    listTagApi({}).then((res) => {
      res.data.forEach((item, index) => {
        item.index = index + 1;
      });
      tagData.value = res.data;
    });
  };
  const getUserorder = () => {
    loading.value = true;
    let userId = userStore.user_id;
    listUserorderApi({ user: userId, oid: orderId.value })
      .then((res) => {
        console.log(res);
        if (res.data && res.data.length > 0) {
          tData.form = res.data[0];
        }
        if (tData.form.cover) {
          tData.form.avatar = BASE_URL + tData.form.cover;
        }
        loading.value = false;
      })
      .catch((err) => {
        console.log(err);
        loading.value = false;
      });
  };
  const submit = () => {
    let formData = new FormData();
    let userId = userStore.user_id;
    if (tData.form.classification) {
      formData.append('classification', tData.form.classification);
    } else {
      message.warn('请选择年级');
      return;
    }
    if (tData.form.tag.length == 0) {
      message.warn('请选择科目');
      return;
    } else {
      tData.form.tag.forEach(function (value) {
        if (value) {
          formData.append('tag', value);
        }
      });
    }
    if (tData.form.sex) {
      formData.append('sex', tData.form.sex);
    } else {
      message.warn('性别不能为空');
      return;
    }
    if (!tData.form.mobile) {
      if (!uData.form.mobile) {
        message.warn('请输入手机号码');
        return;
      } else if (!/^1[3|4|5|6|7|8|9][0-9]\d{8}$/.test(uData.form.mobile)) {
        message.warn('请输入正确的手机号码');
        return;
      } else {
        formData.append('mobile', uData.form.mobile);
      }
    } else if (!/^1[3|4|5|6|7|8|9][0-9]\d{8}$/.test(tData.form.mobile)) {
      message.warn('请输入正确的手机号码');
      return;
    } else {
      formData.append('mobile', tData.form.mobile);
    }
    if (tData.form.location) {
      formData.append('location', tData.form.location);
    } else {
      message.warn('地区不能为空');
      return;
    }
    if (tData.form.price) {
      formData.append('price', tData.form.price);
    } else {
      message.warn('价格不能为空');
      return;
    }
    formData.append('user', userId);
    formData.append('status', '2');

    if (tData.form.id) {
      updateApi(
        {
          id: tData.form.id,
        },
        formData,
      )
        .then((res) => {
          message.success('保存成功，后台审核中');
          getUserorder();
        })
        .catch((err) => {
          console.log(err);
        });
    } else {
      createApi(formData)
        .then((res) => {
          message.success('保存成功，后台审核中');
          getUserorder();
        })
        .catch((err) => {
          console.log(err);
        });
    }
    router.push({ name: 'demandView' });
  };
  const over = () => {
    if (tData.form.id) {
      if (tData.form.status == '3') {
        message.warn('需求已结束');
        return;
      } else {
        updateApi({
          id: tData.form.id,
          over: 1,
        })
          .then((res) => {
            message.success('结束成功');
            getUserorder();
          })
          .catch((err) => {
            console.log(err);
          });
      }
    } else {
      message.warn('需求未存在');
      return;
    }
    router.push({ name: 'demandView' });
  };
</script>

<style scoped lang="less">
  input,
  textarea {
    border-style: none;
    outline: none;
    margin: 0;
    padding: 0;
  }

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
      line-height: 48px;
      height: 48px;
      margin-bottom: 4px;
      border-bottom: 1px solid #cedce4;
    }

    .edit-view {
      .item {
        -webkit-box-align: center;
        -ms-flex-align: center;
        align-items: center;
        margin: 24px 0;

        .label {
          width: 100px;
          color: #152844;
          font-weight: 600;
          font-size: 14px;
        }

        .right-box {
          -webkit-box-flex: 1;
          -ms-flex: 1;
          flex: 1;
        }
        .radio-group {
          display: flex;
          flex: 1;
          width: 340px;
          height: 40px;
        }
        .radio {
          display: flex;
          flex: 1;
          line-height: 40px;
        }
        .avatar {
          width: 64px;
          height: 64px;
          border-radius: 50%;
          margin-right: 16px;
        }

        .change-tips {
          -webkit-box-align: center;
          -ms-flex-align: center;
          align-items: center;
          -ms-flex-wrap: wrap;
          flex-wrap: wrap;
        }

        label {
          color: #4684e2;
          font-size: 14px;
          line-height: 22px;
          height: 22px;
          cursor: pointer;
          width: 100px;
          display: block;
        }

        .tip {
          color: #6f6f6f;
          font-size: 14px;
          height: 22px;
          line-height: 22px;
          margin: 0;
          width: 100%;
        }

        .input-dom {
          width: 300px;
        }

        .input-dom {
          background: #f8fafb;
          border-radius: 4px;
          height: 40px;
          line-height: 40px;
          font-size: 14px;
          color: #152844;
          padding: 0 12px;
        }

        .tip {
          font-size: 12px;
          line-height: 16px;
          color: #6f6f6f;
          height: 16px;
          margin-top: 4px;
        }

        .intro {
          resize: none;
          background: #f8fafb;
          width: 100%;
          padding: 8px 12px;
          height: 100px;
          line-height: 22px;
          font-size: 14px;
          color: #152844;
        }
      }

      .save {
        background: #4684e2;
        border-radius: 32px;
        width: 96px;
        height: 32px;
        line-height: 32px;
        font-size: 14px;
        color: #fff;
        border: none;
        outline: none;
        cursor: pointer;
      }

      .mg {
        margin-left: 100px;
      }
    }
  }
</style>
