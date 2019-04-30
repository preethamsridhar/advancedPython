import sys
# =============================================================================
# for i in range(len(sys.argv)):
#     if i == 0:
#         print("Function name: ", sys.argv[0])
#     else: 
#         print("%d. argument: %s" %(i, sys.argv[i]))
#     
#     
# =============================================================================
# =============================================================================
# for i in (sys.stdin, sys.stdout, sys.stderr):
#     print(i)
# =============================================================================

# =============================================================================
# print("Going via stdout")
# sys.stdout.write("Another way to do it!")
# x = input("read value via stdin: ")
# print(x)
# 
# print("type in value: "dsfd) 
# sys.stdin.readline()[:-1]
# 
# =============================================================================
# =============================================================================
# 
# while True:
#     print("Yet anpother iteration")
#     try:
#         number = input("Enter a number: ")
#     except EOFError:
#         print("\nciao")
#         break
#     else:
#         number = int(number)
#         if number == 0:
#             print("0 has no inverse", file=sys.stderr)
#         else: 
#             print("inverse of %d is %f" %(number, 1.0/number))
# =============================================================================

print("coming throught stdout")

sav_stdout = sys.stdout

fh = open("text.txt", "w")
sys.stdout = fh

while True:
    try:
        number = input("Enter a number: ")
    except EOFError:
        print("end")
        break
    else:
        print(number)
        
sys.stdout = sav_stdout
fh.close()




