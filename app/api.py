from flask import Flask, request
import socket
import struct
import os

# Initialize the Flask application
app = Flask(__name__)

def send_wol_packet(mac_address):
    """
    Send a Wake-on-LAN packet to the specified MAC address.

    Args:
        mac_address (str): The MAC address to send the Wake-on-LAN packet to.
    """

    # Convert the MAC address to a binary format
    packed_mac = struct.pack('!6B', *[int(x, 16) for x in mac_address.split(':')])

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Enable broadcast mode on the socket
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Send the Wake-on-LAN packet
    sock.sendto(b'\xff' * 6 + packed_mac * 16, ('<broadcast>', 9))

    # Close the socket
    sock.close()


@app.route('/wake', methods=['GET'])
def wake_device():
    """
    Flask endpoint to trigger the sending of the Wake-on-LAN packet.
    Retrieves the MAC address either from the URL parameter or the environment variable.

    Returns:
        str: Confirmation message including the targeted MAC address.
    """

    # Get the MAC address from the URL parameter first
    target_mac = request.args.get('mac')

    # If the MAC address is not provided in the URL, fetch it from the environment variable
    if not target_mac:
        target_mac = os.getenv('TARGET_MAC')

    # If no MAC address is provided at all, return an error
    if not target_mac:
        return "No MAC address provided.", 400

    # Send the Wake-on-LAN packet
    send_wol_packet(target_mac)

    # Return a confirmation response
    return f"Wake-on-LAN packet sent to {target_mac}"
   
# Run the Flask app if this is the main program
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000)) #default 5000
    app.run(host='0.0.0.0', port=port)


<<<<<<< HEAD
=======

>>>>>>> 283f25fdd9e760018fa41a4346f554a8e4394ec9
#1.0
