"""
Write a function called solution(s) that, given a non-empty string less than 200 characters in length describing the sequence of M&Ms, returns the maximum number of equal parts that can be cut from the cake without leaving any leftovers.

"""





from multiprocessing.reduction import steal_handle


def solution(s):
    # Your code here
      if len(s) == 1:
        return 1
      elif len(s) == 2:
         if s[0] == s[1]:
            return 2
         else:
            return 0
      else:
         for i in range(len(s)):
            print("\n")
            # print(f'{s[:i]} | {s[i:i+i]} | {s[i+i:]}')
            # print(f'{s[:len(s)-i]} | {s[len(s)-i:len(s)-(i+i)]} | {s[len(s)-(i+i):]}')
            print(f'{s[:-(len(s)-i)]} | {s[-(len(s)-i):-(len(s)-(i+i))]} | {s[-(len(s)-(i+i)):]}')
            print("\n")
            
            if s[:i] == s[i:i+i-1]:
               return i

def finder(s):
   # maximum number of substrings
   max_substring = 0
   # basic condition
   if len(s) == 1:
        return 1
   elif len(s) == 2:
      if s[0] == s[1]:
            return 2
      else:
         return 0
   
   # loop through the string
   for i in range(len(s)):
      # check if the substring is equal to the part of string with same length
      # check if the substring really repeats for the rest of the string
      if i != 0 and (s[:i] == s[i:i+i]) and (s[:-i] == s[-i:-(i+i)]) and len(s) % i == 0 and i > max_substring:
         # if it is, then update the max_substring
         print(f'-{i}-') # i = the length of the substring
         max_substring = int(len(s)/i)
         break
      
      
   return max_substring


def solution1(s):
   # maximum number of substrings
   max__number_of_substring = 0
   max_number_of_substring_lengths = []
   # basic condition
   if len(s) == 1:
        return 1
   elif len(s) == 2:
      if s[0] == s[1]:
            return 2
      else:
         return 0
   
   # loop through the string, i is the width of the substring
   for i in range(1, len(s)+1): # check if the substring really repeats for the rest of the string, add +1 to reach the end of the string
      print(f'i:{i}') # testing
      for sub in range(0, len(s), i): # loop to compare the substring of a given width with the rest of the string
         if sub != 0 and len(s) % i == 0: # ignore 0th index and make sure the width is divisible by the length of the string
            print(f'{sub} & {int(len(s)-i)}') # testing
            if (s[:i] != s[sub:sub+i]): # if the substring is not equal to the rest of the string,
               print(f'not match') # testing 
               break # try the next substring with the next width
            elif (s[:i] == s[sub:sub+i]) and (sub == int(len(s)-i)): # if the substring is equal to every sub part of the string and reached the end of the string
               max_number_of_substring_lengths.append(int(len(s)/i)) # add the number of slices (by calculating string length/substring length) to the list
               print(f'matched:-{i}-') # testing
               break # stop searching for the next substring with the next width. # '[sub:sub+i]' is the sliding window compared with the first substring 's[:i]'
      
      if max_number_of_substring_lengths != []: # if the smallest repeatable substring with is found
         max__number_of_substring = max_number_of_substring_lengths[0] # set the max_number_of_substring to the 
         break # stop searching for other substring widths
   print(max_number_of_substring_lengths) # testing
   return max__number_of_substring


def solution0(s):
   for i in range(1, len(s)+1): # loop through the string, i is the width of the substring
      if s[:i] * int(len(s)/i) == s: # comparison check if the substring really repeats for the rest of the string by multiplying the substring by the number of times it repeats
         return int(len(s)/i) # once the smallest substring width has been found, return the number of slices (by calculating string length/substring length)


if __name__ == '__main__':
    print(find("abcabcabcabc"))
    print(find("abccbaabccba"))
   #  print('\n')
   #  print(finders("abcabcabcabcg"))
   #  print(finder("abcabcdabcabcd"))
   #  print(finder("abcdefghijklmnopqrstuvwxyz"))
   #  print(finder("abababab"))
   #  print(solution("abababab"))
   #  print(finders("aaaacaaaac"))
   #  print(finders("ab"))

   # print("test")
   # aWord = "12345678"
   # print(aWord[::-1])
   # print(aWord[:3:])
   # print(aWord[2::2])
   # print(aWord[2:6:])
   # print(aWord[2:6:2])
   # print(aWord[-1:])
   # print("\n")
   # print("test2")
   # print("\n")
   # print(aWord[:-len(aWord)])
   # for x in range(0, 10, 4):
   #    print(x)
   #    print(aWord[x:x+4])
   #    for y in range(20,40,2):
   #       # print(y)
   #       if y == 30:
   #          break