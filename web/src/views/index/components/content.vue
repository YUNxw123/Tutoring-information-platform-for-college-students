<template>
  <div class="container">
    <div class="title_text">
      <span>服务流程</span><label>Service process</label>
      <ul class="clearfix">
        <li>
          <dl>
            <dt
              ><i><img src="/src/assets/images/zuico1.png" alt="" /></i
            ></dt>
            <dd>
              <h3>1在线预约</h3>
              <p>您可以通过网站添加需求，详细描述学员的基本情况，辅导的时间安排，以及对老师的要求等。 </p>
              <img src="/src/assets/images/sanjiao_08.png" alt="" />
            </dd>
          </dl>
        </li>
        <li>
          <dl>
            <dt
              ><i><img src="/src/assets/images/zuico2.png" alt="" /></i
            ></dt>
            <dd>
              <h3>2筛选老师</h3>
              <p>我们一般会在48小时内审核发布需求，根据学员的情况、辅导的时间安排，以及您的要求，针对性地匹配合适的老师。 </p>
              <img src="/src/assets/images/sanjiao_08.png" alt="" />
            </dd>
          </dl>
        </li>
        <li>
          <dl>
            <dt
              ><i><img src="/src/assets/images/zuico3.png" alt="" /></i
            ></dt>
            <dd>
              <h3>3上门试课</h3>
              <p>若对老师简历满意，则与老师约定的时间、地点进行试课，老师上门会带好学生证、身份证等有证件并主动展示。 </p>
              <img src="/src/assets/images/sanjiao_08.png" alt="" />
            </dd>
          </dl>
        </li>
        <li>
          <dl>
            <dt
              ><i><img src="/src/assets/images/zuico4.png" alt="" /></i
            ></dt>
            <dd>
              <h3>4正式授课</h3>
              <p>试讲成功，则按与老师约定的时间正常授课即可，大学生家教信息平台定期进行回访，对教员进行监督，保证教员的教学质量。 </p>
              <img src="/src/assets/images/sanjiao_08.png" alt="" />
            </dd>
          </dl>
        </li>
      </ul>
    </div>
    <div class="title_txt">
      <span>教学优势</span><label>Teaching advantage</label>
      <ul class="clearfix ysss">
        <li>
          <h6>为什么 <span>我们 值得选择！</span></h6>
        </li>

        <li>
          <h1>价格优惠，辅导成本更低</h1>
          <p>大学生家教信息平台对学员免收服务费，大学生家教课时费用仅为机构1/3-1/2，不用预付课时费用，最大程度的节省成本支出。</p>
          <div>
            <img src="/src/assets/images/bianjiao_03.png" alt="" />
            <b>1</b>
          </div>
        </li>

        <li>
          <h1>海量教员，老师质量更高</h1>
          <p>大学生家教信息平台建立完善的校园教员渠道体系，在全国各重点本科、师范院校皆有海量教员可供选择。</p>
          <div>
            <img src="/src/assets/images/bianjiao_03.png" alt="" />
            <b>2</b>
          </div>
        </li>

        <li>
          <h1>专业团队，响应速度更快</h1>
          <p>大学生家教信息平台是全国连锁，专业的上门家教品牌，7*24小时服务，快速响应您的需求，一般48小时内，最快1小时安排到老师。</p>
          <div>
            <img src="/src/assets/images/bianjiao_03.png" alt="" />
            <b>3</b>
          </div>
        </li>

        <li>
          <h1>一对一辅导，教学个性化</h1>
          <p>大学生家教信息平台推荐大学生一对一上门辅导，省时省力，个性化教学，可培养学习习惯，掌握学习方法，全面提高学习成绩。</p>
          <div>
            <img src="/src/assets/images/bianjiao_03.png" alt="" />
            <b>4</b>
          </div>
        </li>

        <li>
          <h1>一站式服务，便捷找老师</h1>
          <p>大学生家教信息平台提供一站式服务，只需通过网站预约，我们即将安排老师上门辅导，免费试讲，满意为止。</p>
          <div>
            <img src="/src/assets/images/bianjiao_03.png" alt="" />
            <b>5</b>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Content',
  };
</script>

<style scoped>
  .container {
    width: 1200px;
    margin: 0 auto;
  }
  .title_text,
  .title_txt {
    width: 100%;
    margin: 40px 0;
  }
  .title_text > span,
  .title_txt > span {
    font-size: 22px;
    margin-right: 20px;
  }
  .title_text > label,
  .title_txt > label {
    font-size: 18px;
    color: #4f4f4f;
  }
  .title_text ul {
    padding: 40px 0;
    list-style: none;
  }

  .clearfix {
    display: block;
  }

  .title_text li {
    width: 25%;
    float: left;
  }
  .title_text li i img {
    display: inline-block;
  }
  .title_text li i {
    display: block;
    width: 65px;
    height: 65px;
    text-align: center;
    line-height: 65px;
    border: 1px solid #c3c3c3;
    border-radius: 50%;
    -webkit-border-radius: 50%;
    -moz-border-radius: 50%;
    -ms-border-radius: 50%;
    -o-border-radius: 50%;
    transition: 1s;
  }

  .title_text li:hover i {
    transform: rotate(360deg);
    -webkit-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -ms-transform: rotate(360deg);
    -o-transform: rotate(360deg);
  }

  .title_text li dt,
  .title_text li dd {
    display: block;
    float: left;
  }
  .title_text li dd {
    width: 60%;
    padding-left: 20px;
    position: relative;
  }

  .title_text li dd img {
    position: absolute;
    right: -15px;
    top: 20px;
  }
  .title_text li:last-child dd img {
    display: none;
  }
  .title_text h3 {
    font-size: 18px;
    color: #4f4f4f;
    margin-bottom: 8px;
    margin-top: 10px;
  }
  .title_text p {
    font-size: 12px;
    color: #797979;
    line-height: 20px;
  }
  .title_txt ul {
    margin-top: 30px;
  }
  .title_txt li {
    width: 33.3333333%;
    float: left;
    height: 130px;
    box-sizing: border-box;
    border: 1px solid #e5e5e5;
    padding: 30px;
    position: relative;
    transition: 0.2s;
  }
  .title_txt h6 {
    font-size: 24px;
    color: #f9b04e;
    font-weight: 400;
    line-height: 70px;
    text-align: center;
  }
  .title_txt h6 span {
    font-weight: bold;
  }
  .title_txt li h1 {
    font-size: 18px;
    margin-bottom: 10px;
    font-weight: 400;
    transition: 0.2s;
  }
  .title_txt li p {
    font-size: 12px;
    line-height: 20px;
  }
  .title_txt li div {
    position: absolute;
    top: -1px;
    right: -1px;
    background: #f7b04f;
    transition: 0.2s;
  }
  .title_txt li div b {
    font-size: 16px;
    color: #ffffff;
    position: absolute;
    top: 5px;
    right: 7px;
  }
  .title_txt li:hover {
    box-shadow: 6px 6px 10px #f3f3f3, -6px -6px 10px #f3f3f3;
  }
  .title_txt li:hover h1 {
    color: #267fff;
  }
  .title_txt li:hover div {
    background: #267fff;
  }
</style>
