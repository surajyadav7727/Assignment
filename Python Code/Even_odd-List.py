def even_sum(l):
         esum=0
         for i in l:
                  esum+=i
         return esum
def odd_sum(l):
         osum=0
         for i in l:
                  osum+=i
         return osum
if __name__ == '__main__':
         no = [15, 23, 34, 41, 26, 13, 18]
         even_list=[]
         odd_list = []
         num = 0
         while(num < len(no)):
                  if no[num] % 2 == 0:
                           even_list.append(no[num])
                  else:
                           odd_list.append(no[num])
                  num += 1
         print("even")
         for i in even_list:
                  print(i)
         print("odd")
         for i in odd_list:
                  print(i)
         evensum=even_sum(even_list)
         oddsum=odd_sum(odd_list)
         result = {'Even_sum':evensum,'odd_sum':oddsum}
         print(result)





