import math
import ystockquote
import googlefinance


def scalp():

    p = float(raw_input("Enter current price: "))
        

    iv = float(raw_input("Implied Volatility(decimal): "))

    dte = int(raw_input("Days until Expiration: "))
    
        
    x = float(dte)/365

    root = math.sqrt(x)

    a = p * iv * root
    q = a + p
    r = p - a

    print "Current expected move: " + format(a,'.2f')

    print "Price range:", format(r, '.2f'), format(q, '.2f')

    print "80% probability of exeeding: " + format(a * .25, '.2f')

          
    scalp()         
   
        
            

scalp()
  
