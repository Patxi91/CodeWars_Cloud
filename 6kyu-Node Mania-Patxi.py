def search_k_from_end(linked_list, k):
    if k <= 0:
        return None

    slow = fast = linked_list.head

    # Move the fast pointer k steps ahead
    for _ in range(k):
        if fast is None:
            return None  # k exceeds the size of the list
        fast = fast.next

    # Move both pointers until the fast pointer reaches the end
    while fast is not None:
        slow = slow.next
        fast = fast.next

    return slow.data
