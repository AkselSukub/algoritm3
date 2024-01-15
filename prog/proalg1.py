#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random as rnd
import matplotlib.pyplot as plt
import numpy as np
import timeit


def find(a, b, len):
    for i in range(len):
        if b == a[i]:
            return i
    return -1

def create_graph(x, y, aur, bur, namegraph):
    plt.scatter(x, y, s=5, c="red")           #точки
    f = aur * np.array(x) + bur               #прямая
    plt.plot(x, f)                            
    plt.title(namegraph + " случай")
    plt.xlabel("Размер массива")
    plt.ylabel("Время работы функции")
    correlation_coefficient = np.corrcoef(y, x)[0, 1]
    return correlation_coefficient

if __name__ == '__main__':
    correlation_v = []
    # Цикл для создания двух графиков: один при среднем случае, второй при худшем
    for namegraph in ["Средний", "Худший"]:
        x = [i for i in range(10, 10001, 10)]
        time = []
        randmax = 1000000
        for i in x:
            a = [rnd.randint(1, randmax) for j in range(i)]
            if namegraph == "Средний":
                b = a[rnd.randint(1, len(a)-1)]
            else:
                b = randmax+1
            timer = (timeit.timeit(lambda: find(a, b, i), number=50))/50
            time.append(timer)

        # Вычисление коэффицентов в системе уравнений метода наименьших квадратов
        sx = sum(x)
        stime = sum(time)
        sx2 = sum(i**2 for i in x)
        sxtime = sum(i*j for i, j in zip(x, time))
        n = len(x)
        k = sx2/sx   # вычисление свободного коэффициента
        bur = (sxtime - k*stime)/(sx-k*n)   # свободный коэффицент
        aur = (stime - bur*n)/sx

        # Создание графических окон
        plt.figure(namegraph)
        plt.subplots_adjust(left=0.2)

        # Создание графиков
        correlation_v.append(create_graph(x, time, aur, bur, namegraph))
    print("Коэффициент корреляции в первом случае =", correlation_v[0], "\nКоэффициент корреляции во втором случае =", correlation_v[1])

    # Показ графиков
    plt.show()