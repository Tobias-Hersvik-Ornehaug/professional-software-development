#Disclaimer: Should not be used for cryptography!
class randomNumberGenerator:
    
    def __init__( self, amount = 0, minRange = 0, maxRange = 0 ):
        
        try:
            if ( maxRange - minRange ) >= amount:
                self.amount   = int( amount )
                self.minRange = int( minRange )
                self.maxRange = int( maxRange )
                
            else:
                raise TypeError( 'Invalid Type' )
                raise ValueError( 'Invalid Amount or Range' )
        
        except ValueError:
            print('ValueError: Range has to be LARGER than amount!')
        
        except TypeError:
            print('TypeError: Class values has to be of type integer!')
        
    def generateRandomNumberList( self ):
        from random import sample
        randomNumbersList = sample( range( self.minRange, self.maxRange ), self.amount )
        
        return randomNumbersList
