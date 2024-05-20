import { get } from '/@/utils/http/axios';

enum URL {
  list = '/tutor/index/ad/list',
}

const listApi = async (params: any) => get<any>({ url: URL.list, params: params, data: {}, headers: {} });

export { listApi };
