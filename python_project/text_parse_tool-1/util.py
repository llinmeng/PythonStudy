# -*- coding: utf-8 -*-
# 关于yield的问题
# def node._get_child_candidates(self, distance, min_dist, max_dist):
#   if self._leftchild and distance - max_dist < self._median:
#        yield self._leftchild
#   if self._rightchild and distance + max_dist >= self._median:
#        yield self._rightchild
#
# result, candidates = list(), [self]
# while candidates:
#     node = candidates.pop()
#     distance = node._get_dist(obj)
#     if distance <= max_dist and distance >= min_dist:
#         result.extend(node._values)
#     candidates.extend(node._get_child_candidates(distance, min_dist, max_dist))
# return result


# 关于extend():是一个迭代器, 作用于迭代器, 并把参数追加到迭代器的后边
# a = [1, 2]
# b = [3, 4]
# a.extend(b)
# print (a)
# # [1, 2, 3, 4]


def lines(file):
    for line in file:
        yield line
        yield '\n'


def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []



