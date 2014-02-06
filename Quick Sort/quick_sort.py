# Quick Sort Exercise
def quickSort(l):
    run.ctr += 1
    if len(l) <= 1:
        return l
    else:
        pivot = l[0]
        lessor = quickSort([x for x in l[1:] if x < pivot])
        greater = quickSort([x for x in l[1:] if x >= pivot])
        return lessor + [pivot] + greater

# Take things from text box and prepare output
def run(text):
    run.ctr = 0
    outstring = ""
    numbers = map(int, text.split(' '))
    outstring += "Sorted Numbers: " + str(quickSort(numbers))
    outstring += "<br>Recursions: " + str(run.ctr)
    return outstring