name = 'ssss' 
rate = 1500
my_qualification = 'middle'
if rate < 1000:     
    qualification = 'junior'    
if rate >= 1000 and rate < 2200:
  qualification = 'middle'
    
if rate >= 2200:
    qualification = 'senior'
    
answer = "My name is "+name+"! I am the "+qualification+" developer."
print(answer)