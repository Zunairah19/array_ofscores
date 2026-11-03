import sys

scores = list(map(int, sys.argv[1:]))

total = sum(scores)
print("Scores:", scores)
print("Sum:", total)

if scores:
    average = total / len(scores)
    print("Average:", average)

    maximum = max(scores)
    minimum = min(scores)

    print("Maximum:", maximum)
    print("Minimum:", minimum)

else:
    print("No scores provided; average is undefined.")
    print("Maximum and minimum are undefined.")