import numpy as np
even=np.arange(2,31,2)
slicer=even[2:9:2]
last3=even[-3:]
alternate=even[::2]
alternate3=alternate[-3:]
print("a. Original Array :",even)
print("b. Elements fro dex 2 to 8 with step 2 :",slicer)
print("c. Last  3 Elements of he array using negative index :",last3)
print("c. Alternate elements of the array",alternate)
print("d. Display the last 3 alternate elements",alternate3)
