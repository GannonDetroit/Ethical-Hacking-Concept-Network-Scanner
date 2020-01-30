
import scapy.all as scapy
import argparse

def get_argument():
    # allow me to parse out arguments/options/flags from the command line.
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="specify the target IP address or range you want to hit: Example - 10.0.2.1/24.")
    options = parser.parse_args()
    # conditionals in case user forgets to enter the argument for target.
    if not options:
        parser.error("[-] Please specify a target, use --help for more info. ")
    return options


def scan(ip):
    # uses scapy to send packets out to designated ip(s) to get their MAC address
    arp_request = scapy.ARP(pdst=ip)
    #  how we put the destination MAC address into the packets we send out from our MAC address.
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # creating a new packet that is the combo of the above two packets. Asking who has an given IP (or range of IPs)
    # and to send the response to our machine.
    arp_request_broadcast = broadcast/arp_request
    # srp allows us to send packets with a custom ether part, which we did above. the responses will either be answered
    # or unanswered packets. the timeout only lets it weight up to 1 second for a response, otherwise we'll never exit this.
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    # prep data for better display in the terminal.
    clients_list = []
    for element in answered_list:
        client_dict = {"IP": element[1].psrc, "MAC": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list


def print_result(results_list):
    # make the data look pretty in the terminal
    print("IP\t\t\tMAC Address\n---------------------------------------------------------------")
    for client in results_list:
        print(client["IP"] + "\t\t" + client["MAC"])

# invoke the functions
options = get_argument()
scan_result = scan(options.target)
print_result(scan_result)