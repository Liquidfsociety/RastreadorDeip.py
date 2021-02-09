#####################################
#          Liquid Group !          #  
#   Programado pelo Liquid Group   #
#      Liquid fsociety Group       #
#####################################

#!/usr/bin/python3



from __future__ import print_function 
import argparse
import socket

 
try:


        import pygeoip
except ImportError:
        print("[!] Nao deu pra rodar o RastreadorDeIp. Por favor tenha certeza que voce esteja rodando o requiriments.py script first.")
        exit()





def banner():
      
         print(".: RastradorDeiP v0.6 :.")
         print("IP Tracing tool by Liquid fsociety Group // Liquid 2021")
         print("Usage: python iplocator -u [URL] / -a [IP]")

def lookup(ip):

         print("IP:", ip)
         db = pygeoip.GeoIP("GeoLiteCity.dat")
         geo_data = db.record_by_name(ip)
         print("Country: " + geo_data["country"].encode("utf-8"))
         if geo_data["city"]:
                     
                     print("City: " + geo_data["city"].encode("utf-8"))
         print("Logitude: " + str(geo_data["logitude"]).encode("utf-8"))
         print("Latitude: " + str(geo_data["latitude"]).encode("utf-8"))
         s = raw_input("\nVoce quer salvar os dados em um arquivo .txt? [Y/n]: ")
         if s == "n" or s == "N" or s == "no" or s == "No" or s == "NO":
                  exit()

         else:

               
                 f = open(str(ip) ,'w+')
                 c1 = "Country: " + geo_data["country_name"].encode("utf-8") + "\n"
                 f.write(str(c1))
                 if geo_data["city"]:
                           c2 = "City: " + geo_data["city"].encode("utf-8") + "\n" 
                           f.write(str(c2))
                 l1 = "Longitude: " + str(geo_data["longitude"]).encode("utf-8") + "\n"
                 f.write(str(l1))
                 l2 = "Latitude: " + str(geo_data["latitude"]).encode("utf-8") +"\n"
                 f.write(str(12))
                 f.close()


def arguments():
       
         parser = argparse.Argumentsparser()
         parser.add_argument("-u", "--URL", help="A URL para o Website.")
         parser.add_argument("-a", "--IP", help="O IP do Dispositivo.")
         args = parser.parse_args()
         url = args.URL
         ip = args.IP
         if ip:
     
                 try:



                         
                            socket.inet_aton(ip)
                            lookup(ip)
                 except socket.error:
                         print("IP Invalido. Saindo..")
                         exit()
        elif url:
                try:
      
                           URL_IP = socket.gethostbyname(str(url))
                           lookup(URL_IP)
                except socket.gaierror:
                        print("URL Invalida. Saindo..")
                        exit()
       if not ip and not url:
               banner()
arguments()
 
             
                    
