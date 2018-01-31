from math import floor

'''
A simple class that converts decimal to rixits and vice versa,
The encoding will shorten the length of the string representation of a long integer
'''

class Base64Rixits:
    def __init__(self):
    	self.rixits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/'  
        
    def fromDec(self,dec):      
        try:
            val = int(dec)
        except ValueError:
            raise ValueError('Expect an integer only.')
        if val < 0:
            raise ValueError('Expect an positive integer only.')
        residual = floor(val)
        result = ''
        while True:
            rixit = residual % 64
            result = self.rixits[rixit] + result;
            residual = floor(residual / 64);
            if residual == 0 :
                break
        return result

    def toDec(self,rixits):
        result = 0;
        try:
            for e in rixits:
                result = (result * 64) + self.rixits.index(e);
        except:
            raise ValueError(str(rixits) + ' is not a valid rixits.')
        return result;

if __name__ == "__main__":
    base64 = Base64Rixits()
    print(base64.fromDec('13811019878'))
    print(base64.toDec('CtCt1c'))
            