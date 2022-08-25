

import random

from zmq import EVENT_CLOSE_FAILED 

#https://youtu.be/S1gjYtpCoPs

class flight:
    def __init__(self,_name,_seatname):
        self.name = _name
        self.seatname = {}
        for seat in _seatname:
            self.seatname.update({seat: False})


A = flight('Air Asia', ['W1001', 'M1001', 'L1001', 'W1002', 'M1002', 'L1002',])
B = flight('Vistara', ['W1003', 'M1003', 'L1003', 'W1004', 'M1004', 'L1004',])


def seattype(_type, *args):
    totalseats = []
    seatavail = []
    for plane in args:
        #for seat, status in plane.seatname.items():
        #   if seat[0]==_type and status == False:
        #       seatavail.append(seat)
        #       totalseats.append(seat)
        seatavail = [seats for seats, status in plane.seatname.items() if seats[0]== _type and status==False]
        totalseats.extend(seatavail)
        print(plane.name)
        print(seatavail)
        #print(A)
        seatavail=[]
    return totalseats
        

def seatbooking(_type, _name, _seatnumber, _confirm, *args):
    for flight in args:
        if flight.name == _name:
            f = [flt for flt in flight.seatname.keys() if flight.seatname[flt] == False and flt[0] == _type]
            if _seatnumber in f and _confirm.lower()=="y":
                flight.seatname[_seatnumber]=True
                return _seatnumber


def checkemptyseats(_type, _name, *args):
    for flight in args:
        if flight.name == _name:
            emptyseats=[flt for flt in flight.seatname.keys() if flight.seatname[flt]==False]
            return emptyseats



#Main program,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
if __name__ == '__main__':
    _flts=[A,B]
    
    ch='y'
    while ch.lower()=='y':
        _seattype=input('Enter your seat type (W | M | L ): ')
        try:
            if _seattype not in ('W', 'M', 'L'):
                raise ValueError('Please choose a correct seat type again...')
        except ValueError as er:
            print(er)
        else:
            _seatpresent = seattype(_seattype, A, B)
            try:
                if _seatpresent == []:
                    raise IndexError(f'Sorry no further seats for that flight are available.')
            except IndexError as er:
                print(er)
            else:
                _name= input('Enter the name of the flight: ')
                try:
                    if _name not in (A.name, B.name):
                        raise ValueError('Please choose the correct flight again...')
                except ValueError as er:
                    print(er)
                else:
                    _totalseats=checkemptyseats(_seattype, _name, A, B)
                    try:
                        if _totalseats == []:
                            raise IndexError(
                                f'No seats available for selected seat type in flight: {_name}. Please choose another flight..')
                    except IndexError as er:
                        print(er)
                    else:
                        _seatnum = random.choice(_totalseats)
                        _status = input('Kindly, confirm to proceed (Y | N):')
                        try:
                            if _status.lower()==('n'):
                                raise ValueError('You have chosen to proceed. Please book your seat.')
                            elif _status.lower()not in ('y', 'n'):
                                raise ValueError('Please provide your correct input (Y | N)...')
                        except ValueError as er:
                            print(er)
                        else:
                            _seatstatus=seatbooking(_seattype, _name, _seatnum, _status, A, B)
                            print('Your ticket has been booked with seat number {} in {}'.format(_seatstatus, _name))
                            
            finally:
                ch=input('Do you want to continue ( Y | N ):')
                            
                        
