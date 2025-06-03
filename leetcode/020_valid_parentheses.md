### Description

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

### Solution
```js
/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const map = {']':'[', '}':'{', ')':'('};
    let reserva = [];
    
    for (let i=0;i<s.length;i++) {
      const elemento = s[i];
        if (elemento === "[" || s[i] === "{" || s[i] === "(") {
            reserva.push(elemento);
        }
        else if (elemento === "]" || s[i] === "}" || s[i] === ")") {
          if (reserva.length === 0) {
            return false
          }
          const ultimo = reserva.pop();
          if (map[elemento] !== ultimo) {
              return false
              }
        }
    }
  return reserva.length === 0
};
```
