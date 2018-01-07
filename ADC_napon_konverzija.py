
#!/usr/bin/python
 
import spidev
import time
import 16x2_lcd_writer as lcd


#Define Variables
delay = 0.5 #vrednost do sledeceg ucitavanja
ldr_channel = 0 #kanal sa kog se cita

#Kreiranje SPI konekcije
spi = spidev.SpiDev()
spi.open(0, 0)

#Inicijalizacija displeja
#ispis = IspisNaLCD()


#Iscitavanje ADC 
def readadc(adcnum):
    # read SPI data from the MCP3008, 8 channels in total
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data
    
 
while True:
    ldr_value = readadc(ldr_channel)
    #print "---------------------------------------"
    #print("LDR Value: %d" % ldr_value)
    napon = (3.3/1023)*ldr_value
    # metoda za slanje poruke na LCD displej metoda lcd.poruka(str(linija_1), str(linija_2))
    lcd.poruka("Napon [V]:","{0:.2f}".format(napon))
    #ispis.setPisi("Napon:",napon, 0.05)
    time.sleep(delay)
