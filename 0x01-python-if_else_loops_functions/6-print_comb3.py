#!/usr/bin/python3
for num1 in range(10):
    for num2 in range(num1 + 1, 10):
        if num1 < num2:
            print("{:02d}".format(num1 * 10 + num2), end=", "
                  if num1 * 10 + num2 != 89 else "\n")
