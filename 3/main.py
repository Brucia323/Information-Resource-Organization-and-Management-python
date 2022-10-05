from pandas import read_csv, read_sql
from pymssql import connect
from sqlalchemy import create_engine
from tqdm import tqdm


def connect_to_mssql():
    mssql_connection = connect(host='localhost', port='1433', user='sa', password='mssql-2022pw', database='irom')
    if mssql_connection:
        print("连接成功")
    return mssql_connection


def import_to_mssql(path, name):
    """ValueError: Unsigned 64 bit integer datatype is not supported"""
    data = read_csv(path)
    data.to_sql(name, get_mssql_engine('sa', 'mssql-2022pw', 'irom'))


def get_mssql_engine(user, password, database):
    return create_engine('mssql+pyodbc://' + user + ':' + password + '@' + database)


if __name__ == '__main__':
    csv_paths = ['csv/gjj_个人业务明细.csv', 'csv/gsdj_登记信息.csv', 'csv/jgyl_02个人基本信息表.csv',
                 'csv/jgyl_06待遇支付明细表.csv', 'csv/mzhh_殡仪馆火化数据_202012.csv',
                 'csv/sfjy_全省服刑人员数据_202012.csv', 'csv/zgyl_01单位基本信息表.csv',
                 'csv/zgyl_02个人基本信息表.csv', 'csv/zgyl_03人员参保信息表.csv', 'csv/zgyl_05个人征缴明细表.csv']
    table_names = ['gjj', 'gsdj', 'jgyl_02', 'jgyl_06', 'mzhh', 'sfjy', 'zgyl_01', 'zgyl_02', 'zgyl_03', 'zgyl_05']
    for i in tqdm(range(len(csv_paths))):
        import_to_mssql(csv_paths[i], table_names[i])
        
    connection = connect_to_mssql()
    cursor = connection.cursor()

    print("案例二: ")

    sql = "create view 机关火化人员名单 as select a.*, b.火化时间 from jgyl_02 a join mzhh b on a.证件号码 = b.身份证号"
    cursor.execute(sql)
    connection.commit()
    print("机关火化人员名单: ")
    sql = "select * from 机关火化人员名单"
    print(read_sql(sql, connection))

    sql = "create view 机关最大待遇领取年月 as select 人员编码, max(待遇年月) as 待遇年月 from jgyl_06 where 待遇项目代码 not in (100501, 100502, 200030, 200070, 400100, 400040, 600100) group by 人员编码"
    cursor.execute(sql)
    connection.commit()
    print("机关最大待遇领取年月: ")
    sql = "select * from 机关最大待遇领取年月"
    print(read_sql(sql, connection))

    sql = "select * from 机关火化人员名单 a left join 机关最大待遇领取年月 b on a.人员编码 = b.人员编码 and replace(substring(火化时间, 1, 6), '-', '0') < 待遇年月"
    print(read_sql(sql, connection))

    sql = "create view yl_死亡后多领待遇JGYL as select a.*, b.死亡后各月待遇年月, b.待遇金额 from ( select a.*, b.待遇年月 最大待遇年月 from 机关火化人员名单 a inner join 机关最大待遇领取年月 b on a.人员编码 = b.人员编码 and replace(substring(a.火化时间, 1, 6), '-', '0') < b.待遇年月 ) a left join ( select 人员编码, 待遇年月 死亡后各月待遇年月, sum(待遇金额) 待遇金额 from jgyl_06 group by 人员编码, 待遇年月 ) b on a.人员编码 = b.人员编码 where replace(substring(a.火化时间, 1, 6), '-', '0') < b.死亡后各月待遇年月"
    cursor.execute(sql)
    connection.commit()
    print("yl_死亡后多领待遇JGYL: ")
    sql = "select * from yl_死亡后多领待遇JGYL"
    print(read_sql(sql, connection))

    sql = "select count(*) from sfjy where 身份证号 is not null and 身份证号 <> N'无' and (户籍住址 like N'福建%' or 身份证号 like '35%')"
    print(read_sql(sql, connection))

    sql = "create view yl_全省服刑人员_服刑期间发生 as select 姓名, 出生日期, 队别, 罪名, 刑期, 起日, 止日, 户籍住址, 离监日期, 身份证号, cast(cast(replace(replace(replace(起日, N'年', '-'), N'月', '-'), N'日', '') as date) as nvarchar) 起, cast(cast(replace(replace(replace(止日, N'年', '-'), N'月', '-'), N'日', '') as date) as nvarchar) 止, cast(cast(replace(replace(replace(离监日期, N'年', '-'), N'月', '-'), N'日', '') as date) as nvarchar) 离监日 from sfjy where 身份证号 is not null and 身份证号 <> N'无' and (户籍住址 like N'福建%' or 身份证号 like '35%') and 起日 is not null and 止日 is not null and 离监日期 is not null union all select 姓名, 出生日期, 队别, 罪名, 刑期, 起日, 止日, 户籍住址, 离监日期, 身份证号, cast(cast(replace(replace(replace(起日, N'年', '-'), N'月', '-'), N'日', '') as date) as nvarchar) 起, '20301231' 止, '20301231' 离监日 from sfjy where 身份证号 is not null and 身份证号 <> N'无' and (户籍住址 like N'福建%' or 身份证号 like '35%') and 止日 is null and 离监日期 is null union all select 姓名, 出生日期, 队别, 罪名, 刑期, 起日, 止日, 户籍住址, 离监日期, 身份证号, cast(cast(replace(replace(replace(起日, N'年', '-'), N'月', '-'), N'日', '') as date) as nvarchar) 起, cast(cast(replace(replace(replace(离监日期, N'年', '-'), N'月', '-'), N'日', '') as date) as nvarchar) 止, cast(cast(replace(replace(replace(离监日期, N'年', '-'), N'月', '-'), N'日', '') as date) as nvarchar) 离监日 from sfjy where 身份证号 is not null and 身份证号 <> N'无' and (户籍住址 like N'福建%' or 身份证号 like '35%') and 止日 is null and 离监日期 is not null union all select 姓名, 出生日期, 队别, 罪名, 刑期, 起日, 止日, 户籍住址, 离监日期, 身份证号, cast(cast(replace(replace(replace(起日, N'年', '-'), N'月', '-'), N'日', '') as date) as nvarchar) 起, '20301231' 止, '20301231' 离监日 from sfjy where 身份证号 is not null and 身份证号 <> N'无' and (户籍住址 like N'福建%' or 身份证号 like '35%') and 止日 is null and 离监日期 is null union all select 姓名, 出生日期, 队别, 罪名, 刑期, 起日, 止日, 户籍住址, 离监日期, 身份证号, cast(cast(replace(replace(replace(起日, N'年', '-'), N'月', '-'), N'日', '') as date) as nvarchar) 起, cast(cast(replace(replace(replace(离监日期, N'年', '-'), N'月', '-'), N'日', '') as date) as nvarchar) 止, '20301231' 离监日 from sfjy where 身份证号 is not null and 身份证号 <> N'无' and (户籍住址 like N'福建%' or 身份证号 like '35%') and 止日 is not null and 离监日期 is null"
    cursor.execute(sql)
    connection.commit()
    print("yl_全省服刑人员_服刑期间发生: ")
    sql = "select * from yl_全省服刑人员_服刑期间发生"
    print(read_sql(sql, connection))

    print("案例四: ")

    sql = "create view 中间表_最后交保记录 as select * from ( select t.*, row_number() over (partition by 人员编码 order by 本次终止日期 desc) as rn from zgyl_03 t ) as [t.*r] where rn = 1"
    cursor.execute(sql)
    connection.commit()
    print("中间表_最后交保记录: ")
    sql = "select * from 中间表_最后交保记录"
    print(read_sql(sql, connection))

    sql = "create view 中间表_职工养老人员单位表 as select a.*, b.单位编码, t1.单位名称 as 单位名称 from zgyl_02 a join 中间表_最后交保记录 b on a.人员编码 = b.人员编码 join zgyl_01 t1 on b.单位编码 = t1.单位编码 where len(离退休类别) > 0 and charindex(离退休类别, N'正常') = 0 and (离退休类别 = N'因病退休' or 离退休类别 = N'因病退职' or 离退休类别 = N'特殊工种' or 离退休类别 = N'提前退休')"
    cursor.execute(sql)
    connection.commit()
    print("中间表_职工养老人员单位表: ")
    sql = "select * from 中间表_职工养老人员单位表"
    print(read_sql(sql, connection))

    sql = "create view 集中同单位同时间提前退休 as select a.* from 中间表_职工养老人员单位表 A join ( select 单位名称, 离退休日期 from 中间表_职工养老人员单位表 group by 单位名称, 离退休日期 having count(1) > 10 ) B on A.单位名称 = B.单位名称 and A.离退休日期 = B.离退休日期"
    cursor.execute(sql)
    connection.commit()
    print("集中同单位同时间提前退休: ")
    sql = "select * from 集中同单位同时间提前退休"
    print(read_sql(sql, connection))

    sql = "create view 退休后ZG交公积金 as select 经办机构代码, 经办机构名称, a.行政区划代码, 人员编码, 社会保障号码, a.姓名, a.证件号码, 个人身份, 特殊人群标识, 参加工作日期, 视同缴费月数, 实际缴费月数, 离退休日期, 离退休类别, 死亡日期, 个人账户余额, 行政区划名称, 业务年度, 操作中心名称, 操作管理部名称, 操作承办银行名称, 交易渠道类型, 个人账号, b.姓名 姓名_公积金, 账户类型, 单位名称, 记账日期, 借贷标志, 上年结转发生额, 当年归集发生额, 发生额, 发生利息额, 上年余额, 本年余额, 账户余额, 交易码, 归集和提取业务类型, 摘要信息, 汇补缴年月, 汇补缴原因, 提取原因, 提取方式, 业务凭证号, 操作时间, 业务流水号, 流水序号, 资金结算类型, 开户中心归属账务机构, 财务记账凭证生成状态, 财务记账凭证号, 冲账标识, 有效标志, 备注, 时间戳 from zgyl_02 a join gjj b on a.证件号码 = b.证件号码 where a.离退休类别 in (N'因病退休', N'因病退职', N'提前退休', N'特殊工种') and charindex(b.归集和提取业务类型, N'汇缴') > 0 and 离退休日期 - replace(substring(汇补缴年月, 1, 6), '-', '') > 1"
    cursor.execute(sql)
    connection.commit()
    print("退休后ZG交公积金: ")
    sql = "select * from 退休后ZG交公积金"
    print(read_sql(sql, connection))

    cursor.close()
    connection.close()
