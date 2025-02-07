#sabyasachi palita

# def bubble_sort(arr):
#             n=len(arr)
#             for i in range(n):
#                     swaped=False
#                     for j in range(0,n-i-1):
#                             if arr[j]>arr[j+1]:
#                                     arr[j],arr[j+1]=arr[j+1],arr[j]
#                                     swaped=True
#                     if not swaped:
#                             break
# arr=[2,1,4,3,6,5,8,7]
# bubble_sort(arr) 
# print("sorted array is",arr) 






#insertion sort in python

# def insertion_sort(a):
#         for j in range(len(a)):
#                key =a[j]
#                i=j-1
#                while i>=0 and a[i]>key:
#                        a[i+1]=a[i]
#                        i=i-1
#                        a[i+1]=key
#         return a

# s=[2,1,4,3]
# print(insertion_sort(s)) 
# 
# 
# 
# def bubble_sort(a):
#             n=len(a)
#             for i in range(n):
#                     swaped=True
#                     for j in range(0,n-i-1):
#                             if a[j]>a[j+1]:
#                                     a[j],a[j+1]=a[j+1],a[j]
#                                     swaped=False
#                     if not swaped:
#                             break

# a=[2,1,4,3]
# bubble_sort(a)
# print("sorted array is that ",a)
# 
# 
# n=input("enter string:")
# vowels="aeiouAEIOU"
# vowels_count=0
# consonent_count=0
# for char in n:
#             if char.isalpha:
#                     if char in vowels:
#                             vowels_count+=1
#                     else:
#                             consonent_count+=1        

                    
                    
                    
           
# print("the vowels and consonents is",vowels_count,consonent_count) 
#sabyasachi palita
# lcs problem in using python
# a="sabya"
# b="sachi"

# def lcs(i,j):
#         if(i==0) or (j==0):
#                 return 0
#         elif(a[i-1]==b[j-1]):
#                 return 1+lcs(i-1,j-1)
#         else:
#                 return max(lcs(i,j-1),lcs(i-1,j))
# print(lcs(len(a),len(b)))



#sabyasachi palita
# str="SABYA"
# print(str.lower())


# a=lambda a,b :a-b
# print(a(2,3))

# list=[1,2,3,1,3]
# d=[]
# for i in list:
#         if list.count(i)>1 and i not in d:
#                 d.append(i)
                
# print(d) 
# 
# a=input("enter string:")
# b=a[::-1]  
# if a==b:
#         print("palindrom character")
# else:
#         print("not")
# s="sabya"
# sd=s[1::3] 
# print(sd) 
# 
# 
# import keyword
# print(keyword.kwlist)

# str="sabya"
# d=str[:4:3]
# print(d)



#Bubble sort
# def bubble_sort(a):
#         n=len(a)
#         for i in range(n):
#                 swaped=True
#                 for j in range(0,n-i-1):
#                         if a[j]>a[j+1]:
#                                 a[j],a[j+1]=a[j+1],a[j]
#                                 swaped=True

#                 if not swaped:
#                         break

# a=[2,1,5,4,3]
# bubble_sort(a)
# print("the sorted array is that",a)


# insertion sort
# def insertion_sort(a):
#         for j in range(len(a)):
#                key=a[j]
#                i=j-1
#                while i>=0 and a[i]>key:
#                 a[i+1]=a[i]
#                 i-=1
#                 a[i+1]=key
#         return a

# s=[2,1,4,3,8,5,7,6]
# print(insertion_sort(s))


# sabyasachi palita
# d="smruti"
# s=d[2:5:2]
# print(s)


# def merge_sort(arr):
#      while len(arr)<=1:
#           return arr
#      mid=len(arr)//2
#      left_arr=arr[:mid]
#      right_arr=arr[mid:]
#      left_arr=merge_sort(left_arr)
#      right_arr=merge_sort(right_arr)
#      return merge(left_arr,right_arr)

# def merge(left_arr,right_arr):
#      i=0
#      j=0
#      result=[]
#      while i<len(left_arr) and j<len(right_arr):
#           if left_arr[i]<=right_arr[j]:
#                result.append(left_arr[i])
#                i+=1
#           else:
#                result.append(right_arr[j])
#                j+=1
#      result+=left_arr[i:]
#      result+=right_arr[j:]
#      return result


# arr=[2,1,3,4,7,6,5]
# sorted_arr=merge_sort(arr)

# print("the sorted array is that ",sorted_arr)


               



#quick_sort
# def partition(a,low,high):
#      if len(a)<=1:
#           return a
#          pivort=a[low]
#      i=low+1
#      j=high
#      while True:
#           while i<=j and a[i]<=pivort:
#                i+=1
#           while i<=j and a[j]>pivort:
#                j-=1
#           if i<=j:
#                a[i],a[j]=a[j],a[i]
#           else:
#                break
#      a[low],a[j]=a[j],a[low]
#      return j

def quick_sort(a,low,high):
     if(low<=high):
          piv=partition(a,low,high)
          quick_sort(a,low,piv-1)
          quick_sort(a,piv+1,high)

arr=[2,1,5,4,3,7,6]
print("original array is",arr)
quick_sort(arr,0,len(arr)-1)
print("sorted array is that",arr)




# a=(1,2,3)
# print(id(a))

# b=(1,7,8)
# print(id(b))
# if a is b:
#      print("true")
# else:
#      print("not")     
     

# merge sort
# def merge_sort(arr):
#      if len(arr)<=1:
#           return arr
#      mid=len(arr)//2

#      left_arr=arr[:mid]
#      right_arr=arr[mid:]
#      left_arr=merge_sort(left_arr)
#      right_arr=merge_sort(right_arr)
#      return merge(left_arr,right_arr)

# def merge(left_arr,right_arr):
#      i=0
#      j=0
#      result=[]
#      while i<len(left_arr) and j<len(right_arr):
#           if left_arr[i]<=right_arr[j]:
#                result.append(left_arr[i])
#                i+=1
#           else:
#                result.append(right_arr[j])
#                j+=1
#      result=result+left_arr[i:]
#      result=result+right_arr[j:]
#      return result

# arr=[2,1,4,3,5]
# sorted=merge_sort(arr)
# print(sorted)               
          




# quick sort  
def partition(a,low,high):
    
     pivot=a[low]
     i=low+1
     j=high
    
     
       
    

     while True:
          while i<=j and a[i]<=pivot:
               i+=1
          while i<=j and a[j]>pivot:
               j-=1
          if (i<=j):
               a[i],a[j]=a[j],a[i]
          else:
               break
     a[low],a[j]=a[j],a[low]
     return j

def quick_sort(a,low,high):
     if(low<=high):
             piv=partition(a,low,high)
             quick_sort(a,low,piv-1)
             quick_sort(a,piv+1,high)
     
a=[2,1,4,3]
print("the original array is",a)
quick_sort(a,0,len(a)-1) 
print("the sorted array is that",a)

           
                       
     

        









                
        

                                    

