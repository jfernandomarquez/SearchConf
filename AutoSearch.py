import re 

regex="^\[\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\]$"
data = open('sample.txt','r')
line_count = 0
array_line_ip =[]
dict_ip = {}
sucursales=["321","432","543","654"]

with open("sample.txt", "r") as file:
    for line in file:
      line_count += 1
      if re.match(regex, line):
        array_line_ip.append(line_count)
        dict_ip.update({line_count:line.replace("[","").replace("]","")})

# adicionar la linea final del archivo
array_line_ip.append(line_count)

same_file = open('sample.txt')
content = same_file.readlines()
for suc in sucursales:
  for k in range(len(array_line_ip)-1):
    for x in range(array_line_ip[k]-1,array_line_ip[k+1]-1):
        if content[x].find(suc) != -1:
          print("%s,%s"  %  (suc,dict_ip[array_line_ip[k]]))
