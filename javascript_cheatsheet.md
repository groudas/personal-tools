# Basic Javascript Cheatsheet

## General resources
### Variables
`let` declares a local variable (block scope). Can be reassigned.

`const` declares a local variable (block scope). Cannot be reassigned.
```
const person = { name: "Charlie" };
person.name = "David"; // Allowed - modifying properties
person = { name: "Eve" }; // Not allowed - modifying the constant itself
```
`var` is function scoped but has some confusing rules.

Variable names can contain letters, digits, underscores "_" and dollar signs "$. Cannot start with digits, are case-sensitive.

### Functions
The `return` statement stops the function execution. If there's no `return`, "undefined" will be returned.
```
function functionName(argument1, argument2) {
    sum = argument1 + argument2;
    return sum;
};

const subtract = function(number, subtractor) {
    subtraction = number - subtractor;
    return subtraction;
};
```

Arrow function:
```
const sum = (argument1, argument2) => argument1 + argument2;

const subtraction = (number, subtractor) => {
    return number - subtractor;
};

const square = x => x*x;
```

### If statements

```
let temperature = 25;
if (temperature > 20) {
  console.log("It's a warm day!");
}
```
```
let grade = 85;
if (grade >= 90) {
  console.log("Grade: A");
} else if (grade >= 80) {
  console.log("Grade: B");
} else if (grade >= 70) {
  console.log("Grade: C");
} else {
  console.log("Grade: Needs Improvement");
}
```

### Loops

Avaiable statements:
- `break`: stops the loop.
- `continue`: finishes current iteration and starts the next.

`for` loop (_initial state ; condition to check ; action every iteraction_):
```
let nums = [1, 2, 3]
for (let i = 0; i < nums.length; i++) {
  console.log("The number is " + nums[i]);
} // Prints 1 to 3
```

`while` loop (_condition to check_):
```
let count = 0;
while (count < 3) {
  console.log("Count is " + count);
  count++;
}
```

`do...while` loop (`do`{...} `while` (_condition to check_)). Do an action then starts to check the condition right afterwards:
```
let attempts = 0;
do {
  console.log("Attempt number: " + attempts);
  attempts++;
} while (attempts < 0);
```

`for...of` loop. Reduced syntaxto iteracticting over all objects:
```
let fruits = ["apple", "banana", "cherry"];
for (const fruit of fruits) {
  console.log(fruit);
}

let message = "Hello";
for (const char of message) {
  console.log(char); // H, e, l, l, o (each on a new line)
}
```

Bonus: `.forEach` method. Don't have `beak` or `continue`statements:
```
let numbers = [10, 20, 30, 40];

numbers.forEach(function(number, index, array) {
  console.log("Element at index " + index + " is " + number);
  // You can also access the original array if needed:
  // console.log("Original array:", array);
});

// Using an arrow function (more common in modern JS):
numbers.forEach((number, index) => {
  console.log(`Value: ${number}, Index: ${index}`);
});
```

## Methods and properties

### Methods and properties common to strings and arrays

`.length`: returns the number of characters in a string or number of elements in an array.

`indexOf(searchValue[, fromIndex])`: returns the first index at which a given element can be found or -1 if can't be found.
```
let text = "Hello world, world";
console.log(text.indexOf("world"));     // Output: 6
console.log(text.indexOf("world", 7));  // Output: 13

let fruits = ["apple", "banana", "orange", "banana"];
console.log(fruits.indexOf("banana"));    // Output: 1
console.log(fruits.indexOf("banana", 2)); // Output: 3
console.log(fruits.indexOf("grape"));     // Output: -1
```

`.lastIndexOf(searchValue[, fromIndex])`: like `.indexOf` but returns the last found index, or -1.

`.includes(searchElement[, fromIndex])`: like `.indexOf` but returns `true` if the element is found and `false` if not found.

`.slice(beginIndex[, endIndex])`: returns a **new** string/array. Extracts the elements between the given indexes.
```
let str = "JavaScript";
console.log(str.slice(0, 4));  // Output: "Java"
console.log(str.slice(4));     // Output: "Script"
console.log(str.slice(-3));    // Output: "ipt" (last 3 characters)

let numbers = [1, 2, 3, 4, 5];
console.log(numbers.slice(1, 3));  // Output: [2, 3]
console.log(numbers.slice(2));     // Output: [3, 4, 5]
console.log(numbers.slice(-2));    // Output: [4, 5] (last 2 elements)
console.log(numbers);              // Output: [1, 2, 3, 4, 5] (original unchanged)
```

### Methods and properties exclusive to strings

Strings are immutable, so all methods return a new string (must assign to a variable to keep the result)

`.toUpperCase()` and `.toLowerCase()`: converts the entire string to uppercase / lower case.

```
let greeting = "Hello World";
let lowerGreeting = greeting.toLowerCase()
let upperGreeting = greeting.toUpperCase()

console.log(lowerGreeting); // Output: "hello world"
console.log(upperGreeting); // Output: "HELLO WORLD"
console.log(greeting);      // Output: "hello world" (original unchanged)
```

`.trim()`: removes whitespace (spaces, tabs, newlines) from both ends of a string.

`.split(separator[, limit])`: splits the string into an array, using the separator to determine the splits. The limit param determines how many of the elements are returned.
```
let sentence = "This is a sentence.";
let words = sentence.split(' ');
console.log(words);       // Output: ["This", "is", "a", "sentence."]
console.log(sentence.split(' ', 2)); // Output: ['This', 'is']
```

---
**(to be formated yet)**
---

8.  **`.startsWith(searchString[, position])`**
    *   **Description:** Checks if the string begins with the characters of `searchString`. Returns `true` or `false`.
    *   `position` (optional): The position in this string at which to begin searching for `searchString`. Defaults to 0.
    *   **Example:**
        ```javascript
        let filename = "script.js";
        console.log(filename.startsWith("script")); // Output: true
        console.log(filename.startsWith("js", 7));  // Output: true
        ```

9.  **`.endsWith(searchString[, length])`**
    *   **Description:** Checks if the string ends with the characters of `searchString`. Returns `true` or `false`.
    *   `length` (optional): The length of the string to consider. Defaults to the string's length.
    *   **Example:**
        ```javascript
        let url = "https://example.com/page";
        console.log(url.endsWith("/page")); // Output: true
        console.log(url.endsWith(".com", 18)); // Output: true (considers "https://example.com")
        ```

---

### C. Basic Array-Exclusive Methods

Many array methods can be categorized into:
*   **Mutator methods:** Modify the original array.
*   **Accessor methods:** Do not modify the original array and return some representation of it (often a new array or a value).
*   **Iteration methods:** Operate on every element of the array (like `forEach` we've seen, `map`, `filter`).

1.  **`.push(element1[, ..., elementN])`** (Mutator)
    *   **Description:** Adds one or more elements to the *end* of an array and returns the new `length` of the array.
    *   **Example:**
        ```javascript
        let colors = ["red", "green"];
        let newLength = colors.push("blue", "yellow");
        console.log(colors);    // Output: ["red", "green", "blue", "yellow"]
        console.log(newLength); // Output: 4
        ```

2.  **`.pop()`** (Mutator)
    *   **Description:** Removes the *last* element from an array and returns that element.
    *   **Example:**
        ```javascript
        let tasks = ["buy milk", "read book", "call mom"];
        let lastTask = tasks.pop();
        console.log(tasks);     // Output: ["buy milk", "read book"]
        console.log(lastTask);  // Output: "call mom"
        ```

3.  **`.unshift(element1[, ..., elementN])`** (Mutator)
    *   **Description:** Adds one or more elements to the *beginning* of an array and returns the new `length` of the array.
    *   **Example:**
        ```javascript
        let numbers = [3, 4];
        let newLength = numbers.unshift(1, 2);
        console.log(numbers);   // Output: [1, 2, 3, 4]
        console.log(newLength); // Output: 4
        ```

4.  **`.shift()`** (Mutator)
    *   **Description:** Removes the *first* element from an array and returns that removed element.
    *   **Example:**
        ```javascript
        let queue = ["Alice", "Bob", "Charlie"];
        let firstInQueue = queue.shift();
        console.log(queue);         // Output: ["Bob", "Charlie"]
        console.log(firstInQueue);  // Output: "Alice"
        ```

5.  **`.join(separator)`** (Accessor - returns a string)
    *   **Description:** Joins all elements of an array into a string. The `separator` string is used between elements. If omitted, elements are separated by a comma.
    *   **Example:**
        ```javascript
        let parts = ["Ja", "va", "Script"];
        console.log(parts.join(""));   // Output: "JavaScript"
        console.log(parts.join("-"));  // Output: "Ja-va-Script"
        console.log(parts.join());     // Output: "Ja,va,Script" (default comma)
        ```

6.  **`.concat(array2[, ..., arrayN])`** (Accessor - returns a new array)
    *   **Description:** Returns a *new* array comprised of the original array joined with other array(s) and/or value(s). Does not change existing arrays.
    *   **Example:**
        ```javascript
        let arr1 = [1, 2];
        let arr2 = [3, 4];
        let arr3 = [5, 6];
        let combined = arr1.concat(arr2, arr3, 7);
        console.log(combined); // Output: [1, 2, 3, 4, 5, 6, 7]
        console.log(arr1);     // Output: [1, 2] (original unchanged)
        ```

7.  **`.splice(start, deleteCount[, item1[, item2[, ...]]])`** (Mutator)
    *   **Description:** Changes the contents of an array by removing or replacing existing elements and/or adding new elements *in place*. Returns an array containing the deleted elements.
    *   `start`: Index at which to start changing the array.
    *   `deleteCount`: An integer indicating the number of elements in the array to remove from `start`.
    *   `item1, item2, ...` (optional): The elements to add to the array, beginning from `start` index.
    *   **Example:**
        ```javascript
        let months = ["Jan", "March", "April", "June"];
        // Insert "Feb" at index 1
        months.splice(1, 0, "Feb");
        console.log(months); // Output: ["Jan", "Feb", "March", "April", "June"]

        // Remove 1 element at index 3 ("April") and insert "May"
        let removed = months.splice(3, 1, "May");
        console.log(months);   // Output: ["Jan", "Feb", "March", "May", "June"]
        console.log(removed);  // Output: ["April"]
        ```

8.  **`.map(callbackFn(element[, index[, array]]))`** (Accessor - returns a new array)
    *   **Description:** Creates a *new* array populated with the results of calling a provided function (`callbackFn`) on every element in the calling array.
    *   **Example:**
        ```javascript
        let numbers = [1, 4, 9];
        let doubles = numbers.map(function(num) {
          return num * 2;
        });
        // Using arrow function:
        // let doubles = numbers.map(num => num * 2);
        console.log(doubles);  // Output: [2, 8, 18]
        console.log(numbers);  // Output: [1, 4, 9] (original unchanged)
        ```

9.  **`.filter(callbackFn(element[, index[, array]]))`** (Accessor - returns a new array)
    *   **Description:** Creates a *new* array with all elements that pass the test implemented by the provided `callbackFn`. The callback should return `true` to keep the element, or `false` otherwise.
    *   **Example:**
        ```javascript
        let ages = [32, 15, 33, 12, 40, 20];
        let adults = ages.filter(function(age) {
          return age >= 18;
        });
        // Using arrow function:
        // let adults = ages.filter(age => age >= 18);
        console.log(adults); // Output: [32, 33, 40, 20]
        console.log(ages);   // Output: [32, 15, 33, 12, 40, 20] (original unchanged)
        ```

10. **`.find(callbackFn(element[, index[, array]]))`** (Accessor - returns an element or `undefined`)
    *   **Description:** Returns the **first element** in the array that satisfies the provided testing function (`callbackFn`). If no values satisfy the testing function, `undefined` is returned.
    *   **Example:**
        ```javascript
        let inventory = [
          { name: "apples", quantity: 2 },
          { name: "bananas", quantity: 0 },
          { name: "cherries", quantity: 5 },
        ];
        let foundItem = inventory.find(function(item) {
          return item.name === "bananas";
        });
        // Using arrow function:
        // let foundItem = inventory.find(item => item.name === "bananas");
        console.log(foundItem); // Output: { name: 'bananas', quantity: 0 }

        let notFound = inventory.find(item => item.name === "oranges");
        console.log(notFound); // Output: undefined
        ```
