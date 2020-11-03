# class Navi():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def newPos(self, x1, y1):
#         self.x = x1
#         self.y = y1
    
# dot = Navi(0,3)

# import numpy as np

# a = [[0,0,0,1,0,0,0,0,0,0],
#     [0,1,1,1,1,1,1,1,1,0],
#     [0,1,0,0,0,0,1,0,1,0],
#     [0,1,1,1,0,1,1,0,1,0],
#     [0,1,0,1,0,1,0,0,1,0],
#     [0,1,1,1,1,1,0,1,1,0],
#     [0,0,0,0,0,1,0,0,0,0],
#     [0,1,0,1,0,1,0,0,1,0],
#     [0,1,1,1,1,1,1,1,1,0],
#     [0,0,0,0,0,0,0,1,0,0]]


# while dot.x != 9 and dot.y != 9:
#     if a[dot.x + 1][dot.y] == 1 and a[dot.x][dot.y - 1] != 1 and a[dot.x][dot.y + 1] != 1:
#         dot.x += 1
#         print(a[dot.x][dot.y])
#     elif a[dot.x + 1][dot.y] != 1 and a[dot.x][dot.y - 1] != 1 and a[dot.x][dot.y + 1] == 1:
#         dot.y += 1
#         print(a[dot.x][dot.y])
#     elif a[dot.x + 1][dot.y] != 1 and a[dot.x][dot.y - 1] == 1 and a[dot.x][dot.y + 1] != 1:
#         dot.y -= 1
#         print(a[dot.x][dot.y])

# y = int(input("Enter the number"))
# def is_prime(num):
#     x = 1
#     while x <= num + 1:
#         if x < num: 
#             if num % x != 0:
#                 x += 1
#                 continue
#         elif x == num:
#             return True
#         else:
#             return False

# z = is_prime(y)
# if z == True:
#     print("It was true")
# else:
#     print("It was not")

# def isPrime(n) : 
#     if n >= 0 and n <= 3: 
#         return True
#     if n % 2 == 0 or n % 3 == 0: 
#         return False
#     i = 5
#     while i * i <= n: 
#         if n % i == 0 or n % (i + 2) == 0 : 
#             return False
#         i = i + 6
  
#     return True
# a=int(input('Enter Number:'))
# result = isPrime(a)
# print(result)


# def is_prime(x):
#     i = 2
#     while i <= x:

#         if x == i:
#             return True
#         elif x % i == 0:
#             return False
#         elif x % i != 0:
#             i += 1
# y = []
# for z in range(2, 100):
#     if is_prime(z) == True:
#         y.append(z)
# print(y)
    # print(is_prime(z))

# def reverse_words(a):
#     d = []
#     p = ""
#     x = a.split()
#     for a in x:
#         d.append(a[::-1])
#     for b in d:
#         p += (str(b))
#     return p
        
# def reverse_words(a):
#     data = a.split(' ')
#     reverse=[]
#     for i in data:
#         reverse.append(i[::-1])
#     text=''
#     for j in reverse:
#         if j is not reverse[-1]:
#             text+=(str(j)+' ')
#         else:
#             text+=(str(j))
#     return text
import numpy as np
big = 0
middle = 0
small = 0
# p = np.array([(0, 0), (5, 10), (7, 15)])

# # for x in range(len(p)):
# #     if p[x+1[0]] - p[x[0]] > big:
# #         big = p[(x+1)[0]] - p[x[0]]
# # for i in range(p.shape[0]):
# #     for j in range(p.shape[1]):
# #         print(p[i], p[j])


# x = [24, 57, 11]
# for a in len(x):
#     if x[a] > x[a + 1]:
#         big = x[a]
    

# p = [0, 0]
# q = [5, 10]
# r = [7, 15]
# s = [9, 21]


# if q[0] - p[0] > r[0] - q[0]:
#     big = q[0] - p[0]
#     small = r[0] - q[0]
#     print(big, middle, small)
# else:
#     big = r[0] - q[0]
#     small = q[0] - p[0]
#     print(big, middle, small)
# if s[0] - r[0] > big and s[0] - r[0] > small:
#     middle = big
#     big = s[0] - r[0]
# if s[0] - r[0] < big and s[0] - r[0] > small:
#     middle = s[0] - r[0]
# if s[0] - r[0] < small:
#     middle = small
#     small = s[0] - r[0]
# print(big, middle, small)

ad = ("123 Main Street St. Louisville OH 43071,432 Main Long Road St. Louisville OH 43071,786 High Street Pollocksville NY 56432,"
  "54 Holy Grail Street Niagara Town ZP 32908,3200 Main Rd. Bern AE 56210,1 Gordon St. Atlanta RE 13000,"
  "10 Pussy Cat Rd. Chicago EX 34342,10 Gordon St. Atlanta RE 13000,58 Gordon Road Atlanta RE 13000,"
  "22 Tokyo Av. Tedmondville SW 43098,674 Paris bd. Abbeville AA 45521,10 Surta Alley Goodtown GG 30654,"
  "45 Holy Grail Al. Niagara Town ZP 32908,320 Main Al. Bern AE 56210,14 Gordon Park Atlanta RE 13000,"
  "100 Pussy Cat Rd. Chicago EX 34342,2 Gordon St. Atlanta RE 13000,5 Gordon Road Atlanta RE 13000,"
  "2200 Tokyo Av. Tedmondville SW 43098,67 Paris St. Abbeville AA 45521,11 Surta Avenue Goodtown GG 30654,"
  "45 Holy Grail Al. Niagara Town ZP 32918,320 Main Al. Bern AE 56215,14 Gordon Park Atlanta RE 13200,"
  "100 Pussy Cat Rd. Chicago EX 34345,2 Gordon St. Atlanta RE 13222,5 Gordon Road Atlanta RE 13001,"
  "2200 Tokyo Av. Tedmondville SW 43198,67 Paris St. Abbeville AA 45522,11 Surta Avenue Goodville GG 30655,"
  "2222 Tokyo Av. Tedmondville SW 43198,670 Paris St. Abbeville AA 45522,114 Surta Avenue Goodville GG 30655,"
  "2 Holy Grail Street Niagara Town ZP 32908,3 Main Rd. Bern AE 56210,77 Gordon St. Atlanta RE 13000")


code = ("OH 43071,NY 56432,ZP 32908,AE 56210,RE 13000,EX 34342,SW 43098,AA 45521,GG 30654,ZP 32908,AE 56215,RE 13200,EX 34345,"
     "RE 13222,RE 13001,SW 43198,AA 45522,GG 30655,XX 32321,YY 45098")
    
a = 'AA 45522:Paris St. Abbeville,Paris St. Abbeville/67 ,670'
b = 'AA 45522:Paris St. Abbeville,Paris St. Abbeville/67,670'

def travel(r, zipcode):
    address = ""
    number = ""
    x = 0
    if len(zipcode) >= 7:
        for a in r.split(","):
            cnt = 0
            if zipcode in a:
                print(a)
                for b in a:
                    if b == " ":
                        break
                    else:
                        cnt += 1
                if x == 0:
                    address += a[cnt+1:-9]
                    number += a[:cnt]
                    x += 1
                else:
                    address += "," + a[cnt+1:-9]
                    number += "," + a[:cnt]
    return zipcode + ":" + address + "/" + number
    # your code
######################################################################################
def travel(r, zipcode):
    streets = []
    nums = []
    addresses = r.split(',')
    for address in addresses:
        if ' '.join(address.split()[-2:]) == zipcode:
            streets.append(' '.join(address.split()[1:-2]))
            nums += address.split()[:1]
    return '{}:{}/{}'.format(zipcode, ','.join(streets), ','.join(nums))
#####################################################################################
from collections import defaultdict
from re import compile, match

REGEX = compile(r'(?P<num>\d+) (?P<adr>.+) (?P<st_zip>[A-Z]{2} \d{5})')


def travel(addresses, zipcode):
    by_zipcode = defaultdict(lambda: defaultdict(list))
    for address in addresses.split(','):
        m = match(REGEX, address).groupdict()
        by_zipcode[m['st_zip']]['adr'].append(m['adr'])
        by_zipcode[m['st_zip']]['num'].append(m['num'])
    result = by_zipcode[zipcode]
    return '{}:{}/{}'\
        .format(zipcode, ','.join(result['adr']), ','.join(result['num']))