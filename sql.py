f = open("myfile.txt", "w")
f.write("\n09875 - Bath-soap [2345] - 25")
f.close()
total=0.0;
#open and read the file after the appending:
for i in range(0,100):
    num =input("Type Number : ")
    if(num=="exit"):
        break;
    else:
        search = open("myfile.txt")
        for line in search:
            if num in line:
                v=line;
        def convert(v): 
            return (v.split()) 
        l=convert(v);
        #print(l[5]); 
        total=total+float(l[5]);
        l="";
print(total);
    
