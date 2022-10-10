
from slashcommand.secgroup import ip_add, ip_clr, status

def run():
    print(ip_clr.cleanIngress('sg-0d3edb7db7b5e36db','eu-north-1'))
    #print(status.viewIngress('sg-0d45f6f4686fc0055','eu-north-1'))
    #print(ip_add.vpnAdd('158.62.32.38/32','sg-0d45f6f4686fc0055','eu-north-1'))


