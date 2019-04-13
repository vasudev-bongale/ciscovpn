# ciscovpn
A python module to connect to VPN using cisco anyconnect secure mobility client

### Installation

Clone/Download the repository

```bash
$ git clone https://github.com/vasudev-bongale/ciscovpn.git
```

Install using pip
```bash
$ pip install .
```

#### Connecting to VPN
```bash
$ ciscovpn --connect
Connected to VPN - <username>@<vpn_server>

```

#### Disconnecting to VPN
```bash
$ ciscovpn --disconnect
Disconnected from VPN - <username>@<vpn_server>
```