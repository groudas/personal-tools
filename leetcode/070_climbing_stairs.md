### Description

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

### Solution
```js
/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    let fibArr = [1];
    for (let j=1; j<n; j++) {
        if (fibArr[j-2] == undefined) {fibArr[j-2] = 1};
        fibArr[j] = fibArr[j-2] + fibArr[j-1];
    };
    return fibArr[n-1]
};
```