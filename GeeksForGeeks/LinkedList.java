class LinkedList {
    // Driver method
    public static void main (String args[]) {
        LinkedList llist = new LinkedList();
        llist.pushNode(1);
        llist.pushNode(2);
        llist.pushNode(3);
        llist.pushNode(4);
        llist.pushNode(5);
        llist.printLinkedList(head);
        llist.nthNodeFromEnd(head, 2);
    }

    static Node head = null;

    // Define Node
    class Node {
        int data;
        Node next;

        Node (int d) {
            data = d;
            next = null;
        }
    }

    // Util functions
    void pushNode (int d) {
        Node newNode = new Node(d);
        newNode.next = head;
        head = newNode;
    }

    void printLinkedList (Node head) {
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println("");
    }

    // nth Node from the end
    static int i = 0;
    void nthNodeFromEnd (Node node, int n) {
        if (node == null)
            return;
        nthNodeFromEnd(node.next, n);
        if (++i == n)
            System.out.println(node.data);
    }
}