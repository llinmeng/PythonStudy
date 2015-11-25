# -*- coding: utf-8 -*-
import sys
args = sys.argv[1:]
args.reverse()          # 对列表反向排序
print ''.join(args)


print ''.join(reversed(sys.argv[1:]))