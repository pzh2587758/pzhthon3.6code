class Daletou_JianCe():
    def __init__(self,kaijiang,chupiao):
        self.kaijiang = kaijiang
        self.chupiao = chupiao

    def qihao(self):
        if self.kaijiang[0] == self.chupiao[0]:
            return True
            

a = Daletou_JianCe([1,2],[1,4])
a.qihao()