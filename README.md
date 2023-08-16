# Python Control Flow

Control flow in programming refers to the order in which a statement or block of code executes.<br/>
In Python we can control the flow of execution using:
- Conditional statements e.g. `if/else` and `try/except`
- Looping constructs e.g. `for` and `while`

# Control Flow: Operators
We use operators to perform operations on variables and values. For control flow, we use the comparison and logical operators to determine the flow of execution.

## Comparison Operators
Python has the following operators that can be used to compare two values:

`>` greater than<br/>
`>=` greater than or equal to<br/>
`<` less than<br/>
`<=` less than or equal to<br/>
`==` equal to<br/>
`!=` not equal to<br/>

### `==` vs `is`
`==` function in Python does not do any type coercion like JavaScript does, e.g. coercing string to number, before comparing. The `==` function checks if the objects on both sides are considered the equivalent values:<br/>

```
// Javascript

"1" == 1
// => true
0 == []
// => true
[] == ![]
// => true
```

```
# Python

"1" == 1
# False
1 == 1
# True
```

Python has the `is` operator, similar to JavaScript's `===`, it is not used the same way as it is in JavaScript. There are very few scenarios where the `is` operator in Python; in general, for comparing data, you want to use the `==` <br/>
The reason:
> The `==` operator *compares the value* or *equality of two objects*, whereas the Python `is` operator checks whether *two variables point to the same object in memory*. In the vast majority of cases, this means you should use the equality operators == and !=, except when you’re comparing to None.

> Memory management in Python involves a private heap containing all Python objects and data structures. The management of this private heap is ensured internally by the Python memory manager.

## Logical Operators
Python also includes logical operators similar to other programming languages e.g. JavaScript, these include:

`and` - Returns True if both statements are true.<br/>
`or` - Returns True if one of the two statements is true.<br/>
`not` - Coerces the data to its boolean equivalent, then reverses it (True becomes False, and vice versa).<br/>

# Truthy/Falsy Values
In order to use control flow effectively, it's important to know what values Python treats as "truthy" and "falsy".

Values Python considers falsy:

Empty lists `[]` <br/>
Empty tuples `()` <br/>
Empty dictionaries `{}` <br/>
Empty sets `set()` <br/>
Empty strings `''` or `""` <br/>
Zero of any numeric type (`0`, `0.0`) <br/>
`None` <br/>
`False` <br/>

# References

Control Flow on Canvas
- [Control Flow: Operators](https://moringa.instructure.com/courses/479/pages/control-flow-operators?module_item_id=68318)
- [Control Flow: Conditional Statements](https://moringa.instructure.com/courses/479/assignments/32113?module_item_id=68319)

`is` operator vs `==` operator
- [Comparing Python Objects the Right Way: "is" vs "=="](https://realpython.com/courses/python-is-identity-vs-equality/)

Python Memory Management
- [Memory Management](https://docs.python.org/3/c-api/memory.html)