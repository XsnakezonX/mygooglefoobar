"""
['1', '2']
['1', '2', '3']
['1', '2']
None
"stack"
stack.append('1')
stack.append('2')
print(stack)
stack.append('3')
print(stack)
stack.pop()
print(stack)
"""

"""
['1', '2']
['1', '2', '3']
['2', '3']
None
"queue"
stack.append('1')
stack.append('2')
print(stack)
stack.append('3')
print(stack)
stack.pop(0)
print(stack)

"""

"""
Example: 
0. main_list = ['>', '>', '<', '>', '<', '>']
1. ['>'] ['>', '<', '>', '<', '>'] # look at the 1st element; temp_left = main_list[0] = ['>'], temp_right = main_list[1:] = ['>', '<', '>', '<', '>']
2. ['>'] ['<', '<'] # remove all matching symbols
3. counter += len(['<', '<']) # add the length of the remaining symbols, 2
4. ['>'] ['<', '>', '<', '>'] # look at the 2st element



"""


def find(s):
   """ find matching symbols with a bidirectional sliding window """

   main_list = list(s)
   counter = 0 # record the number of salute made from both directions

   for i in range(len(main_list)): # loop through the string
      if main_list[i] == '>': # if the symbol is '>'
         temp_right_side = main_list[i+1:] # compare the current element with the remaining elements on the right
         for arrows in temp_right_side: # add the number of opposing symbols to counter
            if arrows == '<':
               counter += 1
         
      elif main_list[i] == '<': # if the symbol is '<'
         temp_left_side = main_list[:i] # compare the current element with the remaining elements on the left
         for arrows in temp_left_side: # add the number of opposing symbols to counter
            if arrows == '>':
               counter += 1

   return counter
      


   # counting for the queue

   





if __name__ == '__main__':
    print(find("--->-><-><-->-"))
    print(find(">----<"))
    print(find("<<>><"))
