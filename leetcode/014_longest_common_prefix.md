### Description

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

### Solution
```
/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
        let prefix = []
    for (i=0;i<strs[0].length;i++) {
        let word = strs[0];
        let j = 1
        for (j=1;j<strs.length;j++) {
            if (word[i] === strs[j][i]) {
            } else return prefix.join("");
        }
    prefix.push(word[i]);
    } return prefix.join("");
};
```