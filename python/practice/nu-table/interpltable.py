#! /usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
from scipy import interpolate


def nu_table(x, y):

    nu = np.genfromtxt("./data.csv", delimiter=",")
    # 横轴: \rho f_sd / f_cd
    tblx = nu[0, 1:]
    # 纵轴：\eta \e0 / r
    tbly = nu[1:, 0]
    # n_u
    tblz = nu[1:, 1:]
    tbl = interpolate.interp2d(tblx, tbly, tblz, kind='linear')

    res = tbl(x, y)
    return res


if __name__ == '__main__':

    nu_table(0.24, 0.4)
