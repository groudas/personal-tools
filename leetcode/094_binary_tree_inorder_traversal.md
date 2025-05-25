### Description

Given the root of a binary tree, return the inorder traversal of its nodes' values.

### Solution
```js
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var inorderTraversal = function(root) {
    let values = []
    function traverse(node) {
        if (node === null) {return}
        traverse(node.left);
        values.push(node.val);
        traverse(node.right);
    }
    traverse(root);
    return values    
}
```