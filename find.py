a=["22","66","44","78","22","44"]
i=0
while i<len(a):
    if(a[i]=="44" and a.count("44")>1):
        print("found at",i )
    
        
    else:
        print("not found")
        
    
    i+=1