## Weekly Summaries and Highlights

### Week 1: Introduction to Computer Networking

**This week introduces the fundamental concepts of computer networking, focusing on the Internet's architecture and key components.**

*   **What is the Internet?**
    *   A "network of networks" connecting billions of devices worldwide.
    *   Governed by protocols that control sending and receiving messages.
    *   Standardized by organizations like the IETF (Internet Engineering Task Force).

*   **Network Edge:**
    *   **Hosts:** Clients (e.g., laptops, smartphones) and servers (e.g., web servers, email servers) that form the endpoints of communication.
    *   **Access Networks:** Connect hosts to the network core, including technologies like DSL, cable (HFC), fiber (FTTH), and wireless (WiFi, cellular).
    *   **Physical Media:** Transmission media used in networks, including wired (e.g., twisted pair, coaxial cable, fiber optic cable) and wireless (e.g., radio waves).

*   **Network Core:**
    *   **Interconnected Routers:** Forward packets across the Internet.
    *   **Packet Switching:** Data is divided into packets, each routed independently.
    *   **Internet Structure:** Hierarchical structure with Tier-1 ISPs, regional ISPs, and content provider networks.

*   **Protocols:**
    *   Define the format, order, and actions taken for communication between network entities.
    *   Examples: HTTP (Web), SMTP (email), TCP, IP, WiFi.

### Week 2: Network Performance, Layering, and History

**Building on Week 1, this week examines network performance metrics, introduces the concept of layering in network architecture, and provides a historical overview of the Internet.**

*   **Network Performance:**
    *   **Packet Delay:** Time taken for a packet to travel from source to destination, consisting of processing, queuing, transmission, and propagation delays.
    *   **Packet Loss:** Occurs when packets are dropped due to network congestion or buffer overflow.
    *   **Throughput:** Rate at which data is successfully transferred between sender and receiver.

*   **Layering and the Internet Protocol Stack:**
    *   **Layering:** Dividing a complex system into smaller, manageable modules (layers), each with specific functionalities.
    *   **Internet Protocol Stack:** Application, Transport, Network, Link, Physical layers.

        *   **Application Layer:** Supports network applications (e.g., HTTP, SMTP).
        *   **Transport Layer:** Provides logical communication between processes on different hosts (e.g., TCP, UDP).
        *   **Network Layer:** Handles routing of datagrams (e.g., IP).
        *   **Link Layer:** Provides data transfer between neighboring network elements (e.g., Ethernet, WiFi).
        *   **Physical Layer:** Transmits bits over the physical medium.
*   **Encapsulation:** Data is encapsulated with headers at each layer as it travels down the protocol stack.
*   **Internet History:**
    *   Early packet-switching research (1960s).
    *   Development of TCP/IP (1970s).
    *   Growth of the World Wide Web (1990s).
    *   Rise of mobile and content-centric networking (2000s-present).

### Week 3: Application Layer

**This week focuses on the Application layer, exploring the principles of network applications and examining specific protocols such as HTTP and the role of cookies.**

*   **Network Applications:** Software that runs on end systems and communicates over a network, enabling various services like web browsing, email, and file sharing. 

*   **Creating a Network Application:**
    *   Involves writing programs that run on end systems and communicate over a network.
    *   No need to write software for network core devices like routers or switches.

*   **Application Layer Protocols:**
    *   Define the types of messages exchanged, message syntax (format), message semantics (meaning), and rules for communication between processes. 
    *   Examples: HTTP for web, SMTP for email.

*   **Transport Service Requirements:**
    *   Applications have diverse requirements for data loss tolerance, throughput, and time sensitivity.

*   **Internet Transport Protocols:**
    *   **TCP:** Reliable, connection-oriented transport with flow control and congestion control. Used for applications requiring data integrity and ordering.
    *   **UDP:** Unreliable, connectionless transport. Used for applications where speed is more important than reliability (e.g., streaming, online gaming).

*   **Web and HTTP:**
    *   **HTTP:** Application layer protocol for the World Wide Web.
    *   **Client-Server Model:** Web browsers (clients) request web pages (objects) from web servers.
    *   **HTTP Request/Response:** Clients send requests; servers respond with the requested data or status codes.
    *   **Persistent vs. Non-Persistent HTTP:** Persistent HTTP keeps the connection open for multiple requests, improving performance.

*   **Cookies:**
    *   Small pieces of data stored by websites on a user's computer to maintain state and track user activity.

*   **Web Caches (Proxy Servers):**
    *   Intermediary servers that store frequently accessed web content to reduce response time and network traffic.

### Week 4: Email, DNS, and Socket Programming

**This week covers email protocols, the Domain Name System (DNS), and introduces socket programming for building network applications.**

*   **Email:**
    *   **Components:** User agents (email clients), mail servers, and email protocols (SMTP, POP3, IMAP).
    *   **SMTP (Simple Mail Transfer Protocol):** Used for sending emails between servers.
    *   **POP3, IMAP:** Used by email clients to retrieve emails from servers.

*   **DNS (Domain Name System):**
    *   Translates human-readable domain names (e.g., google.com) into numerical IP addresses used by computers.
    *   **Hierarchical Structure:** Root servers, top-level domain (TLD) servers, and authoritative servers.
    *   **DNS Query Process:** Recursive queries (handled by local DNS servers) and iterative queries (client contacts multiple servers directly).

*   **Socket Programming:**
    *   Low-level API (Application Programming Interface) for building network applications. 
    *   Allows processes to communicate over a network using sockets, which act as endpoints for communication. 

### Week 5: Transport Layer: Services and UDP

**This week shifts focus to the Transport layer, covering its services, the UDP protocol, and the principles of reliable data transfer.**

*   **Transport Layer Services:**
    *   Provide logical communication between application processes running on different hosts.
    *   Segmenting application messages and reassembling them at the receiver.
    *   Multiplexing/demultiplexing: Handling data from multiple sockets on a single host.

*   **UDP (User Datagram Protocol):**
    *   Connectionless, unreliable transport protocol. 
    *   No guarantee of data delivery, order, or flow control. 
    *   Offers low overhead and is suitable for applications prioritizing speed over reliability.

*   **UDP Segment Header:**
    *   Source Port, Destination Port, Length, Checksum.

*   **UDP Checksum:**
    *   Used for error detection in UDP segments.

*   **Principles of Reliable Data Transfer:**
    *   Building reliable data transfer mechanisms on top of an unreliable channel (network layer).
    *   Techniques like sequence numbers, acknowledgments (ACKs), timeouts, and retransmissions are used to ensure data integrity and ordering.
    *   **Stop-and-Wait:** Sender sends one packet and waits for acknowledgment before sending the next.
    *   **Pipelining:** Sender sends multiple packets without waiting for individual acknowledgments, improving efficiency.
    *   **Go-Back-N, Selective Repeat:** Mechanisms for handling packet loss and retransmissions in pipelined protocols.

### Week 6: TCP and Congestion Control

**This week delves into TCP, a crucial transport layer protocol, and introduces the concept of congestion control.**

*   **TCP (Transmission Control Protocol):**
    *   Connection-oriented, reliable transport protocol providing a byte-stream service. 
    *   Features include flow control, congestion control, and in-order data delivery.

*   **TCP Segment Structure:**
    *   Headers contain fields for sequence numbers, acknowledgment numbers, flow control (receive window), and more.

*   **TCP Sequence and Acknowledgment Numbers:**
    *   Used to track data segments and ensure reliable, in-order delivery.

*   **TCP Round Trip Time (RTT) and Timeout:**
    *   **RTT:** Time for a segment to travel from sender to receiver and back.
    *   **Timeout:** Used to detect lost segments; calculated based on estimated RTT and its variation.

*   **TCP Retransmission and Cumulative ACKs:**
    *   TCP retransmits lost segments after a timeout.
    *   Cumulative acknowledgments acknowledge all segments received up to a certain point.

*   **TCP Fast Retransmit:**
    *   Retransmits a lost segment before the timer expires upon receiving duplicate acknowledgments.

*   **TCP Flow Control:**
    *   Mechanism to prevent the sender from overwhelming the receiver with data.
    *   The receiver advertises its available buffer space using the receive window (rwnd) field in TCP headers.

*   **TCP Throughput:**
    *   Influenced by factors like window size and round-trip time.

*   **Congestion Control:**
    *   Mechanisms to regulate data flow and prevent network congestion when multiple senders share network resources.
    *   TCP employs congestion control mechanisms to avoid overwhelming the network.

### Week 7: Network Layer: Data Plane

**This week explores the Network Layer's data plane, focusing on router architecture, IP addressing, subnetting, and related concepts.**

*   **Network Layer: Data Plane:**
    *   Handles the forwarding of packets from source to destination.
    *   Key functions include:
        *   **Forwarding:** Moving packets between router interfaces based on forwarding tables.
        *   **Routing:** Determining the best paths for packets (handled by the control plane).

*   **Router Architecture:**
    *   **Input Ports:** Receive packets, perform lookup, and queue packets for switching.
    *   **Switching Fabric:** Connects input and output ports, enabling high-speed packet transfer.
    *   **Output Ports:** Transmit packets onto outgoing links, manage output queues, and schedule packet transmissions.
    *   **Routing Processor:** Executes the routing protocols and maintains routing tables.

*   **IP (Internet Protocol):**
    *   Network layer protocol responsible for addressing and routing datagrams across the Internet.

*   **IP Datagram Format:**
    *   Contains header fields for addressing, fragmentation, time-to-live (TTL), protocol identification, and more.

*   **IP Addressing:**
    *   Each interface on a host or router is assigned a unique IP address.
    *   **Subnetting:** Dividing a network into smaller subnetworks (subnets) using subnet masks.
    *   **CIDR (Classless Inter-Domain Routing):** Allows for more flexible IP address allocation and route aggregation.

*   **DHCP (Dynamic Host Configuration Protocol):**
    *   Dynamically assigns IP addresses to hosts on a network.

*   **NAT (Network Address Translation):**
    *   Allows multiple devices on a private network to share a single public IP address.

*   **IPv6:**
    *   The next-generation Internet Protocol addressing the limitations of IPv4, such as address exhaustion.

### Week 8: Network Address Translation and IPv6

**This week focuses on Network Address Translation (NAT) and IPv6, addressing limitations of IPv4 and introducing the transition between these protocols.**

*   **NAT (Network Address Translation):**

    *   **Purpose:** Conserves public IPv4 addresses by enabling multiple devices on a private network to share a single public IP address.
    *   **Functionality:** NAT router replaces private IP addresses and ports in outgoing packets with its own public IP address and a unique port number, maintaining a translation table for incoming traffic. 

*   **IPv6 (Internet Protocol version 6):**

    *   **Motivation:** Addresses the limitations of IPv4, including IP address exhaustion and the need for a larger address space.
    *   **Key Features:**
        *   128-bit address space, providing a vast number of addresses.
        *   Simplified header format for efficient processing.
        *   Improved security features.
        *   Support for Quality of Service (QoS). 

*   **IPv6 Datagram Format:**

    *   Larger address fields (128-bit source and destination addresses).
    *   Simplified header structure compared to IPv4.
    *   No header checksum, relying on upper-layer protocols for error detection. 

*   **Transitioning from IPv4 to IPv6:**

    *   **Challenges:** Upgrading a vast and complex network like the Internet to a new protocol is a gradual process.
    *   **Tunneling:** Encapsulating IPv6 datagrams within IPv4 datagrams for transmission over IPv4 networks.

### Week 9: Network Layer: Control Plane

**This week examines the Network Layer's control plane, which focuses on routing protocols and determining optimal data paths within and between networks.**

*   **Network Layer: Control Plane:**
    *   Determines how datagrams are routed across networks. 
    *   Responsible for: 
        *   **Routing Protocols:** Algorithms that discover network topology, calculate paths, and populate forwarding tables. 
        *   **Path Selection:** Choosing the best path for data based on factors like cost, distance, and congestion. 

*   **Routing Protocols:** 
    *   **Goals:**  To find efficient and reliable paths for data transmission between networks.
    *   **Path Determination:** Based on factors like cost (e.g., link bandwidth, delay), distance, and congestion.
    *   **Types:**
        *   **Link-State Protocols:** Routers exchange information about the entire network topology (link states) to calculate optimal paths. (e.g., Dijkstra's algorithm)
        *   **Distance-Vector Protocols:** Routers exchange distance vectors (cost to reach destinations) with neighbors and iteratively update routing tables. (e.g., Bellman-Ford algorithm)

*   **Routing Algorithm Classification:**

    *   **Global vs. Decentralized:**
        *   Global algorithms have complete network knowledge, while decentralized algorithms rely on local information exchange.
    *   **Dynamic vs. Static:**
        *   Dynamic algorithms adapt to network changes, while static algorithms use pre-defined routes. 

*   **Comparison of Link-State (LS) and Distance-Vector (DV) Algorithms:**

    *   **Message Complexity:** LS protocols generally have higher message overhead than DV protocols.
    *   **Speed of Convergence:** LS protocols converge faster to optimal routes but may oscillate during convergence.
    *   **Robustness:** LS protocols are more robust to router failures, as errors are localized. DV protocols are more susceptible to routing loops and slow convergence issues (count-to-infinity problem).

Let me know if you need more information on any of the topics covered.
