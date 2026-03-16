# 📁 Polygon Area Calculator
> A Python OOP project that models rectangles and squares with geometry methods, ASCII picture rendering, and shape fitting logic, a freeCodeCamp certification project.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Project](https://img.shields.io/badge/freeCodeCamp-Certification%20Project-informational?logo=freecodecamp)

## 📌 About

This the 3rd freeCodeCamp certification project that models a `Rectangle` class and a `Square` subclass. Beyond basic geometry, the project introduces an ASCII picture renderer and a method that calculates how many times one shape fits inside another. It was built to practice inheritance, method overriding, and the `math` module in a practical geometry context.

## 🧠 What I Learned

- **Inheritance and method overriding** — `Square` extends `Rectangle` using `super().__init__()`, but overrides `set_width()`, `set_height()`, and adds `set_side()` to ensure both dimensions always stay equal — a square's core constraint
- **`math.sqrt()` and `pow()`** — Using the Pythagorean theorem to calculate the diagonal: `math.sqrt(pow(width, 2) + pow(height, 2))`, combining two math tools in a single expression
- **ASCII art with string multiplication** — Building a visual rectangle by looping through the height and multiplying "*" by the width on each row, similar to the dot bars from the RPG Character Creator but applied to 2D shapes
- **Floor division for shape fitting** — Using `//` to calculate how many times a smaller shape fits inside a larger one without going over, by dividing width and height independently and multiplying the results
- **`__str__` overriding in subclasses** — Both `Rectangle` and `Square` define their own `__str__`, with `Square` displaying `side=` instead of `width=` and `height=` since both are always equal
- **Guarding against edge cases** — Returning an early string "Too big for picture." when dimensions exceed 50, `keeping get_picture()` from generating unreadable output

## 🛠️ Technologies Used

| Tool/Library | Purpose |
|--------------|---------|
| Python 3.x | Core Language |
| `math` | Calculating the diagonal with `sqrt()` and `pow()` |

## 💡 How It Works

`Rectangle` provides all the core geometry methods. `Square` inherits them all and overrides the setters to keep width and height in sync.

| Method | Description |
|--------|-------------|
| `get_area() | Returns `width * height` |
| `get_perimeter()` | Returns `2 * (width + height)` |
| `get_diagonal()` | Returns the diagonal using Pythagoras |
| `get_picture()` | Renders and ASCII rectangle made of `*` characters |
| `get_amount_inside(shape)` | Returns how many times `shape` fits inside Rectangle |

##Example Output:**

```
Rectangle(width=5, height=3)

*****
*****
*****

Square(side=4)

****
****
****
****

get_amount_inside: 2
```

## 🚀 Future Improvements

- [ ] Add a `Circle` class with `get_area()` and `get_circumference()` using `math.pi`
- [ ] Add a `get_amount_inside()` that accounts for rotation of the inner shape
- [ ] Write unit tests with pytest to validate all geometry methods and edge cases
- [ ] Extend `get_picture()` to support custom fill characters beyond *

## 📂 Project Structure

```
rectangle-calculator/
│
├── PolygonAreaCalculator.py    # Rectangle and Square classes
└── README.md
```

*Part of my Python learning journey 🐍 — freeCodeCamp Scientific Computing with Python certification*
