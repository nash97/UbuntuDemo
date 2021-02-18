from studentexams.models import demoUserRegistrationModel

demoUser = demoUserRegistrationModel()

keys = [
    name,
    mobile,
    email,
    package
]
values = [
    {
        "name":"nashit",
        "mobile":9384756783,
        "email":"zyz@gmail.com",
        "package":"JEE"
    }
]
# Where key is the field and value is the value you need to fill
product.keys = values

for k, v in response.items():
    setattr(product, k, v)
product.save()
