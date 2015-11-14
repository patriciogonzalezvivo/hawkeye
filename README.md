
![](imgs/img.png)

# Raspberry Hawkeye

[Kodak Brownie Hawkeye](http://kenrockwell.com/trips/2010-02-rt-66/contact-sheet.htm)

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