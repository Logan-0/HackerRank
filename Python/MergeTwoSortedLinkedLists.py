# // Given pointers to the heads of two sorted linked lists, merge them into a single, sorted linked list. Either head pointer may be null meaning that the corresponding list is empty.

def mergeLists(head1, head2): 


    if (head1 == None):
        return head2
    
    if (head2 == None):
        return head1
    

    n = None
    t = None

    if (head1.data < head2.data):
        n = head1
        t = head1
        head1 = head1.next
    else:
        n = head2
        t = head2
        head2 = head2.next
    

    while head1 != None and head2 != None:
        if (head1.data < head2.data):
            t.next = head1
            t = t.next
            head1 = head1.next
        else:
            t.next = head2
            t = t.next
            head2 = head2.next
        
    

    while (head1):
        t.next = head1
        t = t.next
        head1 = head1.next
    

    while (head2):
        t.next = head2
        t = t.next
        head2 = head2.next
    

    return n