"""
Visual demonstration of the diagram:

| 11
| 7 12
| 4 8 13
| 2 5 9 14
| 1 3 6 10 15

[1 2 4 7 11]
vertical differences of 1st column (bottom-up): 1,2,3,4,...

[1 3 6 10 15]
horizontal differences of 1st row (left-right): 2,3,4,5,...

start counting the steps made by y-axis-movement from 1
start traverse from the y-axis (bottom-up), increment steps counter by 1 for each steps made.
Then traverse the x-axis (left-right), start from the position/value/cell where y-axis left off.

"""
def find(x,y):
   """ return target value by performing movements in y & x axis """
   value = 1 # start counting from 1, it is the value of the first cell, and it stores the value of the target coordinate
   x_start_steps = 2 # it is the minimum number of start steps for x axis movement. 1 -> 3, diff = 2.

   for i in range(1,y): # calculate the total value in movements made when traveling in the y axis
      value += i # store & obtain value of every step made in every y coordinate
      x_start_steps += 1 # stores the number of movements made when moving in y axis, which determines the starts step number for x axis movement
   for j in range(x-1): # then, calculate the total value when traversing in the x axis
      value += x_start_steps # accumulate the value of the steps made in x axis
      x_start_steps += 1 # increment the value of the steps in x axis

   return str(value)

def finder(x,y):
   """ return target value by performing movements in y & x axis """
   value = 1 # start counting from 1, it is the value of the first cell, and it stores the value of the target coordinate
   x_start_steps = 2 # it is the minimum number of start steps for x axis movement. 1 -> 3, diff = 2.

   for i in range(1,y): # calculate the total value in movements made when traveling in the y axis
      value += i # store & obtain value of every step made in every y coordinate
      x_start_steps += 1 # stores the number of movements made when moving in y axis, which determines the starts step number for x axis movement

   # print(f'i value {value}')
   # print(f'i x_start_steps {x_start_steps}')

   # print(f'x_start_steps {x_start_steps}')
   # print(f'x-1 {x-1}')

   for j in range(x-1): # then, calculate the total value when traversing in the x axis
      # print("!")
      # print(f'j x_start_steps {x_start_steps}')
      value += x_start_steps # accumulate the value of the steps made in x axis
      x_start_steps += 1 # increment the value of the steps in x axis
   
   # print(f'j value {value}')

   return value

      




   





if __name__ == '__main__':
   # print(find(1,1))
   # print(find(2,2))
   print(find(3,2))
   # print(find(4,4))
   # print(find(1,5))
   # print(find(2,4))
   # print(find(3,1))
   print(find(5,10))
