class multifilter:

    def judge_half(self, pos, neg):
        return pos >= neg

    def judge_any(self, pos, neg):
        return pos >= 1

    def judge_all(self, pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        for i in self.iterable:
            pos = neg = 0
            for j in self.funcs:
                if j(i):
                    pos += 1
                else:
                    neg += 1
            if self.judge(self,pos,neg):
                yield i