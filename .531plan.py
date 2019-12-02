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

def warm_up_set(xlzl, add_load, plan):
    # 热身组重量百分比
    outstrs = []
    # warm_plans = ((0.2, 10), (0.2, 10), (0.4, 8), (0.6, 5), (0.6, 5), (0.8, 2), (0.9, 1))
    warm_plans = (0.15, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9)
    # 次数
    warm_rm = (5, 5, 5, 5, 3, 2, 1)

    xlr = int('%.0f' % (((plan[0] * xlzl * 0.9) + add_load) / 2.5)) * 2.5
    pass
    index = 1
    index_warm = 1
    skip = 0
    for p in warm_plans:
        # 训练重量 = 1rm * 0.9 * 计划重量比率

        xlr_warm = int('%.0f' % (((p * xlr)) / 5)) * 5
        if xlr_warm < 20:
            skip += 1
            continue
        outstr = '\t第%s组: %skg\t%s次' % (index, xlr_warm, warm_rm[index_warm - 1])
        if skip > 1:
            index_warm += 1
            skip -= 1
        index_warm += 1
        index += 1
        print(outstr)
        outstrs.append(outstr)
    pass


def result_plan(xlzl, add_load, plans, des, name=''):
    outstrs = []
    if name:
        print(name)
    print("#### 热身组:")
    warm_up_set(xlzl, add_load, plans[0])
    print("#### 正式组:")
    for i, p in enumerate(plans):
        # 训练重量 = 1rm * 0.9 * 计划重量比率

        xlr = int('%.0f' % (((p[0] * xlzl * 0.9) + add_load) / 2.5)) * 2.5
        outstr = '\t第%s组: %skg\t%s次\t%s\tload: %s' % (i+1, xlr, p[1], des, str(p[0]*100) + '%')
        print(outstr)
        outstrs.append(outstr)
    print("---")


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

            result_plan(sd, add_sd_load, plans[1], plans[2], name="### 深蹲 (周一)")
            result_plan(wt, add_wt_load, plans[1], plans[2], name="### 卧推 (周二)")
            result_plan(yl, add_yl_load, plans[1], plans[2], name="### 硬拉 (周四)")
            result_plan(tj, add_tj_load, plans[1], plans[2], name="### 推举 (周五)")
            print('')
            print('')
            print('')
        print('')

        flag += 1
    print('总周期数: %s    起始重量(1rm), 卧推: %s kg 深蹲: %s kg 推举: %s kg 硬拉: %s kg' % (cycle, wt, sd, tj, yl))

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
