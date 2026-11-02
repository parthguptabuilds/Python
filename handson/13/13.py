import copy

orignal=[["Apple","Banana"],"Mango"]

assigned=orignal
shallow=assigned.copy()
deep_copy=copy.deepcopy(orignal)
assigned[0].append("orange")
assigned[1]="Grapes"
shallow[0].append("Kiwi")
shallow[1]="Pineapple"

deep_copy[0].append("cherry")
