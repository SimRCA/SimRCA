**Root Cause Analysis (RCA)** has been proven to be a promising method for finding the root cause for failures in cellular networks. By finding the most fundamental reasons for the occurring faults according to signalling information, RCA allows operators to powerfully restore the network condition. Our project enables the classification of faults on the RAN side of 5G.

# Data
Our team has established a long-term relationship with Huawei, the four major Chinese carriers, and other related technology vendors, and has jointly built a set of carrier-grade 4/5G core network real experimental environments. We obtain data from Huawei's 5G commercial system (eliminating sensitive data), which includes uplink and downlink RLC total throughput rate, uplink and downlink MAC total throughput rate, SS-RSRP(Synchronization Signal Reference Signal Received Power), SS-RSRQ(Synchronization Signal Reference Signal Received Quality), base station ID, cell ID, physical cell ID, and so on. Among them, signalling data such as SS-RSRP and SS-RSRQ in the RRC messages can directly reflect the connection status of the UE on the wireless side or the failure situation on the RAN side.

Our published data is the first public 5G dataset for RAN fault detection studies in cellular networks.
![RRC Signaling Message](https://github.com/SimRCA/SimRCA/assets/73945868/8980dbbc-51b8-4279-98c1-c49ab54669e9)
