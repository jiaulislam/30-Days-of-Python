import math
import os
import random
import re
import sys
	
if __name__ == '__main__':
	N = int(input())
	output = []
	for N_itr in range(N):
		name_pattern = r"^[a-z]+"


		firstNameEmailID = input().split(" ")
		# print(firstNameEmailID)
		firstName = firstNameEmailID[0]
		gmail = firstNameEmailID[1].strip()
		# print(gmail)
		if len(firstName) <= 20 and len(gmail) <= 50:
			if gmail.endswith("@gmail.com"):
				emailID = firstNameEmailID[1]
				pnl = re.findall(name_pattern, firstName)
				output.append(pnl[0])
	for name in sorted(output):
		print(name)
	