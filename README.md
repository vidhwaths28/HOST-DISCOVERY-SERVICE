# HOST-DISCOVERY-SERVICE
# Host Discovery Service using POX Controller and Mininet

## 📌 Overview

This project implements a **Host Discovery Service** in a Software Defined Networking (SDN) environment using the POX controller and Mininet emulator. The controller dynamically detects hosts in the network by analyzing incoming packets and maintains a mapping of host MAC addresses to switch ports.

---

## 🎯 Objectives

* To understand SDN architecture and controller-based networking
* To implement host discovery using PacketIn events
* To simulate a network using Mininet
* To enable communication between hosts using flow rules

---

## 🧠 Key Concepts

* **SDN (Software Defined Networking)**: Separates control plane and data plane
* **POX Controller**: Python-based SDN controller
* **Mininet**: Network emulator for creating virtual hosts and switches
* **OpenFlow Protocol**: Communication between switch and controller
* **PacketIn Event**: Trigger used for host discovery

---

## ⚙️ Requirements

* Ubuntu (Linux environment / VirtualBox)
* Python 3
* Git
* Mininet
* POX Controller
* Open vSwitch

---

## 🛠️ Installation Steps

### 1. Update system

```bash
sudo apt update
sudo apt upgrade -y
```

### 2. Install dependencies

```bash
sudo apt install git python3 python3-pip openvswitch-switch -y
```

### 3. Install Mininet

```bash
git clone https://github.com/mininet/mininet
cd mininet
sudo ./util/install.sh -a
```

### 4. Install POX Controller

```bash
cd ~
git clone https://github.com/noxrepo/pox
```

---

## 📂 Project Structure

```
pox/
 └── pox/
     └── misc/
         └── host_discovery.py
```

---

## 🚀 Execution Steps

### Terminal 1 (Controller)

```bash
cd ~/pox
python3 pox.py forwarding.l2_learning misc.host_discovery log.level --DEBUG
```

### Terminal 2 (Mininet)

```bash
sudo mn -c
sudo mn --topo single,3 --controller remote,ip=127.0.0.1,port=6633
```

### Test connectivity

```bash
pingall
```

---

## 🔍 Working of the Project

1. A host sends a packet in the network
2. The switch forwards unknown packets to the controller (PacketIn)
3. The controller extracts:

   * Source MAC address
   * Switch ID (DPID)
   * Incoming port
4. The controller stores this information in a MAC table
5. If destination is known → forward directly
6. If unknown → flood the packet

---

## 💻 Sample Code Snippet

```python
mac_to_port[dpid][src] = in_port
```

This line maps a host’s MAC address to a specific switch port, enabling host discovery.

---

## ✅ Output

* Hosts are detected and logged in the controller
* Successful communication between hosts using ping

```
*** Results: 0% dropped
```

---

## ⚠️ Challenges Faced

* Permission issues while editing files
* Controller connection errors
* Packet forwarding not working initially

---

## 🔧 Solutions

* Used `sudo` and changed file ownership
* Ensured controller runs before Mininet
* Added L2 learning module for forwarding

---

## 📊 Applications

* Network monitoring
* Intrusion detection systems
* Dynamic routing
* Data center networking

---

## 📌 Conclusion

This project demonstrates how SDN controllers can dynamically discover hosts and control network traffic. By combining host discovery with forwarding logic, efficient communication is achieved in the network.

---

## 📚 References

* POX Documentation
* Mininet Documentation
* OpenFlow Specification

---
