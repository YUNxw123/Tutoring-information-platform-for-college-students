// 权限问题后期增加
import { get, post } from '/@/utils/http/axios';
import { UserState } from '/@/store/modules/user/types';
// import axios from 'axios';
enum URL {
  list = '/tutor/index/order/list',
  detail = '/tutor/index/order/detail',
  addWishUser = '/tutor/index/order/addWishUser',
  getWishorderList = '/tutor/index/order/getWishorderList',
  removeWishUser = '/tutor/index/order/removeWishUser',
  listUserorder = '/tutor/index/order/listUserorder',
  create = '/tutor/index/order/create',
  update = '/tutor/index/order/update',
  delete = '/tutor/index/order/delete',
}

const listApi = async (params: any) => get<any>({ url: URL.list, params: params, data: {}, headers: {} });
const detailApi = async (params: any) => get<any>({ url: URL.detail, params: params, headers: {} });
const addWishUserApi = async (params: any) => post<any>({ url: URL.addWishUser, params: params, headers: {} });
const getWishorderListApi = async (params: any) => get<any>({ url: URL.getWishorderList, params: params, headers: {} });
const deleteApi = async (params: any) => post<any>({ url: URL.delete, params: params, headers: {} });

const removeWishUserApi = async (params: any) => post<any>({ url: URL.removeWishUser, params: params, headers: {} });

const listUserorderApi = async (params: any) => get<any>({ url: URL.listUserorder, params: params, data: {}, headers: {} });
const createApi = async (data: any) =>
  post<any>({ url: URL.create, params: {}, data: data, headers: { 'Content-Type': 'multipart/form-data;charset=utf-8' } });
const updateApi = async (params: any, data: any) =>
  post<any>({ url: URL.update, params: params, data: data, headers: { 'Content-Type': 'multipart/form-data;charset=utf-8' } });

export { listApi, detailApi, addWishUserApi, getWishorderListApi, removeWishUserApi, listUserorderApi, createApi, updateApi, deleteApi };
