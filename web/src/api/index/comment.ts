import { get, post } from '/@/utils/http/axios';

enum URL {
  create = '/tutor/index/comment/create',
  listThingComments = '/tutor/index/comment/list',
  listorderComments = '/tutor/index/comment/orderlist',
  listUserComments = '/tutor/index/comment/listMyComments',
  like = '/tutor/index/comment/like',
}

const createApi = async (data: any) =>
  post<any>({
    url: URL.create,
    params: {},
    data: data,
    headers: { 'Content-Type': 'multipart/form-data;charset=utf-8' },
  });
const listThingCommentsApi = async (params: any) => get<any>({ url: URL.listThingComments, params: params, data: {}, headers: {} });
const listorderCommentsApi = async (params: any) => get<any>({ url: URL.listorderComments, params: params, data: {}, headers: {} });

const listUserCommentsApi = async (params: any) => get<any>({ url: URL.listUserComments, params: params, data: {}, headers: {} });
const likeApi = async (params: any) => post<any>({ url: URL.like, params: params, headers: {} });

export { createApi, listThingCommentsApi, listorderCommentsApi, listUserCommentsApi, likeApi };
