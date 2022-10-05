from functools import lru_cache

from numpy import ndarray, array
from pandas import concat, read_csv, DataFrame, merge


def check_number(number: int, record, s: str) -> ndarray:
    """
    如果数量不等于记录，打印错误并更正

    :param number: 数量
    :type number: int
    :param record: 要检查的记录
    :param s: 列的名称
    :type s: str
    :return: 记录。
    """
    if number != record[5]:
        print("年度:", record[0], "学校类型:", record[1],
              "县名:", record[2], "城乡区划:", record[3], s, ":", record[5], "错误")
        print("修正:", number)
        record[5] = number
        return record
    return record


def split_data(data: DataFrame, s: str, i: int) -> tuple[DataFrame, DataFrame]:
    """
    它接受一个数据帧、一个字符串和一个整数，并返回两个数据帧，一个包含原始数据帧的所有行，其中整数指定的列中的值等于字符串，另一个包含所有行整数指定的列中的值不等于字符串的原始数据帧

    :param data: 要拆分的数据框
    :type data: DataFrame
    :param s: 要拆分的属性的值
    :type s: str
    :param i: 要拆分的列的索引
    :type i: int
    :return: 两个 DataFrame 的元组。
    """
    data1 = DataFrame()
    for record in data.values:
        if record[i] == s:
            data1 = concat([data1, DataFrame(record)], axis=1)
    data1 = data1.T
    data1.columns = data.columns
    data1 = data1.reset_index(drop=True)
    data2 = DataFrame()
    for record in data.values:
        if record[i] != s:
            data2 = concat([data2, DataFrame(record)], axis=1)
    data2 = data2.T
    data2.columns = data.columns
    data2 = data2.reset_index(drop=True)
    return data1, data2


def o5o1():
    data = read_csv('csv/数据找错原始数据.csv')
    if data is None:
        return
    data1, data2 = split_data(data, '市合计', 2)
    school_number = 0
    teacher_number = 0
    for record in data2.values:
        if record[3] == '总计':
            if record[4] == '学校数':
                record = check_number(school_number, record, '学校数')
                school_number = 0
            if record[4] == '专任教师数':
                record = check_number(teacher_number, record, '专任教师数')
                teacher_number = 0
        if record[3] != '总计':
            if record[4] == '学校数':
                school_number += record[5]
            if record[4] == '专任教师数':
                teacher_number += record[5]
    school_number = 0
    teacher_number = 0
    for record in data1.values:
        year = record[0]
        category = record[1]
        zone = record[3]
        indicator = record[4]
        for record1 in data2.values:
            if year == record1[0] and category == record1[1] and zone == record1[3] and indicator == record1[4]:
                if indicator == '学校数':
                    school_number += record1[5]
                if indicator == '专任教师数':
                    teacher_number += record1[5]
        if indicator == '学校数':
            record = check_number(school_number, record, '学校数')
            school_number = 0
        if indicator == '专任教师数':
            record = check_number(teacher_number, record, '专任教师数')
            teacher_number = 0


def check_number1(value: int, record: ndarray) -> ndarray:
    """
    如果该值不等于记录的金额，则打印记录的年份、地区、金额和错误消息，然后打印更正，然后返回更正金额的记录

    :param value: 要检查的值
    :type value: int
    :param record: 要检查的记录
    :type record: ndarray
    """
    if value != record[3]:
        print('年度:', record[0], '行政区划:', record[1], '金额:', record[3], '错误')
        print('修正:', value)
        record[3] = value
        return record
    return record


def o5o2():
    data = read_csv('csv/债务汇总数据找错.csv')
    if data is None:
        return
    data1, data2 = split_data(data, '债务合计', 2)
    data3, data4 = split_data(data1, '全市合计', 1)
    data5, data6 = split_data(data2, '全市合计', 1)
    value = 0
    for record in data4.values:
        year = record[0]
        zone = record[1]
        for record1 in data6.values:
            if year == record1[0] and zone == record1[1]:
                value += record1[3]
        record = check_number1(value, record)
        value = 0
    for record in data5.values:
        year = record[0]
        category = record[2]
        for record1 in data6.values:
            if year == record1[0] and category == record1[2]:
                value += record1[3]
        record = check_number1(value, record)
        value = 0
    for record in data3.values:
        year = record[0]
        for record1 in data5.values:
            if year == record1[0]:
                value += record1[3]
        record = check_number1(value, record)
        value = 0


@lru_cache()
def taxation_verification(output_value: int, levy_rate: float, levy_amount: int) -> tuple[float, float]:
    """
    此功能计算征税金额与实际征税金额的差额，以及实际征税金额

    :param output_value: 输出值
    :type output_value: int
    :param levy_rate: 税率
    :type levy_rate: float
    :param levy_amount: 用户必须支付的征费金额
    :type levy_amount: int
    :return: 两个值的元组，征税金额与实际征税金额之间的差值，以及实际征税金额。
    """
    real_levy_amount = levy_amount
    if output_value < 10000000:
        if levy_rate < 0.05:
            real_levy_amount = output_value * levy_rate
        if levy_rate >= 0.05:
            real_levy_amount = output_value * levy_rate - output_value * 0.05
    if output_value >= 10000000:
        if levy_rate < 0.05:
            real_levy_amount = output_value * levy_rate - 10000000 * levy_rate
        if levy_rate >= 0.05:
            real_levy_amount = output_value * levy_rate - 500000
    return levy_amount - real_levy_amount, real_levy_amount


def o5o4():
    data = read_csv('csv/某税务机关征税数据.csv')
    if data is None:
        return
    value = 0
    for record in data.values:
        over_taxation, real_levy_amount = taxation_verification(
            record[6], record[7], record[8])
        if over_taxation > 0:
            print('企业代码:', record[0], '企业名称:', record[1], '行业:', record[2], '法人代表:', record[3],
                  '企业地址:', record[4], '联系方式:', record[5], '产值:', record[6], '征收比例:', record[7], '征收额:',
                  record[8], '实际应征收额:', real_levy_amount, '多征收额:', over_taxation)
            value += over_taxation
    print('税务机关多征收:', value)


def o5o5():
    data = read_csv('csv/贷款发放明细表.csv')
    if data is None:
        return
    data = data[['信贷客户编号', '保证人编号']]
    data = merge(merge(data, data, left_on='信贷客户编号', right_on='保证人编号'), data,
                 left_on=['信贷客户编号_y', '保证人编号_x'], right_on=['保证人编号', '信贷客户编号'])
    data = data.drop_duplicates()
    data = data.loc[(data['信贷客户编号_x'] > data['信贷客户编号_y']) & (data['信贷客户编号_x'] > data['信贷客户编号'])]
    data = data[['信贷客户编号_x', '信贷客户编号_y', '信贷客户编号']]
    print(array(data))


if __name__ == '__main__':
    o5o1()
    o5o2()
    o5o4()
    o5o5()
