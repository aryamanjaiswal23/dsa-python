class MyClass:
    def public_method(self):
        pass

    public_variable = 10

    def _protected_method(self):
        pass

    _protected_variable = 20

    def __private_method(self):
        pass

    __private_variable = 30


cl = MyClass()
print(cl.public_variable)  # Output: 10
print(cl._protected_variable)  # Output: 20
print(cl.__private_variable)  # Attribute Error
