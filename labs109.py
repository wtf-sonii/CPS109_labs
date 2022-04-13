# As an example, here is an implementation of
# the first problem "Ryerson Letter Grade":
import math
import decimal
import collections
def ryerson_letter_grade(n):
    if n < 50:
        return 'F'
    elif n > 89:
        return 'A+'
    elif n > 84:
        return 'A'
    elif n > 79:
        return 'A-'
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = ""
    return "DCB"[tens - 5] + adjust

def is_ascending(items):
    if len(items)==0:
        return True
    if len(items)==1:
        return True
    i=1
    while i<len(items):
        if items[i]<= items[i - 1]:
            return False
        i+=1
    return True


def riffle(items, out=True):
    items1= items[0: len(items)//2]
    items2= items[len(items)//2:]
    itemsfinal= [None]* (len(items))
    if out == True:
        itemsfinal[::2] = items1
        itemsfinal[1::2]= items2
        return itemsfinal
    if out == False:
        itemsfinal[1::2]= items1
        itemsfinal[::2]= items2
        return itemsfinal

def only_odd_digits(n):
    new_list = [int(d) for d in str(n)]

    for i in new_list:
        if (i % 2)==0:
            return False
    return True
        
def is_cyclops(n):
    l= str(n)
    y=len(l)
    h=len(l)//2
   
    if (y%2)==0:
         return False
    else:
        if l[h] != "0":
            return False
        if l.count("0")>1:
            return False
        return True
        
def domino_cycle(tiles):
    count=0
    x=0
    if len(tiles)==0:
        return True
    elif len(tiles)==1:
        return tiles[0][0]==tiles[0][1]
    for i in range(len(tiles)-1):
        if tiles[i][1]!=tiles[i+1][0]:
            count+=1
    if tiles[-1][1]==tiles[0][0]:
        x+=1
    if count==0 and x!=0:
        return True
    else:
        return False
            
    

def taxi_zum_zum(moves):
    directions=['N','E','S','W']
    dir=0
    x=0
    y=0
    for i in moves:
        if i=='L':
            dir -= 1
            if dir<0:
                dir=3
        elif i=='R':
            dir+=1
            if dir>3:
                dir=0
        elif i=='F':
            if directions[dir]=='N':
                y+= 1
            elif directions[dir]=='S':
                y -= 1
            elif directions[dir]=='E':
                x += 1
            elif directions[dir]=='W':
                x-=1
    return (x,y)
            
def pancake_scramble(text):
    x=text
    for i in range(2,len(text)+1):
        x=x[:i][::-1]+x[i:]
    return x


def give_change(amount, coins):
    x=[]
    i=0
    while amount>0:
        if amount>=coins[i]:
            amount= amount - coins[i]
            x.append(coins[i])
        else:
            i+=1
    return x
        
def safe_squares_rooks(n, rooks):
    r=set()
    c=set()
    
    for i in range(n):
        r.add(i)
        c.add(i)
    for rook in rooks:
        if rook[0] in r:
            r.remove(rook[0])
        if rook[1] in c:
            c.remove(rook[1])
    return len(r) * len(c)

def count_dominators(items):
    l=items[-1] - 1 if items else 0
    c=0
    for item in reversed(items):
        if item > l:
            c+=1
            l = item
    return c

def knight_jump(knight, start, end):
    result = []
    for i in range(0, len(start)):
        result.append(abs(start[i] - end[i]))
    if set(knight) == set(result):
        return True
    return False

def pyramid_blocks(n, m, h):
    a = 0
    for index in range(h):
        a = a + (n * m)
        n += 1
        m += 1
    return a
                     
        
def sum_of_two_squares(n):
    sq= int(n**0.5)
    for i in range(sq,0,-1):
        temp= n-i*i
        if int(temp**0.5)**2==temp and int(temp**0.5)>0:
            return i , int(temp**0.5)

def count_consecutive_summers(n):
        if n <= 2:
                return 1
        count = 0
        if (n % 2) == 1:
                count += 1
                
        if (n // 2) % 2 == 1:
                m = n // 2
        else: 
                m = (n // 2) - 1
        while m > 1:
                if (n / m) == int(n / m):
                        count += 1
                m -= 2
        return count + 1


    
def count_carries(a, b):
    a = str(a)
    b = str(b)
    carry = 0;
    count = 0;
    len_a = len(a);
    len_b = len(b);
 
    while (len_a != 0 or len_b != 0):
        x = 0;
        y = 0;
        if (len_a > 0):
            x = int(a[len_a - 1]) + int('0');
            len_a -= 1;
         
        if (len_b > 0):
            y = int(b[len_b - 1]) + int('0');
            len_b -= 1;

        sum = x + y + carry;
        if (sum >= 10):
            carry = 1;
            count += 1;
        else:
            carry = 0;
    return count


def three_summers(items, goal):
    a=len(items)
    for i in range(0, a-1):
        s=set()
        cs=goal-items[i]
        for j in range(i+1, a):
            if (cs - items[j]) in s:
                return True
            s.add(items[j])
    return False
        
def count_divisibles_in_range(start, end, n):
    return(end-(start-n-start%n))//n-1 + (1 if start%n==0 else 0)

def fibonacci_word( k ):
    decimal.getcontext().prec = 165
    root_5 = decimal.Decimal( 5 ).sqrt()
    phi = ( 1 + root_5 ) / 2
    r = phi / ( 1 + ( phi * 2 ) )

    return math.floor(  ( k + 2 ) * r ) - math.floor( ( k + 1 ) * r )

def reverse_vowels(text):
        vowels = ''
        for char in text:
                if char in "aeiouAEIOU":
                        vowels += char
        string = ""
        for char in text:
                if char in "aeiouAEIOU":
                        if char.isupper()==True:
                                string += str(vowels[-1].upper())
                                vowels = vowels[:-1]
                        else:
                                string += str(vowels[-1].lower())
                                vowels = vowels[:-1]
                else:
                        string += char
        return string


def m_of_3(a,b,c):
    return sorted([a,b,c])[1]

def tukeys_ninthers(items):
    while len(items) > 1:
        l_o_m=[]
        for i in range(0,len(items),3):
            m=m_of_3(items[i], items[i+1], items[i+2])
            l_o_m.append(m)
        items= l_o_m
    
    return items[0]
            
def group_and_skip(n,out,ins):
    k=[]
    while n!=0:
        k.append(n%out)
        n=n//out
        n=n*ins
    return k

def seven_zero(n):
    k=1
    ks=0
    while True:
        if n%2==0 or n%5==0:
            m=1
            while m<=k:
                i= int(m*'7' + (k-m)*'0')
                if i%n==0:
                    ks=i
                    break
                m=m+1
        else:
            i=int(k*'7')
            ks=i if i%n==0 else 0
        k=k+1
        if ks>0:
            return ks
            break

def bridge_hand_shape(hand):
    cards=[]
    new=[]
    for (a,b) in hand:
        cards.append(b)
    i=cards.count("spades")
    new.append(i)
    j=cards.count("hearts")
    new.append(j)
    k=cards.count("diamonds")
    new.append(k)
    l=cards.count("clubs")
    new.append(l)
    return new

def expand_intervals(intervals):
    if intervals=="":
        return[]
    result=[]

    parts= intervals.split(",")
    
    for part in parts:
        id=part.find("-")
        
        if id<0:
            result.append(int(part))
        else:
            left = part[:id]
            right = part[id+1:]
            elems = list(range(int(left),int(right)+1))
            result=result+elems
    return result

def collapse_intervals(items):
    prev = min(items) if items else None
    n = list()
    for num in sorted(items):
        if num != prev+1:
            n.append([num])
        elif len(n[-1]) > 1:
            n[-1][-1] = num
        else:
            n[-1].append(num)
        prev = num
    return ','.join(['-'.join(map(str, list_item)) for list_item in n])

def count_and_say(digits):
    if len(digits) == 0:
        return ""
    else:
        result = ""
        ch = digits[0]
        count = 1
        for digit in digits[1:]:
            if digit == ch:
                count += 1
            else:
                result += str(count)
                result += ch
                count = 1
            ch = digit
        result += str(count)
        result += ch
        return result               
       
def is_perfect_power(n):
    x = 2
    while True:
        if 2 ** x > n: 
            return False
        a = 2
        b = a
        while b ** x <= n:
            b *= 2
        while b - a > 1:
            mid = (a + b) // 2
            if mid ** x <= n:
                a = mid
            else:
                b = mid
        if a ** x == n:
            return True
        x += 1

def frequency_sort(elms):
    from collections import Counter
    counts = Counter(elms)
    newlst = sorted(counts.most_common(), key=lambda a: (-a[1], a[0]))
    sublst = [([b]*n) for (b,n) in newlst]
    return[item for sublist in sublst for item in sublist]            

def reverse_ascending_sublists(items):
    ans = []
    sublst = []
    for item in items:
        if len(sublst) == 0:
            sublst.append(item)
        else:
            if item > sublst[0]:
                sublst.insert(0, item)
            else:
                ans.extend(sublst)
                sublst = [item]
    ans.extend(sublst)
    return ans

def postfix_evaluate(items):
    stack = []
    for item in items:
        if type(item) is int:
            stack.append(item)
            continue
        num1, num2 = stack.pop(), stack.pop()
        if item == '+':
            stack.append(num2 + num1)
        elif item == '-':
            stack.append(num2 - num1)
        elif item == '*':
            stack.append(num2 * num1)
        elif item == '/':
            if num1!=0:
                stack.append(num2 // num1)
            else:
                stack.append(0)
    return stack.pop()

def squares_intersect(s1, s2):
    square1x1 = s1[0]
    square1y1 = s1[1]
    square1x2 = square1x1 + s1[2]
    square1y2 = square1y1 + s1[2]

    square2x1 = s2[0]
    square2y1 = s2[1]
    square2x2 = square2x1 + s2[2]
    square2y2 = square2y1 + s2[2]

    if square1x2 < square2x1 or square2x2 < square1x1:
        return False
    if square1y2 < square2y1 or square2y2 < square1y1:
        return False
    return True

     

def nearest_smaller(items):
    n, result = len(items), []
    for (i, e) in enumerate(items):
        j = 1
        while j < n:
            left = items[i - j] if i >= j else e
            right = items[i + j] if i+j < n else e
            if left < e or right < e:
                result.append(left if left < right else right)
                break
            j += 1
        else:
            result.append(e)
    return result

def possible_words(words, pattern):
    result = []
    for word in words:
        if len(word) == len(pattern):
            for (chw, chp) in zip(word, pattern):
                if chp == "*" and chw in pattern:
                    break
                if chp != "*" and chp != chw:
                    break
            else:
                result.append(word)
    return result

def extract_increasing(digits):
  list_increasing = []
  int_current_biggest = -1
  str_next_biggest = ""
  for index in range(len(digits)):
    str_next_biggest = str_next_biggest + digits[index]
    int_next_biggest = int(str_next_biggest)
    if int_next_biggest > int_current_biggest:
      list_increasing.append(int_next_biggest)
      int_current_biggest = int_next_biggest
      str_next_biggest = ""
  return list_increasing

def bulgarian_solitaire(piles, k): 
  flag = True
  count = 0
  piles_copy = piles.copy()
  enum_list = [i for i in range(1, k+1)]
  while flag==True:
    for i in enum_list:
      if i not in piles_copy:
        count += 1
        newpile = 0
        tempPiles = []
        for pile in piles_copy:
          adjpile = pile - 1
          newpile += 1
          if adjpile > 0:
            tempPiles.append(adjpile)
        tempPiles.append(newpile)
        piles_copy = tempPiles
        break
      elif i >= len(enum_list):
        flag=False
  return count

def count_growlers(animals): 
  growlers = 0
  
  for animalIndex in range(len(animals)):
    if (animals[animalIndex] == "cat") or (animals[animalIndex] == "dog"):  # look left
      countCats = 0
      countDogs = 0
      for subAI in range(0, animalIndex):
        if (animals[subAI] == "cat") or (animals[subAI] == "tac"):
          countCats +=1
        elif (animals[subAI] == "dog") or (animals[subAI] == "god"):
          countDogs +=1
      if (countDogs > countCats):
        growlers += 1    

    elif (animals[animalIndex] == "tac") or (animals[animalIndex] == "god"): # look right
      countCats = 0
      countDogs = 0
      for subAI in range(animalIndex+1, len(animals)):
        if (animals[subAI] == "cat") or (animals[subAI] == "tac"):
          countCats +=1
        elif (animals[subAI] == "dog") or (animals[subAI] == "god"):
          countDogs +=1
      if (countDogs > countCats):
        growlers += 1    

  
  return growlers

def first_preceded_by_smaller(items, k):
    lowest_k = []
    for i in range(0,len(items)):
        if len(lowest_k) <k:
            lowest_k.append(items[i])
        else:
            if items[i]>max(lowest_k):
                return(items[i])
            elif items[i]<=max(lowest_k):
                lowest_k.remove(max(lowest_k))
                lowest_k.append(items[i])
    return(None)

def remove_after_kth(items, k):
    d = {}
    result = []
    for i in range(0,len(items)):
        if items[i] in d:
            d[items[i]] += 1
        else:
            d[items[i]] = 1
        if d[items[i]]<=k:
            result.append(items[i])
    return(result)



def ztalloc(shape):
    n = 1
    count = 0

    while True:

        try:

            if shape[-1:] == 'd':
                n =n*2
                if n%2 !=0:
                    return(None)

            elif shape[-1] =='u':
                if (((n-1)//3)!= ((n-1)/3)):
                    return(None)
                n = (n-1)//3

                if (n%2 ==0):
                    return(None)
            shape = shape[:-1]

        except:
            return(n)
    return(n)

def duplicate_digit_bonus(n):
    s = str(n)
    score = 0
    i = 0
    k = 1
    while i<len(s):
        try:
            if s[i]==s[i+k]:
                while s[i]==s[i+k]:
                    k+=1
                score += 10**(k-2)
                i +=k
                k = 1
            else:
                i+=1
        except:
            if k>1:
                score += 10**(k-2)*2
            return(score)
    return(score)

def brangelina(first,second):
    vowels='aeiou'
    i=0
    while second[i] not in vowels:
        i+=1
    second=second[i:]
    n_groups=0
    grps=[]
    in_grp=False
    
    for j in range(len(first)):
        if first[j] in vowels:
            if not in_grp:
                grps.append(j)
                in_grp= True
        else:
            in_grp=False
    n_groups=len(grps)
    if n_groups== 1:
        first = first[:grps[0]]
    else:
        first = first[:grps[-2]]
    return first+second
    
    

      
        
        
    
