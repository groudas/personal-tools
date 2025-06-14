### Description

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

### Solution
```js
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    s = s.trim();
    const splitString = s.split(/ /g);
    const lastWord = splitString[splitString.length-1];
    return lastWord.length;
};
```