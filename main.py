#!usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("-----------------------------------------------------------")

print("-------------------Hoş geldiniz----------------------------")

ip_address = input("Lütfen Taramak İstediğiniz İp adresini Giriniz : ")
print("Girdiğiniz İp Adres : ", ip_address)
type(ip_address)


info = input("""\n Lütfen girdiğiniz ip adresini hangi taramayı yapmak istediğinizi seçiniz
                1) SYN ACK Taramsı
                2) UDP Taraması
                3)Comprehensive Taraması \n""")

if info == '1':
    scanner.scan(ip_address, '-p-')
    print(scanner.scaninfo())
    print("Ip Durumu: ", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Açık Portlar: ", scanner[ip_address]["tcp"].keys())
