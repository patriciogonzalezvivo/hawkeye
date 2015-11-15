
![](imgs/img.png)

# Raspberry Hawkeye



## Elements

- [Kodak Brownie Hawkeye](http://kenrockwell.com/trips/2010-02-rt-66/contact-sheet.htm) $30-$40
- [RaspberryPi A+](https://www.adafruit.com/products/2266): $24.95
- [RaspberryPi Camera Module](https://www.adafruit.com/products/1367): $29.95
- [USB to TTL](https://www.adafruit.com/products/954): $9.95
- [PowerBoost 1000 Charger](https://www.adafruit.com/products/2465): $19.95
- [Lithium Ion Battery Pack - 3.7V 6600mAh](https://www.adafruit.com/product/353): $29.50

## Printing mounts

## Assembling

## Wiring

## Connecting to the raspberryPi

### Using the [USB to TTL cable](http://www.adafruit.com/products/954)

#### on OSX

Install PL2303 drivers: [el-capitan](https://github.com/patriciogonzalezvivo/hawkeye/raw/master/drivers/PL2303_MacOSX_1_6_0_20151022.zip)

```bash
screen /dev/cu.usbserial 115200  
```

#### on
 Linux

```bash
sudo apt-get install screen
sudo screen /dev/ttyUSB0 115200
```

## Install need software

```bash
cd ~
git clone —recursive https://github.com/patriciogonzalezvivo/hawkeye.git
cd hawkeye/rpitx
./install.sh
```

And edit the main pythons script for transmitting in in a [legal frequency](http://reboot.fcc.gov/spectrumdashboard/searchSpectrum.seam)



## Install autostart ```hawkeye.py``` after every boot

- Open crontab

```bash
crontab -e
```

- Add ```hawkeye.py``` to crontab list to be run every reboot.

```
@reboot /home/pi/hawkeye/./hawkeye.py
```