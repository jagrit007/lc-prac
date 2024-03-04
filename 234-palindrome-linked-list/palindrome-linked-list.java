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

    public static ListNode recursiveReverse(ListNode head){
        if(head == null || head.next == null){return head;}

        ListNode new_head = recursiveReverse(head.next);
        head.next.next = head;
        head.next = null;

        return new_head;
    }

    public ListNode findMiddle(ListNode head){
        ListNode slow = head;
        ListNode fast = head;

        while(fast.next != null && fast.next.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }

    public boolean isPalidrome2(ListNode head){
        ArrayList<Integer> list = new ArrayList<Integer>();
        ListNode temp = head;

        while(temp != null){
            list.add(temp.val);
            temp = temp.next;
        }

        int i = 0;
        int j = list.size()-1;
        while (i<j){
            if (list.get(i) != list.get(j)){
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
    public boolean isPalindrome(ListNode head) {
        if(head == null || head.next == null){return true;}

        ListNode middle = findMiddle(head);
        ListNode revHead = recursiveReverse(middle.next);
        
        ListNode firstHead = head;

        while(revHead != null){
            if(firstHead.val != revHead.val){
                return false;
            }
            firstHead = firstHead.next;
            revHead = revHead.next;
        }
        return true;

    }
}