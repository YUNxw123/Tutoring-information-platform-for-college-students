// 权限问题后期增加
import { get, post } from '/@/utils/http/axios';
import { UserState } from '/@/store/modules/user/types';
// import axios from 'axios';
enum URL {
  list = '/tutor/index/thing/list',
  detail = '/tutor/index/thing/detail',
  addWishUser = '/tutor/index/thing/addWishUser',
  addCollectUser = '/tutor/index/thing/addCollectUser',
  getCollectThingList = '/tutor/index/thing/getCollectThingList',
  getWishThingList = '/tutor/index/thing/getWishThingList',
  removeCollectUser = '/tutor/index/thing/removeCollectUser',
  removeWishUser = '/tutor/index/thing/removeWishUser',
  listUserThing = '/tutor/index/thing/listUserThing',
  create = '/tutor/index/thing/create',
  update = '/tutor/index/thing/update',
}

const listApi = async (params: any) => get<any>({ url: URL.list, params: params, data: {}, headers: {} });
const detailApi = async (params: any) => get<any>({ url: URL.detail, params: params, headers: {} });
const addCollectUserApi = async (params: any) => post<any>({ url: URL.addCollectUser, params: params, headers: {} });
const getCollectThingListApi = async (params: any) => get<any>({ url: URL.getCollectThingList, params: params, headers: {} });

const removeCollectUserApi = async (params: any) => post<any>({ url: URL.removeCollectUser, params: params, headers: {} });

const listUserThingApi = async (params: any) => get<any>({ url: URL.listUserThing, params: params, data: {}, headers: {} });
const createApi = async (data: any) =>
  post<any>({ url: URL.create, params: {}, data: data, headers: { 'Content-Type': 'multipart/form-data;charset=utf-8' } });
const updateApi = async (params: any, data: any) =>
  post<any>({ url: URL.update, params: params, data: data, headers: { 'Content-Type': 'multipart/form-data;charset=utf-8' } });

export {
  listApi,
  detailApi,
  addCollectUserApi,
  getCollectThingListApi,
  removeCollectUserApi,
  listUserThingApi,
  createApi,
  updateApi,
};
