--分析类别: 统计类
--分析方法: 检查

create view 中间表_最后交保记录 as
select *
from ( select t.*, row_number() over (partition by 人员编码 order by 本次终止日期 desc) as rn from zgyl_03 t ) as [t.*r]
where rn = 1;

create view 中间表_职工养老人员单位表 as
select a.*, b.单位编码, t1.单位名称 as 单位名称
from zgyl_02 a
         join 中间表_最后交保记录 b on a.人员编码 = b.人员编码
         join zgyl_01 t1 on b.单位编码 = t1.单位编码
where len(离退休类别) > 0
  and charindex(离退休类别, N'正常') = 0
  and (离退休类别 = N'因病退休' or 离退休类别 = N'因病退职' or 离退休类别 = N'特殊工种' or 离退休类别 = N'提前退休');

create view 集中同单位同时间提前退休 as
select a.*
from 中间表_职工养老人员单位表 A
         join ( select 单位名称, 离退休日期
                from 中间表_职工养老人员单位表
                group by 单位名称, 离退休日期
                having count(1) > 10 ) B on A.单位名称 = B.单位名称 and A.离退休日期 = B.离退休日期;

create view 退休后ZG交公积金 as
select 经办机构代码,
       经办机构名称,
       a.行政区划代码,
       人员编码,
       社会保障号码,
       a.姓名,
       a.证件号码,
       个人身份,
       特殊人群标识,
       参加工作日期,
       视同缴费月数,
       实际缴费月数,
       离退休日期,
       离退休类别,
       死亡日期,
       个人账户余额,
       行政区划名称,
       业务年度,
       操作中心名称,
       操作管理部名称,
       操作承办银行名称,
       交易渠道类型,
       个人账号,
       b.姓名 姓名_公积金,
       账户类型,
       单位名称,
       记账日期,
       借贷标志,
       上年结转发生额,
       当年归集发生额,
       发生额,
       发生利息额,
       上年余额,
       本年余额,
       账户余额,
       交易码,
       归集和提取业务类型,
       摘要信息,
       汇补缴年月,
       汇补缴原因,
       提取原因,
       提取方式,
       业务凭证号,
       操作时间,
       业务流水号,
       流水序号,
       资金结算类型,
       开户中心归属账务机构,
       财务记账凭证生成状态,
       财务记账凭证号,
       冲账标识,
       有效标志,
       备注,
       时间戳
from zgyl_02 a
         join gjj b on a.证件号码 = b.证件号码
where a.离退休类别 in (N'因病退休', N'因病退职', N'提前退休', N'特殊工种')
  and charindex(b.归集和提取业务类型, N'汇缴') > 0
  and 离退休日期 - replace(substring(汇补缴年月, 1, 6), '-', '') > 1;
