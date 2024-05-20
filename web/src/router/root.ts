// 路由表
const constantRouterMap = [
  // ************* 前台路由 **************
  {
    path: '/',
    redirect: '/index',
  },
  {
    path: '/index',
    name: 'index',
    redirect: '/index/portal',
    component: () => import('/@/views/index/index.vue'),
    children: [
      {
        path: 'login',
        name: 'login',
        component: () => import('/@/views/index/login.vue'),
      },
      {
        path: 'register',
        name: 'register',
        component: () => import('/@/views/index/register.vue'),
      },
      {
        path: 'portal',
        name: 'portal',
        component: () => import('/@/views/index/portal.vue'),
      },
      {
        path: 'tutor',
        name: 'tutor',
        component: () => import('/@/views/index/tutor.vue'),
      },
      {
        path: 'detail',
        name: 'detail',
        component: () => import('/@/views/index/detail.vue'),
      },
      {
        path: 'particulars',
        name: 'particulars',
        component: () => import('/@/views/index/particulars.vue'),
      },
      {
        path: 'demand',
        name: 'demand',
        component: () => import('/@/views/index/demand.vue'),
      },
      {
        path: 'search',
        name: 'search',
        component: () => import('/@/views/index/search.vue'),
      },
      {
        path: 'tutor',
        name: 'tutor',
        component: () => import('/@/views/index/tutor.vue'),
      },
      {
        path: 'usercenter',
        name: 'usercenter',
        redirect: '/index/usercenter/userInfoEditView',
        component: () => import('/@/views/index/usercenter.vue'),
        children: [
          {
            path: 'wishorderView',
            name: 'wishorderView',
            component: () => import('/@/views/index/user/wish-order-view.vue'),
          },
          {
            path: 'collectThingView',
            name: 'collectThingView',
            component: () => import('/@/views/index/user/collect-thing-view.vue'),
          },
          {
            path: 'jiajiaoEditView',
            name: 'jiajiaoEditView',
            component: () => import('/@/views/index/user/jiajiao-edit-view.vue'),
          },
          {
            path: 'demandView',
            name: 'demandView',
            component: () => import('/@/views/index/user/demand-view.vue'),
          },
          {
            path: 'demandEditView',
            name: 'demandEditView',
            component: () => import('/@/views/index/user/demand-edit-view.vue'),
          },
          {
            path: 'userInfoEditView',
            name: 'userInfoEditView',
            component: () => import('/@/views/index/user/userinfo-edit-view.vue'),
          },
          {
            path: 'commentView',
            name: 'commentView',
            component: () => import('/@/views/index/user/comment-view.vue'),
          },
          {
            path: 'securityView',
            name: 'securityView',
            component: () => import('/@/views/index/user/security-view.vue'),
          },
          {
            path: 'pushView',
            name: 'pushView',
            component: () => import('/@/views/index/user/push-view.vue'),
          },
          {
            path: 'messageView',
            name: 'messageView',
            component: () => import('/@/views/index/user/message-view.vue'),
          },
        ],
      },
    ],
  },
  {
    path: '/adminLogin',
    name: 'adminLogin',
    component: () => import('/@/views/admin/admin-login.vue'),
  },
  {
    path: '/admin',
    name: 'admin',
    redirect: '/admin/user',
    component: () => import('/@/views/admin/main.vue'),
    children: [
      { path: 'overview', name: 'overview', component: () => import('/@/views/admin/overview.vue') },
      { path: 'thing', name: 'thing', component: () => import('/@/views/admin/thing.vue') },
      { path: 'order', name: 'order', component: () => import('/@/views/admin/demand.vue') },
      { path: 'commenttutor', name: 'commenttutor', component: () => import('/@/views/admin/comment-tutor.vue') },
      { path: 'commentdemand', name: 'commentdemand', component: () => import('/@/views/admin/comment-demand.vue') },
      { path: 'user', name: 'user', component: () => import('/@/views/admin/user.vue') },
      { path: 'classification', name: 'classification', component: () => import('/@/views/admin/classification.vue') },
      { path: 'tag', name: 'tag', component: () => import('/@/views/admin/tag.vue') },
      { path: 'ad', name: 'ad', component: () => import('/@/views/admin/ad.vue') },
      { path: 'notice', name: 'notice', component: () => import('/@/views/admin/notice.vue') },
      { path: 'loginLog', name: 'loginLog', component: () => import('/@/views/admin/login-log.vue') },
      { path: 'opLog', name: 'opLog', component: () => import('/@/views/admin/op-log.vue') },
      { path: 'errorLog', name: 'errorLog', component: () => import('/@/views/admin/error-log.vue') },
      { path: 'sysInfo', name: 'sysInfo', component: () => import('/@/views/admin/sys-info.vue') },
      { path: 'tutoraudit', name: 'tutoraudit', component: () => import('/@/views/admin/tutor-Audit.vue') },
      { path: 'demandaudit', name: 'demandaudit', component: () => import('/@/views/admin/demand-Audit.vue') },
    ],
  },
];

export default constantRouterMap;
