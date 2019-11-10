from pyspark import SparkContext, SparkConf
import re

#Check if the line match the expected input pattern. Return a line with the expected pattern
def check_input(line):
    #Expected input: 133.43.96.45 - - [01/Aug/1995:00:00:23 -0400] "GET /images/launch-logo.gif HTTP/1.0" 404 1713
    pattern = '(.*) - - \[(.*)\] "(.*)" (.*)'

    aux = re.match(pattern, line)

    if (aux):
        if (aux.group(1) == ''):
            host = 'UnknownHost'
        else:
            host = aux.group(1)
        if (aux.group(2) == ''):
            date = '00/00/0000'
        else:
	    #Check if there is a date with the pattern: 01/Aug/1995   
            full_date = re.match(r'\d{2}\/...\/\d{4}:.*', aux.group(2))
            if (full_date):
                date = full_date.group(0).split(':')[0]
            else:
                date = '00/00/0000'
        if (aux.group(3) == ''):
            request = 'UnknownUrl'
        else:
            #HTTP Request elements: METHOD RESQUEST VERSION
            full_request = re.match(r'(GET|POST|HEAD|PUT|DELETE|OPTIONS|TRACE|PATCH) (.*) (HTTP.*)', aux.group(3))
            if (full_request):
                #Remove " from request, for instance: GET /shuttle/missions/sts-34/mission-sts-34.html"><IMG images/ssbuv1.gif SRC="images/small34p.gif/ HTTP/1.0
                request = full_request.group(2).replace('"','')
            else:
                request = 'UnknownUrl'
        if (aux.group(4) == ''):
            error_id = 'UnknownId'
            bytes_used = 0
        else:
            error_bytes = aux.group(4).split(" ")
            if (len(error_bytes) == 2):
                error_id = error_bytes[0] if error_bytes[0].isdigit() else 'UnknownId'
                try:
                    #Some bytes are the string -
                    bytes_used = int(error_bytes[1])
                except:
                    bytes_used = 0
            else:
                error_id = 'UnknownId'
                bytes_used = 0

        return "{} - - [{}] \"{}\" {} {}".format(host, date, request, error_id, bytes_used)
        
    else: 
        return 'UnknownHost - - \[00/00/0000\] \"UnknownUrl\" UnknownId 0'

#Filter the line returning a key/value pair: (URL, ErrorID)
def get_errors(line): 
    line = line.split('"')
    url = line[1]
    error_id = line[2].split(" ")[1] #Line after split: ['', '304', '0']
    
    return (url,error_id)

#Filter the line returning a key/value pair: (Date, ErrorID)
def get_date(line):
    line_error = line
    line_error = line_error.split('"') 
    error_id = line_error[2].split(" ")[1] 
    line = line.split("[")
    line = line[1].split("]")
    date = line[0]
    
    return (date,error_id)

#Filter the line returning the bytes used
def get_bytes(line):
    line = line.split('"') 
    bytes_used = int(line[2].split(" ")[2]) #Line after split: ['', '304', '0']
    
    return bytes_used



conf = SparkConf().setAppName("Nasa").setMaster("local[*]")
sc = SparkContext(conf=conf)

requests = sc.textFile("input/")
requests = requests.map(check_input)
requests.cache()

#Get total distinct hosts
unique_hosts = requests.map(lambda x: x.split(" ")[0]).filter(lambda x: x != 'UnknownHost')
num_unique_hosts = unique_hosts.distinct().count()

#Get total 404 errors
errors_404 = requests.map(get_errors).filter(lambda x: x[1] == '404')
num_errors_404 = errors_404.count()

errors_404.cache()

#Get top 5 urls with 404 error
url_errors_404 = errors_404.map(lambda x: (x[0],1)).reduceByKey(lambda x,y: x + y)
rank_url_errors_404 = url_errors_404.map(lambda x: (x[1], x[0])).sortByKey(ascending=False) #Inverting key/value to generate a rank using value as new key
top5_url = rank_url_errors_404.take(5)

#Get total errors 404 by day
errors_404_date = requests.map(get_date).filter(lambda x: x[1] == '404').countByKey()

#Sum total bytes returned
bytes_used = requests.map(get_bytes).reduce(lambda x,y: x+y)

#Show results
print("\nO número de hosts únicos: {}\n".format(num_unique_hosts))

print ("O total de erros 404: {}\n".format(num_errors_404))

print ("As 5 URL's que mais causaram erro 404:")
for result in top5_url:
        print ("URL: {} Quantidade: {}".format(result[1], result[0]))

print ("\nA quantidade de erros 404 por dia: ")
for result in errors_404_date:
        print ("Dia: {} Quantidade: {}".format(result, errors_404_date[result]))

print ("\nA quantidade de bytes utilizados: {}\n".format(bytes_used))
