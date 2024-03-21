string = "I love you"

print(string[0:6])  #--> I love
print(string[-3: ]) #--> you
print(string[:])    #--> I love you
print(string[: : 2])    #--> Ilv o (Inlnvn non)
print(string[: : 3])    #--> Io u (Innonn nnu)
print(string[: : -1])    #--> uoy evol I (inverse)
print(string+string[: : -1])    #--> I love youuoy evol I (reflected)

replaceString = "Replace Method"
print(replaceString.replace("e", "E")) #--> REplacE MEthod
print(replaceString.replace("", ",")) #--> ,R,e,p,l,a,c,e, ,M,e,t,h,o,d,
print("R"+ replaceString[1:-1].replace("", ",")+"d") #--> R,e,p,l,a,c,e, ,M,e,t,h,o,d