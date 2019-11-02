# task 1
list1 = [1,2,3,4,5,6,7,8,9]
list2 = list1
list2.append(10)
list2.pop(0)
print(list1)
print(list2)
list3 = list1[:]
list3.append('full copy magic')
print(list1)
print(list3)
# task 2
def sayhello_func():
    username = str(input('What is your name? '))
    if not username:
        username = 'STRANGER' #just for test 
    firstletter = username[0].upper()
    otherletters = username[1:].lower()
    print ('Hello, ' + firstletter + otherletters + '!')
sayhello_func()
# task 3
class Dog:
    def bark (self,number=1):
        print (' BARK!!!' * number)
class SmartDog(Dog):
    def givepaw (self):
        print ('Paw pat')
alex = Dog()
toto = SmartDog()
alex.bark()
toto.bark()
toto.givepaw()
class NoizyDog(Dog):
    def bark (self, number=10):
        while number > 0:
            print ('BARK!!!')
            number -= 1
honey = NoizyDog()
honey.bark()



