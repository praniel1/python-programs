1 . CHECK SUM
data = Take input() eg : 4500 003c 1c46 4000 4006 b1e6 ac10 0a63 ac10 0a0c
loop till the end of data:
    num1 = take 4 digits and convert to binary
save 6th num as checksum
make 6th num = 0000 // check sum has to be made 0 to check it later
add all the numbers together
take the complement of the number
compare number to the recieved checksum:
    if true then
        data is uncorrupted
    else
        data is corrupted

2. Compute ttl
    take ttl = slice from 12 to 14 of data
    convert ttl to decimal

3. Computing Routing metrics
    protocol = slice from 14 to 16 of data
    if(protocol == 00):
        print "HOP OPT"
    elif(protocol == 01)
        print "ICMP"
    elif(protocol == 02)
        print "IGMP"
    elif(protocol == 03)
        print "GGP"
    elif(protocol == 04)
        print "IP in IP"
    elif(protocol == 05)
        print "ST"
    elif(protocol == 06)
        print "TCP"
    elif(protocol == 07)
        print "CBT"
    elif(protocol == 08)
        print "EGP"

4. Getting Route with different possibilities
    des = Destination address
    N = network prefix
    if ( N matches a directly connected network address )
        Deliver datagram to D over that network link;
    else if ( The routing table contains a route for N )
        Send datagram to the next-hop address listed in the routing table;
    else if ( a default route exists )
        Send datagram to the default route;
    else
        Send a forwarding error message to the originator;