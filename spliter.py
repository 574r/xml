
def split(file_name, codes, output_name='output.xml'):
    import linecache
    f2 = open(output_name,'w') 
    for i in range(13):
        f2.write(linecache.getline(file_name, i+1))
    
    K,K1,L=get_line_number(file_name, codes)
    for i in range(len(L)):
        j=0
        while L[i]-2+j<=K1[i]-3:
            f2.write( linecache.getline(file_name, L[i]-2+j))
            j+=1
    Last_str="</CompactData>"

    f2.write(Last_str) 
    f2.close() 
    return print("Done. File name: {0}".format(output_name))


def get_line_number(file_name, codes):
    K=[]
    K1=[]
    L=[]
    t=0
    phrase="GROUP="
    with open(file_name) as f:      
        for i, line in enumerate(f, 1):
            
            if phrase in line:
                
                K.append(i)
                if t==1:
                    K1.append(i)
                    t=0
                if isinstance(codes, list):
                    for code in codes:
                        if phrase+'"'+str(code) in line:
                            L.append(i)
                            t=1
                            break
                else:       
                    if  phrase+'"'+codes in line:
                        L.append(i)
                        t=1             
        return K,K1,L

 


