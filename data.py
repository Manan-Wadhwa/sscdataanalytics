import csv
dict={'Animals':0,'cooking':0,'culture':0,'dogs':0,'education':0,'fitness':0,'food':0,'healthy eating':0,'public speaking':0,'science':0,'soccer':0,'Studying':0,'technology':0,'tennis':0,'travel':0,'veganism':0}

main=[]
a=open('contentxvalue.csv','r')
c=a.readlines()
for i in c:
    a=i.split('/n')
    for i in a:
        input_string=i
        output_list = [item.strip('"') for item in input_string.strip().strip('\n').split(',')]
        main.append(output_list)
print(main)
