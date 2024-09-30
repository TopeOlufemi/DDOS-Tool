<h3>Understanding DDOS</h3>
<p>A distributed denial-of -service attack is a malicious attempt to disrupt the normal functioning of a targeted server, service or network by overwhelming it with a flood of internet traffic.
<h4>Types of DDos Attacks!
</h4> 
<li>Volume-based attacks : these include UDP floods and ICMP floods, which aim to consume bandwidth.
  <strong>
Note:  UDP (User Datagram Protocol) floods attack is done when the attacker sends a large number of UDP packets to random ports on a target server. ICMP (Internet Control Message Protocol) floods involve sending a high volume 
Of ICMP Echo Request packets also known as ping requests to the target.</strong>
</li>
<li>
  	 Protocol Attacks : These exploit weakness in network protocols, SYN floods , which consume server resources.
    <strong> Note: SYN floods is the type of attack that exploits TCP handshake. </strong>
</li>
<li>Application layer attacks : these focus on specific applications, such as HTTP floods, targeting web servers to overwhelm them.
</li>

# DDOS Tool

## Overview
The DDOS Tool is a Python-based application designed to simulate Distributed Denial of Service (DDoS) attacks for educational purposes. It helps users understand how DDoS attacks work and the importance of network security.

## Prerequisites
Before running the code, ensure you have the following installed:
- Python 3.x
- pip (Python package installer)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/TopeOlufemi/DDOS-Tool.git
   ```
2. Navigate to the project directory:
   ```bash
   cd DDOS-Tool
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Run on Linux
   ```bash
    sudo python3 DDOS_Tool.py
   ```

