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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        
        ListNode result = new ListNode(); //dummy
        ListNode tail = result;
        
        while(list1 != null && list2 != null){
            if (list1.val < list2.val){
                tail.next = list1;
                list1 = list1.next;
            } else {
                tail.next = list2;
                list2 = list2.next;
            }
            tail = tail.next;
        }

        tail.next = (list1 != null) ? list1 : list2;

        return result.next;
    }

    public ListNode mergeKLists(ListNode[] lists) {

        if (lists == null || lists.length == 0) return null;
        if (lists.length == 1) return lists[0];
        
        int interval = 1;
        while(interval < lists.length){
            for(int i=0; i + interval < lists.length; i += interval * 2){
                    lists[i] = mergeTwoLists(lists[i], lists[i +interval]);
            }
            interval *= 2;
        }
        return lists[0];
    }
}