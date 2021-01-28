"""
比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）

"""
class Animal:
    def __init__(self,name,color,age,gender):
        self.name = name
        self. color = color
        self.age = age
        self.gender = gender
    #定义类的方法
    def animal_shout(self):
        shout = "会叫"
        print(f"{self.name}饿了{shout}")

    def animal_run (self):
        run = "会跑"
        print(f"{self.name}遇到危险{run}")
if __name__ == "__main__":
    animal = Animal('pupey','yellow',3,'male')
    print(animal.name)
    animal.animal_shout()
    animal.animal_run()
    print(animal.age)




