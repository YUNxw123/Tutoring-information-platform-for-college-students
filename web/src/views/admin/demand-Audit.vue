<template>
  <div>
    <!--页面区域-->
    <div class="page-view">
      <div class="table-operations">
        <a-space>
          <a-button @click="handleBatchAudit_pass">批量通过</a-button>
          <a-button @click="handleBatchAudit_unpass">批量不通过</a-button>
          <a-input-group class="a-input-group">
            <a-select class="searchtype" defaultValue="n" v-model:value="search_type">
              <a-select-option label="名称" value="n">名称</a-select-option>
              <a-select-option label="年级" value="c">年级</a-select-option>
              <a-select-option label="科目" value="t">科目</a-select-option>
            </a-select>
            <a-input-search enter-button @search="onSearch" @change="onSearchChange" />
          </a-input-group>
          <!--          <div>{{ search_type }}</div>-->
        </a-space>
      </div>
      <a-table
        size="middle"
        rowKey="id"
        :loading="data.loading"
        :columns="columns"
        :data-source="data.dataList"
        :scroll="{ x: 'max-content' }"
        :row-selection="rowSelection"
        :pagination="{
          size: 'default',
          current: data.page,
          pageSize: data.pageSize,
          onChange: (current) => (data.page = current),
          showSizeChanger: false,
          showTotal: (total) => `共${total}条数据`,
        }"
      >
        <template #bodyCell="{ record, column }">
          <template v-if="column.key === 'operation'">
            <span>
              <a @click="confirmAudit_pass(record)">通过</a>
              <a-divider type="vertical" />
              <a @mouseover="handleEdit(record)">查看/编辑</a>
              <a-divider type="vertical" />
              <a-popconfirm title="确定不通过?" ok-text="是" cancel-text="否" @confirm="confirmAudit_unpass(record)">
                <a href="#">不通过</a>
              </a-popconfirm>
            </span>
          </template>
        </template>
      </a-table>
    </div>

    <!--弹窗区域-->
    <div>
      <div>
        <a-modal
          :visible="modal.visile"
          :forceRender="true"
          :title="modal.title"
          :body-style="bodystyle"
          width="880px"
          ok-text="确认"
          cancel-text="取消"
          @cancel="handleCancel"
          @ok="handleOk"
        >
          <div>
            <a-form ref="myform" :label-col="{ style: { width: '80px' } }" :model="modal.form" :rules="modal.rules">
              <a-row :gutter="24">
                <a-col span="24">
                  <a-form-item label="用户" name="username">
                    <a-input readonly v-model:value="modal.form.username" style="width: 100%" :bordered="false" />
                  </a-form-item>
                </a-col>
                <a-col span="12">
                  <a-form-item label="手机号" name="mobile">
                    <a-input-number placeholder="请输入" :min="0" v-model:value="modal.form.mobile" style="width: 100%" />
                  </a-form-item>
                </a-col>
                <a-col span="12">
                  <a-form-item label="所在地区" name="location">
                    <a-cascader v-model:value="modal.form.location" :options="city" placeholder="请选择地区" />
                  </a-form-item>
                </a-col>
                <a-col span="12">
                  <a-form-item label="年级" name="classification">
                    <a-select
                      placeholder="请选择"
                      allowClear
                      :options="modal.cData"
                      :field-names="{ label: 'title', value: 'id' }"
                      v-model:value="modal.form.classification"
                    />
                  </a-form-item>
                </a-col>
                <a-col span="12">
                  <a-form-item label="科目" name="tag">
                    <a-select mode="multiple" placeholder="请选择" allowClear v-model:value="modal.form.tag">
                      <template v-for="item in modal.tagData">
                        <a-select-option :value="item.id">{{ item.title }}</a-select-option>
                      </template>
                    </a-select>
                  </a-form-item>
                </a-col>
                <a-col span="12">
                  <a-form-item label="家教价格" name="price">
                    <a-input-number placeholder="请输入" :min="0" v-model:value="modal.form.price" style="width: 100%" />
                  </a-form-item>
                </a-col>
                <a-col span="12">
                  <a-form-item label="家教性别" name="sex">
                    <a-select placeholder="请选择" allowClear v-model:value="modal.form.sex" style="width: 100%">
                      <a-select-option key="M" value="M">男</a-select-option>
                      <a-select-option key="F" value="F">女</a-select-option>
                      <a-select-option key="N" value="N">无要求</a-select-option>
                    </a-select>
                  </a-form-item>
                </a-col>
                <a-col span="12">
                  <a-form-item label="状态" name="status">
                    <a-select placeholder="请选择" allowClear v-model:value="modal.form.status">
                      <a-select-option key="0" value="0">上架</a-select-option>
                      <a-select-option key="1" value="1">下架</a-select-option>
                      <a-select-option key="2" value="2">待审核</a-select-option>
                      <a-select-option key="3" value="3">已结束</a-select-option>
                    </a-select>
                  </a-form-item>
                </a-col>
                <a-col span="24">
                  <a-form-item label="需求简介">
                    <a-textarea placeholder="请输入" v-model:value="modal.form.description" />
                  </a-form-item>
                </a-col>
                <!--                <a-col span="24">-->
                <!--                  <a-form-item label="已预约家教" name="thing">-->
                <!--                    <a-select mode="multiple" placeholder="请选择" allowClear v-model:value="modal.form.thing">-->
                <!--                      <template v-for="item in modal.thingData">-->
                <!--                        <a-select-option :value="item.id">{{ item.title }}</a-select-option>-->
                <!--                      </template>-->
                <!--                    </a-select>-->
                <!--                  </a-form-item>-->
                <!--                </a-col>-->
              </a-row>
            </a-form>
          </div>
        </a-modal>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { FormInstance, message, CascaderProps } from 'ant-design-vue';
  import { auditlistApi, updateApi, audit_passApi } from '/@/api/admin/order';
  import { listApi as listClassificationApi } from '/@/api/admin/classification';
  import { listApi as listTagApi } from '/@/api/admin/tag';
  import { listApi as listThingApi } from '/@/api/admin/thing';
  import city from '/@/assets/cities.json';

  const columns = reactive([
    {
      title: '序号',
      dataIndex: 'index',
      key: 'index',
      width: 60,
    },
    {
      title: '用户名',
      dataIndex: 'username',
      key: 'username',
      align: 'center',
    },
    {
      title: '价格',
      dataIndex: 'price',
      key: 'price',
      customRender: ({ text, record, index, column }) => (text === '0元/时' ? '免费' : text),
    },
    {
      title: '手机号',
      dataIndex: 'mobile',
      key: 'mobile',
    },
    {
      title: '所在地区',
      dataIndex: 'location',
      key: 'location',
    },
    {
      title: '简介',
      dataIndex: 'description',
      key: 'description',
      customRender: ({ text }) => (text ? text.substring(0, 10) + '...' : '--'),
    },
    {
      title: '状态',
      dataIndex: 'status',
      key: 'status',
      customRender: ({ text }) => {
        if (text === '0') {
          return '上架';
        } else if (text === '1') {
          return '下架';
        } else if (text === '2') {
          return '待审核';
        } else {
          return '已结束';
        }
      },
    },
    {
      title: '操作',
      dataIndex: 'action',
      key: 'operation',
      align: 'center',
      fixed: 'right',
      width: 180,
    },
  ]);
  // 页面数据
  const data = reactive({
    dataList: [],
    loading: false,
    keyword: '',
    selectedRowKeys: [] as any[],
    pageSize: 10,
    page: 1,
  });

  // 弹窗数据源
  const modal = reactive({
    visile: false,
    editFlag: false,
    title: '',
    uData: [],
    cData: [],
    tagData: [{}],
    thingData: [{}],
    form: {
      id: undefined,
      username: undefined,
      classification: undefined,
      tag: [],
      thing: [],
      price: undefined,
      mobile: undefined,
      sex: undefined,
      location: undefined,
      status: undefined,
    },
    rules: {
      classification: [{ required: true, message: '请选择分类', trigger: 'change' }],
      location: [{ required: true, message: '请选择地区', trigger: 'change' }],
      tag: [{ type: 'array', required: true, message: '请至少选择一个科目', trigger: 'change' }],
      price: [{ required: true, message: '请输入定价', trigger: 'change' }],
      mobile: [
        { required: true, message: '请输入手机号', trigger: 'blur' },
        { pattern: /^1[3|4|5|6|7|8|9][0-9]\d{8}$/, message: '请输入正确的手机号码', trigger: 'blur' },
      ],
      sex: [{ required: true, message: '请选择性别', trigger: 'change' }],
      status: [{ required: true, message: '请选择状态', trigger: 'change' }],
    },
  });

  const bodystyle = {
    height: '500px',
    overflow: 'hidden',
    overflowY: 'scroll',
  };

  const myform = ref<FormInstance>();

  onMounted(() => {
    getDataList();
    getThingDataList();
    getCDataList();
    getTagDataList();
  });

  const search_type = ref<string>('n');
  const getDataList = () => {
    data.loading = true;
    auditlistApi({
      keyword: data.keyword,
      search_type: search_type.value,
    })
      .then((res) => {
        data.loading = false;
        console.log(res);
        res.data.forEach((item: any, index: any) => {
          item.index = index + 1;
          item.price = item.price + '元/时';
        });
        data.dataList = res.data;
      })
      .catch((err) => {
        data.loading = false;
        console.log(err);
      });
  };

  const getCDataList = () => {
    listClassificationApi({}).then((res) => {
      modal.cData = res.data;
    });
  };
  const getTagDataList = () => {
    listTagApi({}).then((res) => {
      res.data.forEach((item, index) => {
        item.index = index + 1;
      });
      modal.tagData = res.data;
    });
  };
  const getThingDataList = () => {
    listThingApi({}).then((res) => {
      res.data.forEach((item, index) => {
        item.index = index + 1;
      });
      modal.thingData = res.data;
    });
  };

  const onSearchChange = (e: Event) => {
    data.keyword = e?.target?.value;
    console.log(data.keyword);
  };

  const onSearch = () => {
    getDataList();
  };

  const rowSelection = ref({
    onChange: (selectedRowKeys: (string | number)[], selectedRows: DataItem[]) => {
      console.log(`selectedRowKeys: ${selectedRowKeys}`, 'selectedRows: ', selectedRows);
      data.selectedRowKeys = selectedRowKeys;
    },
  });

  const handleEdit = (record: any) => {
    resetModal();
    modal.visile = true;
    modal.editFlag = true;
    modal.title = '查看/编辑';
    // 重置
    for (const key in modal.form) {
      modal.form[key] = undefined;
    }
    for (const key in record) {
      if (record[key]) {
        modal.form[key] = record[key];
      }
    }
  };

  const confirmAudit_pass = (record: any) => {
    console.log('audit_pass', record);
    audit_passApi({ ids: record.id, type: 1 })
      .then((res) => {
        getDataList();
      })
      .catch((err) => {
        message.error(err.msg || '操作失败');
      });
  };
  const confirmAudit_unpass = (record: any) => {
    console.log('audit_pass', record);
    audit_passApi({ ids: record.id, type: 2 })
      .then((res) => {
        getDataList();
      })
      .catch((err) => {
        message.error(err.msg || '操作失败');
      });
  };

  const handleBatchAudit_pass = () => {
    console.log(data.selectedRowKeys);
    if (data.selectedRowKeys.length <= 0) {
      console.log('hello');
      message.warn('请勾选想要通过的家教项');
      return;
    }
    audit_passApi({ ids: data.selectedRowKeys.join(','), type: 1 })
      .then((res) => {
        message.success('通过成功');
        data.selectedRowKeys = [];
        getDataList();
      })
      .catch((err) => {
        message.error(err.msg || '操作失败');
      });
  };
  const handleBatchAudit_unpass = () => {
    console.log(data.selectedRowKeys);
    if (data.selectedRowKeys.length <= 0) {
      console.log('hello');
      message.warn('请勾选想要通过的家教项');
      return;
    }
    audit_passApi({ ids: data.selectedRowKeys.join(','), type: 2 })
      .then((res) => {
        message.success('通过成功');
        data.selectedRowKeys = [];
        getDataList();
      })
      .catch((err) => {
        message.error(err.msg || '操作失败');
      });
  };

  const handleOk = () => {
    myform.value
      ?.validate()
      .then(() => {
        const formData = new FormData();
        if (modal.editFlag) {
          formData.append('id', modal.form.id);
        }
        if (modal.form.classification) {
          formData.append('classification', modal.form.classification);
        }
        if (modal.form.tag) {
          modal.form.tag.forEach(function (value) {
            if (value) {
              formData.append('tag', value);
            }
          });
        }
        if (modal.form.thing) {
          modal.form.thing.forEach(function (value) {
            if (value) {
              formData.append('thing', value);
            }
          });
        }
        formData.append('description', modal.form.description || '');

        formData.append('price', parseInt(modal.form.price) || '0');

        if (modal.form.mobile) {
          formData.append('mobile', modal.form.mobile);
        }
        if (modal.form.sex) {
          formData.append('sex', modal.form.sex);
        }
        if (modal.form.location) {
          formData.append('location', modal.form.location);
        }
        if (modal.form.status) {
          formData.append('status', modal.form.status);
        }
        if (modal.editFlag) {
          updateApi(
            {
              id: modal.form.id,
            },
            formData,
          )
            .then((res) => {
              hideModal();
              getDataList();
            })
            .catch((err) => {
              console.log(err);
              message.error(err.msg || '操作失败');
            });
        }
      })
      .catch((err) => {
        console.log('不能为空');
      });
  };

  const handleCancel = () => {
    hideModal();
  };

  // 恢复表单初始状态
  const resetModal = () => {
    myform.value?.resetFields();
  };

  // 关闭弹窗
  const hideModal = () => {
    modal.visile = false;
  };
</script>

<style scoped lang="less">
  .page-view {
    min-height: 100%;
    background: #fff;
    padding: 24px;
    display: flex;
    flex-direction: column;
  }

  .table-operations {
    margin-bottom: 16px;
    text-align: right;
  }

  .table-operations > button {
    margin-right: 8px;
  }
  .a-input-group {
    display: flex;
    flex-direction: row;
    align-items: center;
  }
  .searchtype {
    width: auto;
  }
</style>
