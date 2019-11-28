#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import argparse

import collections

CYCLE_PLANS = [
    ['## 第一周', ((0.65, 5), (0.75, 5), (0.85, 5)), 'Joker Set+ ｜辅助训练'],
    ['## 第二周', ((0.8, 3), (0.85, 3), (0.9, 3)), 'Joker Set+ ｜辅助训练'],
    ['## 第三周', ((0.75, 5), (0.85, 3), (0.95, 1)), 'Joker Set+ ｜辅助训练'],
    ['## 第四周', ((0.6, 5), (0.65, 5), (0.7, 5)), 'Deload ｜辅助训练'],
]

def result_plan(xlzl, add_load, name, plans, des):
    outstrs = []
    print(name)
    for i, p in enumerate(plans):
        # 训练重量 = 1rm * 0.9 * 计划重量比率

        xlr = int('%.0f' % (((p[0] * xlzl * 0.9) + add_load) / 2.5)) * 2.5
        outstr = '\t第%s组: %skg\t%s次\t%s\tload: %s' % (i+1, xlr, p[1], des, str(p[0]*100) + '%')
        print(outstr)
        outstrs.append(outstr)


def plan(sd, wt, tj, yl, cycle):
    flag = 0
    while flag < cycle:
        print('# 第%s个周期' % (flag + 1))
        for plans in CYCLE_PLANS:
            print(plans[0])
            # 渐进增加负荷
            add_sd_load = 5 * flag
            add_wt_load = 2.5 * flag
            add_tj_load = 2.5 * flag
            add_yl_load = 5 * flag

            result_plan(sd, add_sd_load, "### 深蹲 (周一)", plans[1], plans[2])
            result_plan(wt, add_wt_load, "### 卧推 (周二)", plans[1], plans[2])
            result_plan(tj, add_tj_load, "### 推举 (周四)", plans[1], plans[2])
            result_plan(yl, add_yl_load, "### 硬拉 (周五)", plans[1], plans[2])
            print('---')
        print('')

        print('---')
        flag += 1
    print('起始1rm, 卧推: %s kg 深蹲: %s kg 推举: %s kg 硬拉: %s kg' % (wt, sd, tj, yl))

class Prepare:
    parser = None

    def __init__(self):
        parser = argparse.ArgumentParser(description='饮食管理')

        parser.add_argument("-s", help="深蹲最大 1rm 重量", type=int, required=True)
        parser.add_argument("-w", help="卧推最大 1rm 重量", type=int, required=True)
        parser.add_argument("-t", help="推举最大 1rm 重量", type=int, required=True)
        parser.add_argument("-y", help="硬拉最大 1rm 重量", type=int, required=True)
        parser.add_argument("--cycle", help="计划执行周期", type=int, default=6)
        self.parser = parser

    def run(self, argv):
        args = self.parser.parse_args(argv)
        plan(args.s, args.w, args.t, args.y, args.cycle)

def main(argv=sys.argv[1:]):
    app = Prepare()
    app.run(argv)


if __name__ == '__main__':
    sys.exit(main())
