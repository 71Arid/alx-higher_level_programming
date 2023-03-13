#!/usr/nin/python3
for i in range(ord('z'), ord('a') - 1, - 1)
    print(chr(i) + chr(i - 32) if i % 2 == 1 else '', end='')
