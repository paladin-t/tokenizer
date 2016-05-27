#!/usr/bin/python
# -*- coding:utf-8 -*-

from __future__ import print_function

"""
适合于各种需要中文分词的场合，如：
    网游脏词过滤
    搜索引擎文档解析
    自然语言处理
    ……
"""
class Tokenizer:
    vocabulary = None

    def __init__(self):
        self.vocabulary = { }

    def addVocable(self, v):
        self.vocabulary[v] = v
        return self

    def getVocable(self, v):
        if v in self.vocabulary:
            return self.vocabulary[v]
        return None

    def getSentences(self, s):
        got = False
        for i in reversed(range(1, 5)):
            if i > len(s):
                continue
            head = s[0 : i]
            if self.getVocable(head):
                got = True
                if len(s) > i:
                    tail = s[i : ]
                    tails = self.getSentences(tail)
                    for it in tails:
                        it.insert(0, head)
                        yield it
                else:
                    yield [head]
            else:
                if i == 1 and not got:
                    tail = s[i : ]
                    if not tail:
                        yield [head]
                    else:
                        tails = self.getSentences(tail)
                        for it in tails:
                            it.insert(0, head)
                            yield it

def test():
    tk = Tokenizer()
    tk.addVocable(u"我")
    tk.addVocable(u"喜")
    tk.addVocable(u"欢")
    tk.addVocable(u"喜欢")
    tk.addVocable(u"研究")
    tk.addVocable(u"搜索")
    tk.addVocable(u"引擎")
    tk.addVocable(u"索引")
    ss = tk.getSentences(u"我喜欢研究开发搜索引擎")
    import sys
    if sys.version_info < (3, 0):
        fmt = lambda _ : sys.stdout.write(_.encode("utf-8"))
    else:
        fmt = lambda _ : print(_, end = "")
    for s in ss:
        fmt("[")
        fmt(", ".join(w for w in s))
        fmt("]\n")

if __name__ == "__main__":
    test()
