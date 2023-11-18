
# WoLAPI 🌐

[![Docker Pulls](https://img.shields.io/docker/pulls/xfrenchgamer73/wolapi.svg?logo=docker)](https://hub.docker.com/r/xfrenchgamer73/wolapi)
[![GitHub last commit](https://img.shields.io/github/last-commit/xFrenchGamer73/WoLAPI?logo=github&logoColor=959DA5)](https://github.com/xFrenchGamer73/WoLAPI/commits/main)
![Wake-on-LAN](https://img.shields.io/badge/WoL-Wake--on--LAN-blue)
![Docker](https://img.shields.io/badge/container-Docker-blue)
![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/xFrenchGamer73/WoLAPI?label=version)
![Python](https://img.shields.io/badge/language-Python-yellowgreen)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/xFrenchGamer73/WoLAPI/blob/main/LICENSE)

WoLAPI is a simple yet powerful Wake-on-LAN API, enabling remote wake-up of devices in local networks. This project is inspired by and based on [Misterbabou's gptwol](https://github.com/Misterbabou/gptwol). It's designed for ease of use and integration into existing systems, offering a straightforward method for network device management.

## 🚀 Features

- Deployable as a Docker container.
- Send Wake-on-LAN packets to devices in a local network.
- Integrate into other applications via API.
- Set the target MAC address via configuration file or URL.
- Two possible configuration choices
## 🐳 Docker Configuration

### Using Host Network Mode 

```yaml
version: '3.8'
services:
  wolapi:
    image: xfrenchgamer73/wolapi:latest
    container_name: wolapi
    network_mode: host
    restart: unless-stopped
    environment:
      - FLASK_ENV=production
      - TARGET_MAC= #ff:ff:ff:ff:ff:ff
      - PORT= #5000
```

### Using Macvlan Network for Advanced Networking 

```yaml
version: '3.8'
services:
  wolapi:
    image: xfrenchgamer73/wolapi:latest
    container_name: wolapi
    networks:
      wolapi:
        ipv4_address: #192.168.1.123
    environment:
      - FLASK_ENV=production
      - PORT= #5000
      - TARGET_MAC= #ff:ff:ff:ff:ff:ff

networks:
  wolapi:
    driver: macvlan
    driver_opts:
      parent: #eth0
    ipam:
      config:
        - subnet: #192.168.1.0/24
```

## 📖 Usage

The WoLAPI can be utilized in the following ways:

1. **If a MAC address is specified in the configuration file:**
   You can wake a device by accessing the API at `http://IP:PORT/wake`. Replace IP and PORT with the actual IP address and port where WoLAPI is running (default: 5000).

2. **If no MAC address is specified in the configuration file:**
   You can directly pass the MAC address in the API call: `http://IP:PORT/wake?mac=ff:ff:ff:ff:ff:ff`. Replace `ff:ff:ff:ff:ff:ff` with the actual MAC address of the device you want to wake.

Note: The MAC address provided via the API is prioritized over the one in the configuration file.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 📧 Contact

Discord : xfrg73

Project Link: [https://github.com/xFrenchGamer73/WoLAPI](https://github.com/xFrenchGamer73/WoLAPI)
