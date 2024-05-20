// 权限问题后期增加
import { get, post } from '/@/utils/http/axios';
import { UserState } from '/@/store/modules/user/types';
// import axios from 'axios';
enum URL {
  list = '/tutor/admin/order/list',
  auditlist = '/tutor/admin/order/auditlist',
  create = '/tutor/admin/order/create',
  update = '/tutor/admin/order/update',
  delete = '/tutor/admin/order/delete',
  audit_pass = '/tutor/admin/order/audit_pass',
  detail = '/api/order/detail',
}

const listApi = async (params: any) => get<any>({ url: URL.list, params: params, data: {}, headers: {} });
const auditlistApi = async (params: any) => get<any>({ url: URL.auditlist, params: params, data: {}, headers: {} });
const createApi = async (data: any) =>
  post<any>({ url: URL.create, params: {}, data: data, headers: { 'Content-Type': 'multipart/form-data;charset=utf-8' } });
const updateApi = async (params: any, data: any) =>
  post<any>({ url: URL.update, params: params, data: data, headers: { 'Content-Type': 'multipart/form-data;charset=utf-8' } });
const deleteApi = async (params: any) => post<any>({ url: URL.delete, params: params, headers: {} });
const audit_passApi = async (params: any) => post<any>({ url: URL.audit_pass, params: params, headers: {} });
const detailApi = async (params: any) => get<any>({ url: URL.detail, params: params, headers: {} });

export { listApi, createApi, updateApi, deleteApi, detailApi, auditlistApi, audit_passApi };
