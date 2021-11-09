class randomNumberGenerator:
    
    def __init__( self, amount = 0, minRange = 0, maxRange = 0 ):
        
        try:
            if ( maxRange - minRange ) >= amount:
                self.amount   = int( amount )
                self.minRange = int( minRange )
                self.maxRange = int( maxRange )
                
            else:
                raise TypeError( 'Invalid type' )
                raise ValueError( 'Invalid amount or range' )
        
        except ValueError:
            print('Range has to be bigger than the amount!')
        
        except TypeError:
            print('Class only accept integer type!')
        
    def get_randomNumber( self ):
        from random import sample
        randomNumbersList = sample( range( self.minRange, self.maxRange ), self.amount )
        
        return randomNumbersList
