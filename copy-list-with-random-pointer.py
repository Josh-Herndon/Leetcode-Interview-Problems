
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):

        if not head:
            return None

        index_node_map = {}
        node_index_map = {}

        head_copy = head
        index = 0
        while head_copy:

            index_node_map[index] = {'node': Node(head_copy.val)}
            index_node_map[index]['next'] = index + 1

            node_index_map[head_copy] = index
            
            index += 1
            head_copy = head_copy.next

        list_len = index

        index = 0
        while head:

            if head.random:
                index_node_map[index]['random'] = node_index_map[head.random]
            else:
                index_node_map[index]['random'] = None

            index += 1
            head = head.next

        for key in index_node_map:

            node = index_node_map[key]['node']
            next_node = index_node_map[key]['next']
            random = index_node_map[key]['random']

            if next_node < list_len:
                node.next = index_node_map[next_node]['node']
            else:
                node.next = None

            if random != None:
                node.random = index_node_map[random]['node']
            else:
                node.random = random
        
        return index_node_map[0]['node']