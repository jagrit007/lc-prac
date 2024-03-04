/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if(head == null){ return head; }
        if(head.next == null){return null;}

        ListNode prev = head;
        ListNode ptr_one = head;
        ListNode ptr_two = head;

        for(int i=0; i<n;i++){
            if(ptr_two != null){
                ptr_two = ptr_two.next;
                continue;
            }
            break;
        }

        while (ptr_two != null) {
                prev = ptr_one;
                ptr_one = ptr_one.next;
                ptr_two = ptr_two.next;
        }
        if (ptr_two == null) {
            if(ptr_one == head){
                head = head.next;
            }
            // remove the node
            prev.next = ptr_one.next;
            ptr_one = null;

        }
        return head;

    }
}