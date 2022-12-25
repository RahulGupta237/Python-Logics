m = []
y=[]
import calendar
for i in range(1, 13):
    m.append(list(calendar.month_name))
    
print(m)
print(y)
print(m[0][1::])
print(type(m[0][1::][0]))
#text =" my date is January|1996"
text1 =" my date is January-1996"
text2=text1.lower()
print(text2)
text=input("enter a string what you want to test")
result1=([i for i in range(1,20022) if str(i) in text if "   " not in text])
result=([i for i in  m[0][1::] if i[:3] in  text if ('-') not in text if "   " not in text])
print(result)
if result==[] and result1==[]:
    print("False")
else:
    print("True")


