
def bubble_sort(arr):
            n=len(arr)
            for i in range(n):
                    swaped=False
                    for j in range(0,n-i-1):
                            if arr[j]>arr[j+1]:
                                    arr[j],arr[j+1]=arr[j+1],arr[j]
                                    swaped=True
                    if not swaped:
                            break
arr=[2,1,4,3,6,5,8,7]
bubble_sort(arr) 
print("sorted array is",arr) 









       


                











               







     
     

               
          






           
                       
     

        









                
        

                                    

