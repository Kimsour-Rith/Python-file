 #Parent class
# class A:                                # Parent/ Base/ Super Class
#     def feature1(self):
#         print("Feature 1 working")
#     def feature2(self):
#         print("Feature 2 working")
# # Child class
# class B(A):                             # Child/sub/derived
#     def feature3(self):
#         print("Feature 3 working")
# a1 = A()
# a1.feature1()
# a1.feature2()
#
# a2 = B()
# a2.feature1()
# a2.feature2()
# a2.feature3()
#
#
# # Mutilple level
# class A:                                # Parent/ Base/ Super Class
#     def feature1(self):
#         print("Feature 1 working")
#     def feature2(self):
#         print("Feature 2 working")
# # Child class
# class B(A):                             # Child/sub/derived
#     def feature3(self):
#         print("Feature 3 working")
#     def feature4(self):
#         print("Feature 4 working")
#
# class C(B):                             # Child/sub/derived
#     def feature5(self):
#         print("Feature 5 working")
#     def feature6(self):
#         print("Feature 6 working")
#
# a1 = A()
# a1.feature1()
# a1.feature2()
# print("##"*10)
#
# a2 = B()
# a2.feature1()
# a2.feature2()
# a2.feature3()
# a2.feature4()
# print("**"*10)
#
# a3 = C()
# a3.feature1()
# a3.feature2()
# a3.feature3()
# a3.feature4()
# a3.feature5()
# a3.feature6()
# print("@@"*10)

#############

class A:                                # Parent/ Base/ Super Class
    def init(self):
        print("In A Init")
    def feature1(self):
        print("Feature 1 working")
    def feature2(self):
        print("Feature 2 working")
# Child class
class B(A):                             # Child/sub/derived
    def init(self):
        print("In B Init")
    def feature3(self):
        print("Feature 3 working")
#Call init A:
a1 = A()  # Output: init A
#Call init B:
a2 = B()     # Output: init B    # if there are no init B, it will print Init A




#super can access all feature in parent class
# class A:                                # Parent/ Base/ Super Class
#     def init(self):
#         print("In A Init")
#     def feature1(self):
#         print("Feature 1 working")
#     def feature2(self):
#         print("Feature 2 working")
# # Child class
# class B(A):                             # Child/sub/derived
#     def init(self):
#         super().init()              # can access all feature in Parent class, work with A and B
#         print("In B Init")
#     def feature3(self):
#         print("Feature 3 working")
# a1 = B()        # Output: init A, init B
#class B work and call class A, Class A print "init A" then go to print "init B"

##########################

#super with multiple:
# class A:                                # Parent/ Base/ Super Class
#     def init(self):
#         print("In init A")
#     def feature1(self):
#         print("Feature 1 working")
#     def feature2(self):
#         print("Feature 2 working")
# # Child class
# class B(A):                             # Child/sub/derived
#     def init(self):
#         print("In init B")
#     def feature3(self):
#         print("Feature 3 working")
#     def feature4(self):
#         print("Feature 4 working")
#
# class C(B):                             # Child/sub/derived
#     def init(self):
#         super().init()    # work with B and C
#         print("In init C")
#     def feature5(self):
#         print("Feature 5 working")
#     def feature6(self):
#         print("Feature 6 working")
#
# a1 = C()                # Output: "Init B", "Init C"

################


# class A:                                # Parent/ Base/ Super Class
#     def init(self):
#         print("In init A")
#     def feature1(self):
#         print("Feature 1 working")
#     def feature2(self):
#         print("Feature 2 working")
# # Child class
# class B:                             # Child/sub/derived
#     def init(self):
#         print("In init B")
#     def feature3(self):
#         print("Feature 3 working")
#     def feature4(self):
#         print("Feature 4 working")
#
# class C(A, B):                             # Child/sub/derived
#     def init(self):
#         super().init()
#         print("In init C")
#     def feat(self):
#         super().feature2()      # feature2 is feature of parent class(A)
#         super().feature3()
# a1 = C()                # Output: "Init B", "Init C"
# a1.feat()