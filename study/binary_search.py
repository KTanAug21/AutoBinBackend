def binary_search( array, val, left, right ):
    if left > right or right < left:
        return False
    
    # Get Midpoint
    mid = int((left+right)/2)

    if val == array[mid]:
        return True
    elif val < array[mid]:
        return binary_search( array, val, left, mid-1 )
    else:
        return binary_search( array, val, mid+1, right )
#End

arr =  [3,6,19,20,24,46,50,100,101,102,103]
data = binary_search(
    arr,
    100,
    0,
    len(arr)-1
)
print( data )