from pydantic import BaseModel, ValidationError, Field, field_validator

# Exercise 1: Create a model Book with title: str, author: str, pages: int and price: float.
# Create one valid book and print it. Then try to create one with pages="many", catch the ValidationError, and print it.

class Book(BaseModel):
    title: str
    author: str
    pages: int
    price: float

try:
    book = Book(title="AI Expert", author="ABc", pages= 10, price=19.99)
    print(book)
    book = Book(title="AI Expert", author="ABc", pages= "many", price=19.99)
    print(book)
except ValidationError as e:
    print(e)
    
    
    

# Exercise 2: Create a model Student with these rules (use Field):

# name: at least 2 characters
# age: between 5 and 100
# marks: a list[int], default an empty list
# email: optional (str | None = None)

# Test it with 2 valid students and 3 invalid ones, each breaking a different rule. Catch and print every error.

class Student(BaseModel):
    name: str = Field(min_length=2)
    age: int = Field(ge=5, le=100)
    marks: list[int] = []
    email: str | None = None

tests = [
    {"name": "A", "age": 10},
    {"name": "Ali", "age": 1},
    {"name": "Ali", "age": "ten"},
]
for data in tests:
    try:
        print(Student(**data))
    except ValidationError as e:
        print(e)
    

# Exercise 3: Add a field_validator to Student that rejects any mark below 0 or above 100.
# Hint: the validator receives the whole list, so loop through it.

class Student(BaseModel):
    name: str = Field(min_length=2)
    age: int = Field(ge=5, le=100)
    marks: list[int] = []
    email: str | None = None

    @field_validator("marks")
    @classmethod
    def marks_range(cls, value:list[int]) -> list[int]:
        for m in value:
            if m < 0 or m > 100:
                raise ValueError("Studend cannot have mark below 0 or above 100")
        return value

try:
    Student(name="ALI", age=10, marks=[23,34,25],email="abc@gmail.com")
    Student(name="ALI", age=10, marks=[-3,34,25],email=None)

except ValidationError as e:
    print(e)


# Exercise 4: Given this JSON text, use one Pydantic method to load and validate it, then print each item’s name and the total price:

order_json = '''
{
    "order_id": 101,
    "customer": "Dummy",
    "items": [
        {"name": "Rice", "price": 350, "quantity": 2},
        {"name": "Milk", "price": 220, "quantity": 1}
    ]
}
'''

class Item(BaseModel):
    name: str
    price: int
    quantity: int

class Order(BaseModel):
    order_id: int
    customer: str
    items: list[Item]
    
order = Order.model_validate_json(order_json)

total = 0
for item in order.items:
    print(f"{item.name}: {item.quantity} x Rs {item.price}")
    total += item.price * item.quantity
print(f"Order total: Rs {total}")


# Excercise # 6

replies = [
    '{"name": "Ali", "age": 28, "city": "Lahore"}',
    '{"name": "Sara", "age": "31", "city": "Karachi"}',
    '{"name": "Ahmed", "city": "Multan"}'
]

class Person(BaseModel):
    name: str
    age: int
    city: str

valid_list = []
for reply in replies:
    try:
        valid_list.append(Person.model_validate_json(reply))
    except ValidationError as e:
        print(f"Failed: {reply}")
        print(e)

ages = []
for a in valid_list:
    ages.append(a.age)

print(f"Average age: {sum(ages)/len(ages)}")    