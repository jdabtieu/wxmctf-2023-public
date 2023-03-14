Opening the pcap file in Wireshark, it's obvious that it's a USB device.
The problem statement references using MS Paint, where you can draw messages
using a mouse, so it's probably mouse data.

Googling for the format of the data, sites like [OSDev](https://wiki.osdev.org/USB_Human_Interface_Devices)
are able to help: in the useful bytes of the mouse HID data, the first byte is whether it's pressed,
the second byte is the x displacement (signed 8-bit), and the third byte is the y displacement (signed 8-bit).

If you check out the admin folder, there are two solve scripts available: the first one uses tshark on the
pcap directly, and the second one has you extract the HID data first, and then parses it to draw out the image.


