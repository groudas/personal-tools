### Description

Given two binary strings a and b, return their sum as a binary string.

### Solution
```js
/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    let resultArray = [];
    let carry = 0;
    let i = a.length - 1;
    let j = b.length - 1;

    while (i >= 0 || j >= 0 || carry > 0) {
        const digitA = i >= 0 ? Number(a[i]) : 0;
        const digitB = j >= 0 ? Number(b[j]) : 0;

        const sum = digitA + digitB + carry;

        const currentBit = sum % 2;
        carry = Math.floor(sum / 2);

        resultArray.push(currentBit);

        i--;
        j--;
    }

    return resultArray.reverse().join('');
};
```