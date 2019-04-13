"""
Connect/disconnect to VPN via CISCO AnyConnect Secure Mobility Client
with multiple groups to connect.

Uses keyring to retrieve password from the OSX keychain

Tested on Version: 4.6.03049
Platform: macOS Mojave 10.14.4
"""
import sys
import os
import keyring
import click
import pexpect
import time

USERNAME = ''
VPN_HOST = ''
VPN_BIN = '/opt/cisco/anyconnect/bin/vpn'
CONNECT_GROUP = ''

CISCO_CLIENT_APP = 'Cisco AnyConnect Secure Mobility Client'

SYS_NAME = ''
ACCOUNT_NAME = ''


@click.command()
@click.option('--connect/--disconnect', is_flag=True, required=True,
              default=True, help='Connect/Disconnect VPN')
def main(connect):
    if (USERNAME == '' or
            VPN_HOST == '' or
            VPN_BIN == '' or
            CISCO_CLIENT_APP == '' or
            SYS_NAME == '' or
            ACCOUNT_NAME == ''):
        print("VPN parameters undefined. Aborting")
        sys.exit(1)

    if connect:
        connect_vpn()
    else:
        disconnect_vpn()


def connect_vpn():
    """
    * Spawn the cisco anyconnect vpn client binary
    Supply the arguments to the binary using pexpect
    Shutdown any currently running instance of the VPN client
    before attempting to connect.
    * Open Anyconnect GUI after establishing connection
    """

    shutdown_gui()

    # Delay to wait until disconnection/app is closed
    time.sleep(2)
    child = pexpect.spawn(VPN_BIN + ' -s connect ' + VPN_HOST, encoding='utf-8')
    if CONNECT_GROUP != '':
        child.expect(r'Group: \[.*\]')
        child.sendline(CONNECT_GROUP)
    child.expect(r'Username: \[.*\]')
    child.sendline(USERNAME)
    child.expect('Password:')
    password = keyring.get_password(SYS_NAME, ACCOUNT_NAME)
    child.sendline(password)
    child.expect('  >> state: Connected')
    open_vpn_gui()
    print(f"Connected to VPN - {USERNAME}@{VPN_HOST}")


def disconnect_vpn():
    """
    Disconnect VPN
    Wait for 2 seconds before shutting the down the app
    """
    child = pexpect.spawn(VPN_BIN + ' disconnect')
    child.expect('  >> state: Disconnected')
    time.sleep(2)
    shutdown_gui()
    time.sleep(1)
    print(f"Disconnected from VPN - {USERNAME}@{VPN_HOST}")


def open_vpn_gui():
    """
    Open :var CISCO_CLIENT_APP: app
    """
    os.system(f'open -a "{CISCO_CLIENT_APP}"')


def shutdown_gui():
    """
    Close :var CISCO_CLIENT_APP: app
    """
    os.system(f'osascript -e \'quit app "{CISCO_CLIENT_APP}"\' > /dev/null 2>&1')


if __name__ == "__main__":
    main()
