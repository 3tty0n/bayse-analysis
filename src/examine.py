# -*- encoding=utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


K = 47


def processing(df):
    x = data.under15man / data.population
    df['x'] = x
    return df


def ratio_each_city(df):
    result = []
    for i in range(1, K + 1):
        p = df[df['number'] == i].x
        ratio_sum = sum(p)
        result.append(ratio_sum)
    return result


def calc_mean_var(df):
    lst = ratio_each_city(df)
    m = np.mean(lst)
    v = np.std(lst)
    return m, v


def examine(df):
    m, s = calc_mean_var(df)
    y = ratio_each_city(df)
    z = []
    for k in range(K):
        z.append(abs((y[k] - m) / s))
    ans = []
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(x=range(1, K + 1), y=z)
    plt.axhline(2.58, c='red')
    plt.xlabel("index")
    plt.ylabel("Z_k")
    for k in range(K):
        if abs(z[k]) > 2.58:
            ans.append((k + 1, z[k]))
            plt.text(x=k, y=abs(z[k]), s=(k + 1, z[k]))
    plt.savefig('output/image/examine.png')
    plt.show()
    return ans


if __name__ == '__main__':
    data = pd.read_csv('input/data_example2.csv')
    data = processing(data)
    print(examine(df=data))
