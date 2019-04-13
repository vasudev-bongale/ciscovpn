# ciscovpn
A python module to connect to VPN using cisco anyconnect secure mobility client

### Installation

Clone/Download the repository

```bash
$ git clone https://github.com/vasudev-bongale/ciscovpn.git
```

Update the parameters in `ciscovpn.py`

```text

USERNAME - Username for the client connection
VPN_HOST - VPN Server host name
VPN_BIN - The binary path of the VPN client
CONNECT_GROUP - The group number under which you wish to connect, leave it '' if no group selection is required.

CISCO_CLIENT_APP = 'Cisco AnyConnect Secure Mobility Client'

SYS_NAME - Keychain item name which stores the password
ACCOUNT_NAME - The account name in the keychain item
```

Install using pip
```bash
$ pip install .
```

Uninstalling
```bash
$ pip uninstall ciscovpn
```

#### Connecting to VPN
```bash
$ ciscovpn --connect
Connected to VPN - "username"@"vpn_server"

```

#### Disconnecting to VPN
```bash
$ ciscovpn --disconnect
Disconnected from VPN - "username"@"vpn_server"
```