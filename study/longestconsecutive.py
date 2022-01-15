
def get_longest_consecutive_char( string ):
    

 
    if len(string)==0:
        return {}
    else:
        longest_count = 0
        longest_char  = ''
        prev  = ''
        count = 0

        for char in string:
            print( '---------------{}-------------'.format(char) )
            if prev == char:
                print( 'adding count')
                count = count+1
            else:
                count = 1
           
            print( 'count {} vs longest {}'.format(count, longest_count ) )
            if count > longest_count:
                longest_count = count
                longest_char  = prev
           
            prev  = char
            #End

            print( 'Prev {} Count {} longestcount{} longestchar{}'.format( prev, count, longest_count, longest_char) )
        #End

    
        return {longest_char:longest_count}
  
print(get_longest_consecutive_char('AABCDDBBBEAaaaaaaa'))