# %%
from matplotlib import rcParams
from matplotlib.pyplot import bar, pie, show, title, xlabel, ylabel
from pandas import DataFrame, read_csv
from pyecharts import options
from pyecharts.charts import Bar, Pie

rcParams["font.sans-serif"] = ["SimHei"]  # 显示中文
# %%


def release_data(_data: DataFrame) -> DataFrame:
    """
    处理数据

    :param _data: 数据
    :type _data: DataFrame
    :return: 数据
    :rtype: DataFrame
    """
    _data = _data[["身份证号码", "户主身份证号码"]]
    _data = _data.drop_duplicates()
    _data = _data.groupby("户主身份证号码").count()
    _data = _data.rename(columns={"身份证号码": "人数"})
    _data = _data.reset_index()
    _data = _data.groupby("人数").count()
    _data = _data.rename(columns={"户主身份证号码": "家庭数"})
    _data = _data.reset_index()
    return _data


# %%
data = read_csv("csv/城市低保.csv")
data = release_data(data)
pie(data["家庭数"], labels=data["人数"], autopct="%0.2f%%")  # type: ignore
title("城市低保家庭人数分布图")
show()
Pie().add("", [list(z) for z in zip(data["人数"], data["家庭数"])]).set_global_opts(
    title_opts=options.TitleOpts(title="城市低保家庭人数分布图")).render("城市低保家庭人数分布图.html")
# %%
data = read_csv("csv/农村低保.csv")
data = release_data(data)
pie(data["家庭数"], labels=data["人数"], autopct="%0.2f%%")  # type: ignore
title("农村低保家庭人数分布图")
show()
Pie().add("", [list(z) for z in zip(data["人数"], data["家庭数"])]).set_global_opts(
    title_opts=options.TitleOpts(title="农村低保家庭人数分布图")).render("农村低保家庭人数分布图.html")


# %%
data = read_csv("csv/城市低保.csv")
data1 = data.groupby("性别").count()
pie(data1["姓名"], labels=data1.index, autopct="%0.2f%%")  # type: ignore
title("城市低保人群性别构成")
show()
Pie().add("", [list(z) for z in zip(data1.index, data1["姓名"])]).set_global_opts(
    title_opts=options.TitleOpts(title="城市低保人群性别构成")).render("城市低保人群性别构成.html")
data1 = data.groupby("年龄").count()
bar(data1.index, data1["姓名"])
xlabel("年龄")
ylabel("人数")
title("城市低保人群年龄构成")
show()
Bar().add_xaxis(list(data1.index)).add_yaxis("", list(data1["姓名"])).set_global_opts(  # type: ignore
    title_opts=options.TitleOpts(title="城市低保人群年龄构成")).render("城市低保人群年龄构成.html")
data1 = data.groupby("文化程度").count()
data1 = data1.sort_values(by=["姓名"], ascending=False)
bar(data1.index, data1["姓名"])
ylabel("人数")
title("城市低保人群学历构成")
show()
Bar().add_xaxis(list(data1.index)).add_yaxis("", list(data1["姓名"])).set_global_opts(  # type: ignore
    title_opts=options.TitleOpts(title="城市低保人群学历构成")).render("城市低保人群学历构成(bar).html")
pie(data1["姓名"], labels=data1.index, autopct="%0.2f%%")  # type: ignore
title("城市低保人群学历构成")
show()
Pie().add("", [list(z) for z in zip(data1.index, data1["姓名"])]).set_global_opts(
    title_opts=options.TitleOpts(title="城市低保人群学历构成")).render("城市低保人群学历构成(pie).html")
# %%
data = read_csv("csv/农村低保.csv")
data1 = data.groupby("性别").count()
pie(data1["姓名"], labels=data1.index, autopct="%0.2f%%")  # type: ignore
title("农村低保人群性别构成")
show()
Pie().add("", [list(z) for z in zip(data1.index, data1["姓名"])]).set_global_opts(
    title_opts=options.TitleOpts(title="农村低保人群性别构成")).render("农村低保人群性别构成.html")
data1 = data.groupby("年龄").count()
bar(data1.index, data1["姓名"])
xlabel("年龄")
ylabel("人数")
title("农村低保人群年龄构成")
show()
Bar().add_xaxis(list(data1.index)).add_yaxis("", list(data1["姓名"])).set_global_opts(  # type: ignore
    title_opts=options.TitleOpts(title="农村低保人群年龄构成")).render("农村低保人群年龄构成.html")
data1 = data.groupby("文化程度").count()
data1 = data1.sort_values(by=["姓名"], ascending=False)
bar(data1.index, data1["姓名"])
ylabel("人数")
title("农村低保人群学历构成")
show()
Bar().add_xaxis(list(data1.index)).add_yaxis("", list(data1["姓名"])).set_global_opts(  # type: ignore
    title_opts=options.TitleOpts(title="农村低保人群学历构成")).render("农村低保人群学历构成(bar).html")
pie(data1["姓名"], labels=data1.index, autopct="%0.2f%%")  # type: ignore
title("农村低保人群学历构成")
show()
Pie().add("", [list(z) for z in zip(data1.index, data1["姓名"])]).set_global_opts(
    title_opts=options.TitleOpts(title="农村低保人群学历构成")).render("农村低保人群学历构成(pie).html")
# %%
