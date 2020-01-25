# Ethical-Hacking-Concept-Network-Scanner

While there are several network scanner tools available on the net, I wanted to create a low-level one that will work for linux machines and is written using python and scapy.

This tool is just a proof of concept and not intended to be used for any illegal or unethical activity. It should only be used on machines and networks that you as a user own and/or have written permission to use and access.

# Notes of use:

- I used argparse to allow the user to input a target into the command line 

    `"-t", "--target", help="specify the target IP address or range you want to hit: Example - 10.0.2.1/24."`

- user can input an exact IP address for the target or a range.

    - so if you wanted to target a specific machine just type in something like 10.0.2.15 and you'll get the MAC address.

    - if you want the entire range of options add /24 to the end like in the help example and it will scan the entire network returning all IP address and their coresponding MAC address. 

- I added some console styling so that it looks clean and easy to read in the console when the command is run. 

- reminder, this should not be used against real targets. Its not very stealthy and thus most IDS will (or at least should) pick up on this. This is for understanding purposes only.

- Can be run using python2 or python3
