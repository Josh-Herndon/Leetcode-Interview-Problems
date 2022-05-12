/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    
    let l1String = '';
    let l2String = '';
    
    while (l1 || l2) {
        if (l1 !== null) {
            l1String = String(l1.val) + l1String;
            l1 = l1.next;
        }
        
        if (l2 !== null) {
            l2String = String(l2.val) + l2String;
            l2 = l2.next;
        }
    }
    
    const total = String(BigInt(l1String) + BigInt(l2String));
    const len = total.length;
    
    let head = new ListNode(BigInt(total[len - 1]));
    const output = head;
    
    let j = 2;
    while (len - j >= 0) {
        head.next = new ListNode(BigInt(total[len - j]));
        head = head.next;
        j++;
    }
    
    head.next = null;
    
    return output
};
