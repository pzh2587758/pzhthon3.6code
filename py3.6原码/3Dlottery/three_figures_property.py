class three_figures_property():
    """三位数的各种属性类"""

    def __init__(self, threefigures):
        self.threefigures = threefigures

    def jo(self):
        """判断三位数奇偶的函数"""
        result = int(self.threefigures) % 2
        if(result == 0):
            print("偶数")
        else:
            print("奇数")


a = three_figures_property("999")
a.jo()
