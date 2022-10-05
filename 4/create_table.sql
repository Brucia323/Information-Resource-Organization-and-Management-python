create table irom.dbo.债务汇总数据找错 (
  年度 nvarchar(max),
  行政区划 nvarchar(max),
  债务类型 nvarchar(max),
  金额 int,
  单位 nvarchar(max)
);
GO

create table irom.dbo.数据找错原始数据 (
  年度 int,
  学校类型 nvarchar(max),
  县名 nvarchar(max),
  城乡区划 nvarchar(max),
  统计指标 nvarchar(max),
  统计量 int,
  统计单位 nvarchar(max)
);
GO

create table irom.dbo.某税务机关征税数据 (
  企业代码 nvarchar(max),
  企业名称 nvarchar(max),
  行业 nvarchar(max),
  法人代表 nvarchar(max),
  企业地址 nvarchar(max),
  联系方式 float(53),
  产值 int,
  征收比例 float(53),
  征收额 int
);
GO

create table irom.dbo.贷款发放明细表 (
  合同编码 nvarchar(max),
  信贷客户编号 float(53),
  合同开始日 nvarchar(max),
  合同到期日 nvarchar(max),
  合同金额 nvarchar(max),
  保证人编号 float(53),
  保证金额 nvarchar(max),
  贷款余额 nvarchar(max),
  逾期余额 nvarchar(max),
  呆滞余额 nvarchar(max),
  呆帐余额 nvarchar(max)
);
GO

