#!/usr/bin/env python3
import sys
import argparse
import string

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--pattern", required=True, type=str, help="Set a pattern type (yz, bruijn, msf)")
parser.add_argument("-l", "--length", required=True, type=int, help="Length of the pattern")
parser.add_argument("-f", "--find", type=str, help="Find the offset")
parser.add_argument("-a", "--alphabet", help="Alphabet to be used in the pattern")
args = parser.parse_args()

'''
speed is fast
max length is 865,280
'''
def yz(alphabet, original_size):
  size = original_size // 4 + 1
  lower = string.ascii_lowercase
  upper = string.ascii_uppercase
  digits = string.digits
  punctuation = string.punctuation
  counter = 0
  output = ""
  while size > counter:
    output += upper[counter//(len(punctuation)*len(digits)*len(lower))%len(upper)]
    output += lower[counter//(len(punctuation)*len(digits))%len(lower)]
    output += digits[counter//len(punctuation)%len(digits)]
    output += punctuation[counter%len(punctuation)]
    counter += 1
  return output[:original_size]


'''
speed is fast
max length is 20,280
'''
def msf(alphabet, original_size):
  size = original_size // 3 + 1
  lower = string.ascii_lowercase
  upper = string.ascii_uppercase
  digits = string.digits
  counter = 0
  output = ""
  while size > counter:
    output += upper[counter//(len(digits)*len(lower))%len(upper)]
    output += lower[counter//len(digits)%len(lower)]
    output += digits[counter%len(digits)]
    counter += 1
  return output[:original_size]


'''
speed is slow
max length is 78,074,896
'''
def de_bruijn(k, n):
  try:
    _ = int(k)
    alphabet = list(map(str, range(k)))

  except (ValueError, TypeError):
    alphabet = k
    k = len(k)

  a = [0] * k * n
  sequence = []

  def db(t, p):
    if t > n:
      if n % p == 0:
        sequence.extend(a[1:p + 1])
    else:
      a[t] = a[t - p]
      db(t + 1, p)
      for j in range(a[t - p] + 1, k):
        a[t] = j
        db(t + 1, t)
  db(1, 1)
  return "".join(alphabet[i] for i in sequence)

def main():
  if args.alphabet:
    alphabet = args.alphabet
  else:
    alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

  if args.find:
    if args.pattern == "yz":
      print(yz("", args.length).find(args.find))
    elif args.pattern == "bruijn":
      print(de_bruijn(alphabet,4)[:args.length].find(args.find))
    elif args.pattern == "msf":
      print(msf("", args.length).find(args.find))
    else:
      print("[!] Unknown pattern type, use 'yz', 'bruijn' or 'msf'.")
  else:
    if args.pattern == "yz":
      print(yz("", args.length))
    elif args.pattern == "bruijn":
      print(de_bruijn(alphabet,4)[:args.length])
    elif args.pattern == "msf":
      print(msf("", args.length)) 
    else:
      print("[!] Unknown pattern type, use 'yz', 'bruijn' or 'msf'.")

if __name__ == "__main__":
  main()