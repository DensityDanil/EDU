
#itype: int
#rtype: dict with [int,list]

def fibb_number(your_int_number):
        #ref: https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/

        first = 0
        second = 1
        fibb_seq = []
        if your_int_number<0:
                print('Incorrect number')
        elif your_int_number == 0:
                return first
        elif your_int_number==1:
                return second
        else:

                for i in range( 2
                               ,your_int_number+1): #note `i` is not depend and not link with `first`,`second`  variables
                        third = first+second
                        first = second #note shift for variables
                        second = third #din-don
                        fibb_seq.append(second)

                out_dict = { 'fibb_n_number':       second
                            ,'sequence_till_number':fibb_seq}
                return out_dict

#TODO: two variations:
#        search by
#                slice of position
#                given fibb number idx to expected number
#                        (or idx in fibb sequence)
        
fibb_number(9)
