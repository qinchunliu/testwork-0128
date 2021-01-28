from Animal_class import Animal


class Cat(Animal):
    # 定义新的属性
    def __init__(self,name,color,age,gender,hair):
        super().__init__(name,color,age,gender)
        self.hair = hair
    # 添加新的方法，会抓老鼠

    def cat_skiil(self):
        self.skiil = '会抓老鼠'
        print(f"猫的技能是{self.skiil}")

    # 重新叫的方法
    def animal_shout(self):
        shout = "喵喵叫"
        print(f"{self.name}饿了会{shout}")


if __name__ == '__main__':
    cat = Cat("kitty","red",2,"male","短毛")
    cat.animal_shout()
    cat.cat_skiil()







