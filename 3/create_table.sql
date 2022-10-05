create table gjj
(
    行政区划代码         int,
    行政区划名称         nvarchar(max),
    业务年度             int,
    开户中心编号         int,
    开户中心名称         nvarchar(max),
    开户管理部编号       int,
    开户管理部名称       nvarchar(max),
    开户机构编号         nvarchar(max),
    开户承办银行         int,
    开户承办银行名称     nvarchar(max),
    操作中心编号         int,
    操作中心名称         nvarchar(max),
    操作管理部编号       int,
    操作管理部名称       nvarchar(max),
    操作机构编号         nvarchar(max),
    操作承办银行         varchar(max),
    操作承办银行名称     nvarchar(max),
    操作员编号           nvarchar(max),
    交易渠道类型         nvarchar(max),
    个人账号             float,
    客户编号             float,
    证件号码             nvarchar(max),
    姓名                 nvarchar(max),
    账户类型             nvarchar(max),
    单位账号             float,
    单位名称             nvarchar(max),
    记账日期             nvarchar(max),
    借贷标志             nvarchar(max),
    上年结转发生额       float,
    当年归集发生额       float,
    发生额               float,
    发生利息额           float,
    上年余额             float,
    本年余额             float,
    账户余额             float,
    交易码               nvarchar(max),
    归集和提取业务类型   nvarchar(max),
    摘要信息             nvarchar(max),
    汇补缴年月           nvarchar(max),
    汇补缴原因           nvarchar(max),
    提取原因             nvarchar(max),
    提取方式             nvarchar(max),
    业务凭证号           float,
    操作时间             nvarchar(max),
    业务流水号           float,
    流水序号             float,
    资金结算类型         nvarchar(max),
    开户中心归属账务机构 varchar(max),
    财务记账凭证生成状态 nvarchar(max),
    财务记账凭证号       nvarchar(max),
    冲账标识             nvarchar(max),
    有效标志             nvarchar(max),
    备注                 nvarchar(max),
    时间戳               nvarchar(max)
)
go

create table gsdj
(
    行政区划代码     int,
    行政区划名称     nvarchar(max),
    主体标识         nvarchar(max),
    主体名称         nvarchar(max),
    营业证照号码     float,
    主体类型名称     nvarchar(max),
    经营场所         nvarchar(max),
    邮政编码         int,
    经营场所电话     nvarchar(max),
    注册日期         int,
    核准日期         int,
    登记机关名称     nvarchar(max),
    行业名称         nvarchar(max),
    注册资本         float,
    实收资本         nvarchar(max),
    注册资金标准     nvarchar(max),
    经营范围         nvarchar(max),
    营业期限起       int,
    营业期限止       int,
    登记状态         nvarchar(max),
    法人代表姓名     nvarchar(max),
    法人代表国籍     nvarchar(max),
    法人证件类型名称 nvarchar(max),
    法人证件号码     nvarchar(max),
    备注             nvarchar(max)
)
go

create table jgyl_02
(
    经办机构代码                 int,
    经办机构名称                 nvarchar(max),
    行政区划代码                 int,
    人员编码                     int,
    社会保障号码                 nvarchar(max),
    姓名                         nvarchar(max),
    证件号码                     nvarchar(max),
    参加工作日期                 int,
    视同缴费月数                 nvarchar(max),
    实际缴费月数                 int,
    离退休日期                   int,
    离退休类别                   nvarchar(max),
    死亡日期                     int,
    当前基本养老保险个人账户余额 nvarchar(max),
    当前个人职业年金账户余额     nvarchar(max)
)
go

create table jgyl_06
(
    经办机构代码 int,
    经办机构名称 nvarchar(max),
    行政区划代码 int,
    单位编码     float,
    险种类型代码 int,
    人员编码     int,
    开户银行名称 nvarchar(max),
    银行账号     nvarchar(max),
    银行账户名称 nvarchar(max),
    结算年月     int,
    待遇年月     int,
    待遇项目代码 int,
    待遇项目名称 nvarchar(max),
    待遇金额     float
)
go

create table mzhh
(
    行政区划代码         nvarchar(max),
    行政区划名称         nvarchar(max),
    业务年度             int,
    死者姓名             nvarchar(max),
    身份证号             nvarchar(max),
    身份证件类型         nvarchar(max),
    登记号码             nvarchar(max),
    火化时间             nvarchar(max),
    死亡证编号           nvarchar(max),
    性别                 nvarchar(max),
    民族                 nvarchar(max),
    国家或地区           nvarchar(max),
    常住地址             nvarchar(max),
    死亡原因             nvarchar(max),
    邮编                 nvarchar(max),
    家庭电话             nvarchar(max),
    安葬时间             nvarchar(max),
    火化单位组织机构代码 int,
    火化单位名称         nvarchar(max),
    是否本地户口         nvarchar(max),
    户口所在地           nvarchar(max),
    是否重复             int
)
go

create table sfjy
(
    姓名     nvarchar(max),
    出生日期 nvarchar(max),
    队别     nvarchar(max),
    罪名     nvarchar(max),
    刑期     nvarchar(max),
    起日     nvarchar(max),
    止日     nvarchar(max),
    户籍住址 nvarchar(max),
    身份证号 nvarchar(max),
    离监日期 nvarchar(max)
)
go

create table zgyl_01
(
    经办机构代码     int,
    经办机构名称     nvarchar(max),
    行政区划代码     int,
    单位编码         float,
    单位名称         nvarchar(max),
    统一社会信用代码 nvarchar(max),
    单位类型         nvarchar(max),
    经济类型         nvarchar(max),
    所属行业         nvarchar(max),
    地址             nvarchar(max),
    单位参保日期     int,
    单位缴费状态代码 int
)
go

create table zgyl_02
(
    经办机构代码 int,
    经办机构名称 nvarchar(max),
    行政区划代码 int,
    人员编码     float,
    社会保障号码 nvarchar(max),
    姓名         nvarchar(max),
    证件号码     nvarchar(max),
    个人身份     nvarchar(max),
    特殊人群标识 nvarchar(max),
    参加工作日期 int,
    视同缴费月数 int,
    实际缴费月数 int,
    离退休日期   int,
    离退休类别   nvarchar(max),
    死亡日期     int,
    个人账户余额 float
)
go

create table zgyl_03
(
    经办机构代码     int,
    经办机构名称     nvarchar(max),
    行政区划代码     int,
    人员编码         int,
    单位编码         int,
    首次参保年月     int,
    人员参保状态代码 int,
    个人缴费状态代码 int,
    本次开始日期     int,
    本次终止日期     int
)
go

create table zgyl_05
(
    经办机构代码 int,
    经办机构名称 nvarchar(max),
    行政区划代码 int,
    单位编码     varchar(max),
    人员编码     varchar(max),
    应缴类型代码 int,
    结算年月     int,
    应缴开始年月 int,
    应缴终止年月 int,
    到账标志     int,
    到账日期     int,
    缴费基数     int,
    应缴总金额   int,
    单位应缴金额 int,
    个人应缴金额 int,
    单位缴费比例 float,
    个人缴费比例 float,
    单位实缴金额 int,
    个人实缴金额 int
)
go

