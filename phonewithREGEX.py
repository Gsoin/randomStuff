import re
import sys


phoneNum = input("Please Enter Your Phone Number: ")

regex = r"\w{3}-\w{3}-\w{4}"

lmao = re.search(regex, phoneNum)

print(lmao)
