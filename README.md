# Li-Fi

Repository for a R&D project based on the principles of Li-FI for communication and sharing of data between multiple devices using visible light at SRA, VJTI

## Note: 

All the material posted here (datasheets, books and research papers) are properties of the respective authors, is solely for sharing and informative purposes.

## Flow:

![Flow of the Hardware](https://github.com/laukik-hase/Li-Fi/blob/master/References/Flow.jpg)

## Tasks accomplished:
1. Transfer of text (.txt), image (.png/.jpeg) and .pdf files from one laptop to another, using the prototype as shown, which uses the basic 3V, 20mA LED and simple IR photodiode 
(Range: 5 cm; Speed: 3600 baud)

2. Successful testing of the BPW21R photodiode, for faster response and better range
 (Range: 35 cm; Speed: 19200 baud)
 
3. Designing of analog filters for reducing the effect of ambient light and AC noise and increasing the range of communication (to be implemented)

4. Designing a simple protocol using UART as a framework for efficient and error-free transmission (to be tested)

## Future goals:
1. Implementation of a Master LED (240V, 50 Hz AC) for the transmission side

2. Implementation of the analog filters (namely, High-Pass and Notch) for noise-reduction

3. Creating a robust protocol for the error-free data transmission and receiving; exploring the scope of socket programming and TCP/IP for LiFi

4. Maximizing the speed of communication by implementing faster Op-Amps, LEDs and PDs and replacing the CP2102 module with a faster and reliable alternative

