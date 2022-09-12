from typing import List
def insertionSort(array) -> List[int]:
  for step in range(1, len(array)):
    key = array[step]
    j = step - 1
    while j >= 0 and key < array[j]:
      array[j + 1] = array[j]
      j = j - 1
    array[j + 1] = key
  return array

input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(insertionSort(data))
