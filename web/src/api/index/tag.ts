import { get, post } from '/@/utils/http/axios';

enum URL {
  list = '/tutor/index/tag/list',
  countlist = '/tutor/index/tag/countlist',
}

const listApi = async (params: any) => get<any>({ url: URL.list, params: params, data: {}, headers: {} });
const countlistApi = async (params: any) => get<any>({ url: URL.countlist, params: params, data: {}, headers: {} });

export { listApi, countlistApi };
