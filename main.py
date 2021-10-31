#!/bin/python

class Temperature:
    def __init__(self):
        from zeus import ZeusSession
        self._session = ZeusSession()

    def save(self):
        from random import randint
        VALUE_MIN = 0.0
        VALUE_MAX = 37.5

        #value = input('>>> Input your temperature (\'C): ')
        #value = float(value)
        #if value < VALUE_MIN or value >= VALUE_MAX:
        #    raise Exception(f'Invalid value: {value}')
        while True:
            value = 36.0 + randint(0,1) + 0.1 * randint(0,9)
            if value <= VALUE_MAX: break


        self._session.save(
            path='/amc/amcDailyTempRegE/save.do',
            pg_name='AmcDailyTempRegE',
            temp=value,
            sympt_1=False,
            sympt_2=False,
            sympt_3=False,
            sympt_4=False,
            sympt_5=False,
            sympt_6=False,
            spc_ctnt='',
            gubun='AA',
        )


if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()

    Temperature().save()
