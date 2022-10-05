--分析类别: 统计类
--分析方法: 检查

create view 机关火化人员名单 as
select a.*, b.火化时间
from jgyl_02 a
         join mzhh b on a.证件号码 = b.身份证号;

create view 机关最大待遇领取年月 as
select 人员编码, max(待遇年月) as 待遇年月
from jgyl_06
where 待遇项目代码 not in (100501, 100502, 200030, 200070, 400100, 400040, 600100)
group by 人员编码;

select *
from 机关火化人员名单 a
         left join 机关最大待遇领取年月 b
                   on a.人员编码 = b.人员编码 and replace(substring(火化时间, 1, 6), '-', '0') < 待遇年月;

create view yl_死亡后多领待遇JGYL as
select a.*, b.死亡后各月待遇年月, b.待遇金额
from ( select a.*, b.待遇年月 最大待遇年月
       from 机关火化人员名单 a
                inner join 机关最大待遇领取年月 b on a.人员编码 = b.人员编码 and
                                                     replace(substring(a.火化时间, 1, 6), '-', '0') < b.待遇年月 ) a
         left join ( select 人员编码, 待遇年月 死亡后各月待遇年月, sum(待遇金额) 待遇金额
                     from jgyl_06
                     group by 人员编码, 待遇年月 ) b on a.人员编码 = b.人员编码
where replace(substring(a.火化时间, 1, 6), '-', '0') < b.死亡后各月待遇年月;

select count(*)
from sfjy
where 身份证号 is not null
  and 身份证号 <> N'无'
  and (户籍住址 like N'福建%' or 身份证号 like '35%');

create view yl_全省服刑人员_服刑期间发生 as
select 姓名,
       出生日期,
       队别,
       罪名,
       刑期,
       起日,
       止日,
       户籍住址,
       离监日期,
       身份证号,
       cast(cast(replace(replace(replace(起日, N'年', '-'), N'月', '-'), N'日', '') as date) as nvarchar)     起,
       cast(cast(replace(replace(replace(止日, N'年', '-'), N'月', '-'), N'日', '') as date) as nvarchar)     止,
       cast(cast(replace(replace(replace(离监日期, N'年', '-'), N'月', '-'), N'日', '') as date) as nvarchar) 离监日
from sfjy
where 身份证号 is not null
  and 身份证号 <> N'无'
  and (户籍住址 like N'福建%' or 身份证号 like '35%')
  and 起日 is not null
  and 止日 is not null
  and 离监日期 is not null
union all
select 姓名,
       出生日期,
       队别,
       罪名,
       刑期,
       起日,
       止日,
       户籍住址,
       离监日期,
       身份证号,
       cast(cast(replace(replace(replace(起日, N'年', '-'), N'月', '-'), N'日', '') as date) as nvarchar) 起,
       '20301231'                                                                                         止,
       '20301231'                                                                                         离监日
from sfjy
where 身份证号 is not null
  and 身份证号 <> N'无'
  and (户籍住址 like N'福建%' or 身份证号 like '35%')
  and 止日 is null
  and 离监日期 is null
union all
select 姓名,
       出生日期,
       队别,
       罪名,
       刑期,
       起日,
       止日,
       户籍住址,
       离监日期,
       身份证号,
       cast(cast(replace(replace(replace(起日, N'年', '-'), N'月', '-'), N'日', '') as date) as nvarchar)     起,
       cast(cast(replace(replace(replace(离监日期, N'年', '-'), N'月', '-'), N'日', '') as date) as nvarchar) 止,
       cast(cast(replace(replace(replace(离监日期, N'年', '-'), N'月', '-'), N'日', '') as date) as nvarchar) 离监日
from sfjy
where 身份证号 is not null
  and 身份证号 <> N'无'
  and (户籍住址 like N'福建%' or 身份证号 like '35%')
  and 止日 is null
  and 离监日期 is not null
union all
select 姓名,
       出生日期,
       队别,
       罪名,
       刑期,
       起日,
       止日,
       户籍住址,
       离监日期,
       身份证号,
       cast(cast(replace(replace(replace(起日, N'年', '-'), N'月', '-'), N'日', '') as date) as nvarchar) 起,
       '20301231'                                                                                         止,
       '20301231'                                                                                         离监日
from sfjy
where 身份证号 is not null
  and 身份证号 <> N'无'
  and (户籍住址 like N'福建%' or 身份证号 like '35%')
  and 止日 is null
  and 离监日期 is null
union all
select 姓名,
       出生日期,
       队别,
       罪名,
       刑期,
       起日,
       止日,
       户籍住址,
       离监日期,
       身份证号,
       cast(cast(replace(replace(replace(起日, N'年', '-'), N'月', '-'), N'日', '') as date) as nvarchar)     起,
       cast(cast(replace(replace(replace(离监日期, N'年', '-'), N'月', '-'), N'日', '') as date) as nvarchar) 止,
       '20301231'                                                                                             离监日
from sfjy
where 身份证号 is not null
  and 身份证号 <> N'无'
  and (户籍住址 like N'福建%' or 身份证号 like '35%')
  and 止日 is not null
  and 离监日期 is null;