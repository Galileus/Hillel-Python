class Supply(object):
    def __init__(self):
        self.sup_stat = False
        self.power = 0
        self.pwr1 = 0

    def check(self,volt):
        if volt > 0:
            self.power = volt
        if self.power < 250 and self.power > 220:
            self.sup_stat = True

        return self.sup_stat

    def work(self):
        if self.sup_stat == True:
            self.pwr1 = 12
        return self.pwr1


class HDD(object):
    def __init__(self):
        self.hdd_stat = False

    def check(self, supply):
        if supply.work() == 12:
            self.hdd_stat = True

        return self.hdd_stat

class BIOS(object):
    def __init__(self):
        self.state = False

    def error(self,msg):
        print(msg)

    def check_power(self, supply, volt):
        if supply.check(volt) == True:
            self.state = True
        else:
            self.error('Power problem')
        return self.state

    def check_hdd(self, hdd, supply):
        if hdd.check(supply) == True:
            self.state = True
        else:
            self.error('HDD problem')
        return self.state



class PC(object):
    def __init__(self):
        self.supply = Supply()
        self.hdd = HDD()
        self.bios = BIOS()

    def on(self,volt):
        if self.bios.check_power(self.supply,volt) == True:
            print('mother - ok')
        if self.bios.check_hdd(self.hdd, self.supply) == True:
            print('hdd - ok')

            print('pc is working')


pc = PC()

pc.on(220)



