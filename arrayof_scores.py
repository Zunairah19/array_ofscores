import sys

scores = list(map(int, sys.argv[1:]))

total = sum(scores)
print("Scores:", scores)
print("Sum:", total)

if scores:
    average = total / len(scores)
    print("Average:", average)
else:
    print("No scores provided; average is undefined.")