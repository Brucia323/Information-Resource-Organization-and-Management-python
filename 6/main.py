from pandas import Series, read_csv
from tqdm import tqdm


def verify(_data: Series, weight: list[int]):
    for d in tqdm(_data):
        arr = list(str(d))
        value = 0
        for index, a in enumerate(arr):
            if index == 9:
                if value % 9 != int(a):
                    print("错误编码:", d)
                break
            value += int(a) * weight[index]


data = read_csv("csv/某企业培训登记表.csv")
data1 = data["培训登记号（算术）"]
weight1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
verify(data1, weight1)
data2 = data["培训登记号（几何）"]
weight2 = [2**9, 2**8, 2**7, 2**6, 2**5, 2**4, 2**3, 2**2, 2**1]
verify(data2, weight2)
data3 = data["培训登记号（质数）"]
weight3 = [29, 23, 19, 17, 13, 11, 7, 5, 3]
verify(data3, weight3)
