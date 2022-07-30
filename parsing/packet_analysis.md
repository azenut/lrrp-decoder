# PACKET ANALYSIS

This analysis is performed on the data extracted manually from 4 packets in the [file](./dsd_log.txt). The file is the output of the comand `DSDplus [options] > dsd_log.txt`

## 1

The analysis can be done by using a packet analyzer like [Wireshark](https://www.wireshark.org/) or using an online tool like [Hex Packet Decoder](https://hpd.gasmi.net/)

45 00 00 2D \<Ipv4 header>  
FA EF 00 00  
40 11 66 45  
0C 00 00 8B \<src: 12.0.0.193>  
0D 00 00 01 \<dst: 13.0.0.1>  
0F A1 0F A1 \<src_port: 4001> <dst_port: 4001>  
00 19 72 2D

### UDP payload (17 bytes)
0D 0F 22 04 11 22 33 44 66  
3A 10 1D 44 \<latitude>  
0B C1 E4 65 \<longitude>  

## 2
45 00 00 2D  
FA F0 00 00   
40 11 66 44  
0C 00 00 8B   
0D 00 00 01   
0F A1 0F A1  
00 19 D3 21  

### UDP payload
0D 0F 22 04 11 22 33 44 66  
3A 10 2A 74 \<latitude>  
0B C1 E2 D4 \<longitude>  

## 3
45 00 00 2D  
FA F1 00 00   
40 11 66 43  
0C 00 00 8B   
0D 00 00 01   
0F A1 0F A1  
00 19 83 1C  

### UDP payload
0D 0F 22 04 11 22 33 44 66  
3A 10 2F 84 \<latitude>  
0B C1 E3 14 \<longitude>  

## 4
45 00 00 2D  
FA F2 00 00   
40 11 66 42  
0C 00 00 8B   
0D 00 00 01   
0F A1 0F A1  
00 19 8F 25  

### UDP payload
0D 0F 22 04 11 22 33 44 66  
3A 10 27 76 \<latitude>  
0B C1 E2 16 \<longitude>  