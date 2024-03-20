import csv
def no1uid(name,row):
    main=[]
    a=open(name,'r')
    c=a.readlines()
    for i in range(0,len(c)):
        b=c[i]
        lst=b.split(',')
        main.append(lst[row])
    return(main)
final=[]
final2=[]
uid1=no1uid('Untitled-1.csv',1)
uid2=no1uid('no3.csv',1)
cats=no1uid('no3.csv',4)
dict={cats: uid2 for uid2, cats in zip(cats,uid2)}
for i in uid1:
    final.append(dict.get(i))
for i in final:
    final2.append(i.replace('"', ''))
print(final2)
lst = final2

# Define the output CSV file path
csv_file_path = "output.csv"

# Write the list to the CSV file
with open(csv_file_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for item in lst:
        csvwriter.writerow([item])

print("CSV file has been created successfully.")
    