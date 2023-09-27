def insert_sort(unsorted_list:list,direction='asc') -> list:
    """
    Sorts a list using the insertion sort algorithm.

    Args:
        unsorted_list: A list of elements to be sorted.
        direction: A string indicating the sort order ('asc' for ascending order, 'desc' for descending order).

    Returns:
        A sorted list.
    """
    len_list=len(unsorted_list)
    if len_list==1:
        return unsorted_list
    sorted_part=insert_sort(unsorted_list[:-1],direction)
    uninsert_num=unsorted_list[-1]
    insert_index=0
    if direction=='asc':
        for index in range(len(sorted_part)-1,-1,-1):
            if uninsert_num>sorted_part[index]:
                insert_index=index+1
                break
            insert_index=0
    if direction=='desc':
        for index in range(len(sorted_part)-1,-1,-1):
            if uninsert_num<sorted_part[index]:
                insert_index=index+1
                break
            insert_index=len(sorted_part)-1
    sorted_part.insert(insert_index,uninsert_num)
    return sorted_part
unsorted_list=[5,2,3,4,1]
s=insert_sort(unsorted_list,direction='desc')
print(s)