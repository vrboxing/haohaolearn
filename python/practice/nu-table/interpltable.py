#! /usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
from scipy import interpolate
import bisect


def nu(re, rho):
    """
    由于相对偏心距re和折算配筋率rho查找nu
    """

    nu = np.genfromtxt("./data.csv", delimiter=",")
    # 横轴: \rho f_sd / f_cd
    tblx = nu[0, 1:]
    # 纵轴：\eta \e0 / r
    tbly = nu[1:, 0]
    # n_u
    tblz = nu[1:, 1:]
    tbl = interpolate.interp2d(tblx, tbly, tblz, kind='linear')

    res = tbl(re, rho)
    return res


def rho(re, nuval):
    """
    由于相对偏心距re和承载力系数nu查找折算配筋率rho
    """
    return 0


if __name__ == '__main__':

    nu(0.24, 0.4)

    nu = np.genfromtxt("./data.csv", delimiter=",")
    # 横轴: \rho f_sd / f_cd
    tblx = nu[0, 1:]
    # 纵轴：\eta \e0 / r
    tbly = nu[1:, 0]
    # n_u
    tblz = nu[1:, 1:]

    re = 0.38
    nuval = 0.623

    idy = bisect.bisect_left(tbly, re)
    if idy < 1 or idy > len(tbly):
        res = False

    nux1 = nu[idy, 1:]
    nux2 = nu[idy + 1, 1:]

    nui = np.array([])
    for nu1, nu2 in zip(nux1, nux2):
        f = interpolate.interp1d([0.35, 0.4], [nu1, nu2], kind='linear')
        nui = np.append(nui, f(re))

    idx = bisect.bisect_left(nui, nuval) - 1

    if idx < 0:
        res = False

    rho1 = tblx[idx]
    rho2 = tblx[idx + 1]
    f = interpolate.interp1d([nui[idx], nui[idx + 1]], [rho1, rho2],
                             kind='linear')
    nures = f(nuval)[0,0]
