### Description

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

### Solution
```js
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    if (s.length !== t.length) return false;

    let sToT = {};
    let tToS = {};

    for (let i = 0; i < s.length; i++) {
        if (!sToT[s[i]] && !tToS[t[i]]) {
            sToT[s[i]] = t[i];
            tToS[t[i]] = s[i];
        } else if (sToT[s[i]] !== t[i] || tToS[t[i]] !== s[i]) {
            return false;
        }
    }

    return true;
};
```