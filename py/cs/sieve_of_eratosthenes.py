#note_s
#description: this code define prime numbers (not best algorithm)
#benefit: ability to define speed of programs
#weakness: work temporary with one test data without exceptions
#ref: https://colab.research.google.com/drive/1dA038IiVmvzdt9BP0yB3lMDce7-h0oBy#scrollTo=Fy7pAcMnCk3U
#note_e

def clean(arr,g):
  arr_res = [i for i in arr if i%g!=0]
  return arr_res

arr = range(1,101)

while len(arr)>=2:
  sec_elem = arr[1]
  arr = clean(arr,sec_elem)
  print(sec_elem,arr)