#!/usr/bin/python3
print("{}".format(
    ", ".join("{:02d}".format(i)
              for i in range(1, 10))), end=', ')
print("{}".format(
    ", ".join("{:02d}".format(a)
              for a in range(10, 100)
              if any(sorted(str(a)) == sorted(str(b))
                     for b in range(a + 1, 100)))))
