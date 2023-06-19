import nmap


def port_scanner(begin, end, ip):
    scanner = nmap.PortScanner()

    for i in range(begin, end+1):
        res = scanner.scan(ip, str(i))
        res = res['scan'][ip]['tcp'][i]['state']

        print(f'port {i} is {res}.')


print("-------------Hoş Geldiniz---------------")
choice = input("\n 1- Port Scanner ")
if choice == '1':
    begin = input("Başlangıç Portunu Giriniz : ")
    end = input("Bitiş Portunu Giriniz : ")
    ip = input("Port kontrolu yapılacak ip adresini Giriniz : ")
    port_scanner(int(begin), int(end), ip)
else:
    print("Yanlış Seçim")
