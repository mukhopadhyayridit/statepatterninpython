from __future__ import annotations
from abc import ABC, abstractmethod
import time

class Mamma():
    def __init__(self, chickenstate):
        self._chickenstate = chickenstate
        
    def get_state(self):
        return self._chickenstate
    
    def set_state(self, chickenstate):
        self._chickenstate = chickenstate
        
    def startpreparation(self):
        self._chickenstate.wash()
        self._chickenstate.marinate()
        self._chickenstate.cook()
        self._chickenstate.serve()
        

class ChickenState(ABC):
    @abstractmethod
    def wash(self):
        pass
    @abstractmethod
    def marinate(self):
        pass
    @abstractmethod
    def cook(self):
        pass
    @abstractmethod
    def serve(self):
        pass

class UncleanedState(ChickenState):
    def __init__(self, mamma):
        self._mamma = mamma
    def wash(self):
        print("Chicken is getting cleaned. Next state will be cleaned State")
        time.sleep(1)
        self._mamma.set_state(CleanedState(self._mamma))
    def marinate(self):
        pass
    def cook(self):
        pass
    def serve(self):
        pass
    
    
class CleanedState(ChickenState):
    def __init__(self, mamma):
        self._mamma = mamma
    def wash(self):
        pass
        
    def marinate(self):
        print("Chicken is getting marionated. Next state will be MarionatedState")
        time.sleep(1)
        self._mamma.set_state(MarinatedSTate(self._mamma))
    def cook(self):
        pass
    def serve(self):
        pass
    
    
class MarinatedSTate(ChickenState):
    def __init__(self, mamma):
        self._mamma = mamma
    
    def wash(self):
        pass    
    def marinate(self):
        pass
    def cook(self):
        print("Chicken is getting cooked. Next state will be CookedState")
        time.sleep(1)
        self._mamma.set_state(CookedState(self._mamma))
    def serve(self):
        pass
    
class CookedState(ChickenState):
    def __init__(self, mamma):
        self._mamma = mamma
    
    def wash(self):
        pass    
    def marinate(self):
        pass
    def cook(self):
        pass
    def serve(self):
        print("Chicken is ready  Now chicken will be served. This is the last state")
        time.sleep(1)
        print("Guests are saying Thank you...")
        
mamma = Mamma(None)
mamma.set_state(UncleanedState(mamma))
mamma.startpreparation()



                               
              
           
    