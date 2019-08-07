import csv

icao_list_icao = []
icao_list_lat = []
icao_list_lon = []
icao_list_name = []

with open('icaodata.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    index = 0
    for row in reader:
        if index > 0:
            icao_list_icao.append(row[0])
            icao_list_lat.append(float(row[1]))
            icao_list_lon.append(float(row[2]))
            icao_list_name.append(row[5] + ", " + row[6] + ", " + row[7] + ", " + row[8])
        index +=1
    csv_file.close()
    
dep_list = []
arr_list = []
acf_list = []

with open('r.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for row in reader:
        if len(row) >= 9:
            dep_list.append(row[2])
            arr_list.append(row[4])
            acf_list.append(row[8])

    csv_file.close()
    
code_icao = []
code_iata = []

with open('c.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    index = 0
    for row in reader:
        print(row[0])
        if (len(row) >= 3) and (index > 0):
            code_icao.append(row[0])
            code_iata.append(row[2])
        index +=1
    csv_file.close()    

all_in_list = []
    
for icao_index in range(0, len(icao_list_icao)):
    act_iata = "xxxx"
    print(str(icao_list_icao[icao_index]))
    
    for iata_index in range(0, len(code_icao)):
        if (code_icao[iata_index] == icao_list_icao[icao_index]):
            act_iata = code_iata[iata_index]

    route_found = False
    
    if (act_iata != "xxxx"):
        for route_index in range(0, len(dep_list)):
            if dep_list[route_index] == act_iata:
                route_found = True
                
    if route_found == True:
        all_in_list.append(icao_list_icao[icao_index])

out_file = open("out.txt","w")
        
for allin_index in range(0, len(all_in_list)):
    out_file.write(str(all_in_list[allin_index]) + "\n")
out_file.close()    