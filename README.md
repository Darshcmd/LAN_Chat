
````
# 🖧 Python LAN Chat App (Terminal-Based)

A simple LAN-based real-time chat system using Python sockets.  
This project allows multiple users on the same Wi-Fi network to communicate using the terminal — no internet or browser required.

---

## ✨ Features

- Full-duplex messaging using multithreading
- Works across devices on the same local network (LAN)
- Pure Python — no external libraries required
- Real-time message broadcasting
- Minimal, clean terminal interface

---

## 🧠 Computer Networks Concepts Applied

- **TCP/IP (Transport + Network Layers)** — Reliable delivery via TCP sockets
- **OSI Model Layer 4** — Sockets for bi-directional communication
- **Socket Programming** — Bind, listen, accept, connect, send, receive
- **Multithreading** — Full duplex (send/receive simultaneously)
- **Client-Server Architecture** — Centralized communication via a server

---

## 📦 Requirements

- Python 3.x
- Two or more devices connected to the **same Wi-Fi**

---

## 🚀 How to Run

### Step 1: Find Your IP Address (on Server PC)

```bash/terminal
ipconfig      # On Windows
ifconfig      # On Linux/macOS
````

Note the **IPv4 address** (e.g., `192.168.1.5`)

---

### Step 2: Run the Server

On the **main computer (server)**:

```bash
python server.py
```

Output:

```
[SERVER STARTED] Listening on port 8000...
```

---

### Step 3: Update `client.py`

On **all client devices**, edit this line in `client.py`:

```python
SERVER_IP = "192.168.1.5"  # Replace with your server's actual IP
```

---

### Step 4: Run the Client(s)

On each device (same Wi-Fi):

```bash
python client.py
```

You will be prompted to enter a nickname, then you can start chatting!

---

## 🖼️ Terminal Demo

```
Darsh: Hey everyone!
Ritika: Hello Darsh 👋
Raj: Good to see this working!
```

---

## 🛠️ File Structure

```
LANchat/
├── server.py      # Runs the chat server
├── client.py      # Runs the client (chat user)
├── README.md      # You're reading it :)
```

---

## 🧪 Tested On

* Windows 10
* Termux on Android (Python 3)
* Ubuntu 22.04
* Python 3.8+

---

## 📚 Use Cases

* Computer Networks course mini project
* LAN-based messaging without internet
* Terminal chat between multiple systems
* Peer-to-peer communication demo

---

## 📌 Credits

Built with ❤️ by **Darsh Soni and Pritisha Mishra**
For the **Computer Networks] Project**

---
````
