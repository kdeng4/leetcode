from rec.ListNode import ListNode

class LinkedListSolution:
    def removeNodes(self, head: ListNode) -> ListNode:
        node = head
        vals = []
        while node is not None:
            if len(vals) > 0 and node.val > vals[-1]:
                while len(vals) > 0 and node.val > vals[-1]:
                    vals.pop(-1)
            vals.append(node.val)
            node = node.next
        node = head
        for n_idx, n_val in enumerate(vals):
            node.val = n_val
            if n_idx == len(vals) - 1:
                node.next = None
            node = node.next
        return head

    def doubleIt(self, head: ListNode) -> ListNode:
        node = head
        total_val = 0
        while node is not None:
            total_val *= 10
            total_val += node.val
            node = node.next
        total_val *= 2
        list_vals = []
        while total_val > 0:
            list_vals.insert(0, total_val % 10)
            total_val = total_val // 10
        node = head
        for v_idx, v in enumerate(list_vals):
            node.val = v
            if v_idx < len(list_vals) - 1:
                node.next = ListNode()
                node = node.next
        return head


s = LinkedListSolution()
input = [1, 8, 9]
nodes = []
node_temp = None
for val in input:
    curr_node = ListNode(val=val)
    nodes.append(curr_node)
    if node_temp is not None:
        node_temp.next = curr_node
    node_temp = curr_node
input = nodes
output = s.doubleIt(input[0])
while output is not None:
    print(output.val)
    output = output.next