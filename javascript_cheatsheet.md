# Basic Javascript Cheatsheet

## General resources
### Variables
`let` declares a local variable (block scope). Can be reassigned.

`const` declares a local variable (block scope). Cannot be reassigned.
```js
const person = { name: "Charlie" };
person.name = "David"; // Allowed - modifying properties
person = { name: "Eve" }; // Not allowed - modifying the constant itself
```
`var` is function scoped but has some confusing rules.

Variable names can contain letters, digits, underscores "_" and dollar signs "$. Cannot start with digits, are case-sensitive.

### Functions
The `return` statement stops the function execution. If there's no `return`, "undefined" will be returned.
```js
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
```js
const sum = (argument1, argument2) => argument1 + argument2;

const subtraction = (number, subtractor) => {
    return number - subtractor;
};

const square = x => x*x;
```

### If statements

```js
let temperature = 25;
if (temperature > 20) {
  console.log("It's a warm day!");
}
```
```js
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
```js
let nums = [1, 2, 3]
for (let i = 0; i < nums.length; i++) {
  console.log("The number is " + nums[i]);
} // Prints 1 to 3
```

`while` loop (_condition to check_):
```js
let count = 0;
while (count < 3) {
  console.log("Count is " + count);
  count++;
}
```

`do...while` loop (`do`{...} `while` (_condition to check_)). Do an action then starts to check the condition right afterwards:
```js
let attempts = 0;
do {
  console.log("Attempt number: " + attempts);
  attempts++;
} while (attempts < 0);
```

`for...of` loop. Reduced syntaxto iteracticting over all objects:
```js
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
```js
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
```js
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
```js
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

`.at(index)`: returns the element at the specified index. Can use negative integers to count back from the end.
```js
let language = "JavaScript";
console.log(language.at(2));    // Output: "v"
console.log(language.at(-1));   // Output: "t"

let scores = [88, 95, 74];
console.log(scores.at(1));      // Output: 95
console.log(scores.at(-2));     // Output: 95
```

### Methods and properties exclusive to strings

Strings are immutable, so all methods return a new string (must assign to a variable to keep the result).

`.toUpperCase()` and `.toLowerCase()`: converts the entire string to uppercase / lower case.
```js
let greeting = "Hello World";
let lowerGreeting = greeting.toLowerCase();
let upperGreeting = greeting.toUpperCase();

console.log(lowerGreeting); // Output: "hello world"
console.log(upperGreeting); // Output: "HELLO WORLD"
console.log(greeting);      // Output: "Hello World" (original unchanged)
```

`.trim()`: removes whitespace (spaces, tabs, newlines) from both ends of a string.

`.replace(pattern, replacement)` and `.replaceAll(pattern, replacement)`: returns a new string with one, some, or all matches of a `pattern` replaced by a `replacement`. `.replace()` with a string pattern only replaces the first occurrence, while `.replaceAll()` replaces all.
```js
let message = "I like cats. Dogs are nice, but I prefer cats.";
let newMessage = message.replace("cats", "birds");
console.log(newMessage); // Output: "I like birds. Dogs are nice, but I prefer cats."

let newAllMessage = message.replaceAll("cats", "birds");
console.log(newAllMessage); // Output: "I like birds. Dogs are nice, but I prefer birds."
```

`.split(separator[, limit])`: splits the string into an array, using the separator to determine the splits. The limit param determines how many of the elements are returned.
```js
let sentence = "This is a sentence.";
let words = sentence.split(' ');
console.log(words);       // Output: ["This", "is", "a", "sentence."]
console.log(sentence.split(' ', 2)); // Output: ['This', 'is']
```

`.startsWith(searchString[, position])` and `.endsWith(searchString[, length])`: checks if the string begins or ends with the characters of `searchString`. The optional second parameter specifies the position to begin searching from or the length of the string to consider.
```js
let url = "https://example.com";
console.log(url.startsWith("https"));     // Output: true
console.log(url.endsWith(".com"));        // Output: true
console.log(url.endsWith(".com", 18)); // Output: true (considers "https://example.com")
```

`.repeat(count)`: returns a new string containing the specified number of copies of the string on which it was called.
```js
console.log("ha".repeat(3)); // Output: "hahaha"
console.log("---".repeat(5)); // Output: "---------------"
```

---

### Methods and properties exclusive to arrays

Many array methods can be categorized into:
- **Mutator methods:** Modify the original array.
- **Accessor methods:** Do not modify the original array and return some representation of it (often a new array or a value).
- **Iteration methods:** Operate on every element of the array (like `forEach`, `map`, `filter`).

#### Static Methods

`Array.isArray(obj)`: determines whether the passed value is an `Array`. This is a method on the `Array` object itself, not an array instance.
```js
console.log(Array.isArray([1, 2, 3])); // Output: true
console.log(Array.isArray({}));        // Output: false
console.log(Array.isArray("text"));    // Output: false
```

#### Mutator Methods

`.push(element1[, ..., elementN])` and `.unshift(element1[, ..., elementN])`: adds one or more elements to the end or beginning of an array and returns the new `length` of the array.
```js
let colors = ["red", "green"];
let newLength = colors.push("blue", "yellow");
console.log(colors);    // Output: ["red", "green", "blue", "yellow"]
console.log(newLength); // Output: 4
newLength = colors.unshift("black");
console.log(colors);    // Output: ["black", "red", "green", "blue", "yellow"]
console.log(newLength); // Output: 5
```

`.pop()` and `.shift()`: removes the last or first element from an array and returns that element.
```js
let tasks = ["buy milk", "read book", "call mom"];
let lastTask = tasks.pop();
console.log(tasks);     // Output: ["buy milk", "read book"]
console.log(lastTask);  // Output: "call mom"
let firstTask = tasks.shift();
console.log(tasks);     // Output: ["read book"]
console.log(firstTask);  // Output: "buy milk"
```

`.splice(start, deleteCount[, item1[, item2[, ...]]])`: changes the contents of an array by removing or replacing existing elements and/or adding new elements *in place*. Returns an array containing the deleted elements.
*   `start`: Index at which to start changing the array.
*   `deleteCount`: An integer indicating the number of elements in the array to remove from `start`.
*   `item1, item2, ...` (optional): The elements to add to the array, beginning from `start` index.
```js
let months = ["Jan", "March", "April", "June"];
// Insert "Feb" at index 1
months.splice(1, 0, "Feb");
console.log(months); // Output: ["Jan", "Feb", "March", "April", "June"]
// Remove 1 element at index 3 ("April") and insert "May"
let removed = months.splice(3, 1, "May");
console.log(months);   // Output: ["Jan", "Feb", "March", "May", "June"]
console.log(removed);  // Output: ["April"]
```

`.sort([compareFunction])`: sorts the elements of an array *in place*. **By default, it sorts based on string conversion**, which can lead to unexpected results for numbers. Provide a `compareFunction` for custom sort order (like numeric).
```js
let fruits = ["banana", "apple", "cherry"];
fruits.sort();
console.log(fruits); // Output: ["apple", "banana", "cherry"]

let numbers = [100, 20, 1, 5];
numbers.sort(); // Sorts as strings: "1", "100", "20", "5"
console.log(numbers); // Output: [1, 100, 20, 5] (Incorrect numeric sort!)

// Correct numeric sort with a compare function
numbers.sort((a, b) => a - b);
console.log(numbers); // Output: [1, 5, 20, 100]
```

`.reverse()`: reverses an array *in place*. The first element becomes the last, and the last becomes the first.
```js
let items = [1, 2, 3, 4];
items.reverse();
console.log(items); // Output: [4, 3, 2, 1]
```

#### Accessor Methods

`.join(separator)`: (returns a string) joins all elements of an array into a string. The `separator` string is used between elements. If omitted, elements are separated by a comma.

`.concat(array2[, ..., arrayN])`: (returns a new array) returns a *new* array comprised of the original array joined with other array(s) and/or value(s). Does not change existing arrays.
```js
let arr1 = [1, 2];
let arr2 = [3, 4];
let arr3 = [5, 6];
let combined = arr1.concat(arr2, arr3, 7);
console.log(combined); // Output: [1, 2, 3, 4, 5, 6, 7]
console.log(arr1);     // Output: [1, 2] (original unchanged)
```

#### Iteration Methods

`.forEach(callbackFn(element[, index[, array]]))`: executes a provided function once for each array element. Unlike `map`, it does not return a new array and its return value is `undefined`.
```js
let names = ["Alice", "Bob", "Charlie"];
names.forEach(name => {
  console.log(`Hello, ${name}!`);
});
// Output:
// "Hello, Alice!"
// "Hello, Bob!"
// "Hello, Charlie!"
```

`.map(callbackFn(element[, index[, array]]))`: (returns a new array) creates a *new* array populated with the results of calling a provided function (`callbackFn`) on every element in the calling array.
```js
let numbers = [1, 4, 9];
let doubles = numbers.map(num => num * 2);
console.log(doubles);  // Output: [2, 8, 18]
console.log(numbers);  // Output: [1, 4, 9] (original unchanged)
```

`.filter(callbackFn(element[, index[, array]]))`: (returns a new array) creates a *new* array with all elements that pass the test implemented by the provided `callbackFn`. The callback should return `true` to keep the element, or `false` otherwise.
```js
let ages = [32, 15, 33, 12, 40, 20];
let adults = ages.filter(age => age >= 18);
console.log(adults); // Output: [32, 33, 40, 20]
console.log(ages);   // Output: [32, 15, 33, 12, 40, 20] (original unchanged)
```

`.reduce(callbackFn(accumulator, currentValue[, currentIndex[, array]])[, initialValue])`: (returns a single value) executes a "reducer" function on each element of the array, resulting in a single output value.
```js
let prices = [10.5, 20, 8.75];
let sum = prices.reduce((total, currentPrice) => total + currentPrice, 0);
// 1st call: total=0, currentPrice=10.5 -> returns 10.5
// 2nd call: total=10.5, currentPrice=20 -> returns 30.5
// 3rd call: total=30.5, currentPrice=8.75 -> returns 39.25
console.log(sum); // Output: 39.25
```

`.find(callbackFn(element[, index[, array]]))`: (returns an element or `undefined`) returns the **first element** in the array that satisfies the provided testing function (`callbackFn`). If no values satisfy the testing function, `undefined` is returned.
```js
let inventory = [
{ name: "apples", quantity: 2 },
{ name: "bananas", quantity: 0 },
{ name: "cherries", quantity: 5 },
];
let foundItem = inventory.find(item => item.name === "bananas");

console.log(foundItem); // Output: { name: 'bananas', quantity: 0 }
let notFound = inventory.find(item => item.name === "oranges");
console.log(notFound); // Output: undefined
```

`.findIndex(callbackFn(element[, index[, array]]))`: (returns an index or -1) returns the **index of the first element** in the array that satisfies the provided testing function. Otherwise, it returns -1.
```js
let numbers = [5, 12, 8, 130, 44];
let largeNumberIndex = numbers.findIndex(num => num > 100);
console.log(largeNumberIndex); // Output: 3
```

`.some(callbackFn)` and `.every(callbackFn)`: (return a boolean) `.some` tests whether at least one element passes the test. `.every` tests whether all elements pass the test.
```js
let grades = [85, 92, 78, 65, 95];
let hasFailingGrade = grades.some(grade => grade < 70);
console.log(hasFailingGrade); // Output: true

let allPassingGrades = grades.every(grade => grade >= 65);
console.log(allPassingGrades); // Output: true
```