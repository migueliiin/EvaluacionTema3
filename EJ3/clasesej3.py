class Nave:
    def __init__(self,nombre,velocidad,tripulacion,transporte,tripmin,pasajeros):
        self.nombre=nombre
        self.velocidad=velocidad
        self.tripulacion=tripulacion
        self.transporte = transporte
        self.tripmin=tripmin
        self.pasajeros=pasajeros

class HalconMilenario(Nave):
    def __init__(self):
        self.nombre='Halcon Milenario'
        self.velocidad=1050
        self.tripulacion=4
        self.transporte=1000
        self.tripmin=4
        self.pasajeros=4
    
    def __str__(self):
        print('El Halcon Milenario consta de las siguientes caracteristicas:\n'
              f'Velocidad maxima >>> {self.velocidad} km/h\n'
              f'Tripulacion >>> {self.tripulacion} entes\n'
              f'Capacidad de transporte >>> {self.transporte} kg\n')
        
class EstrellaDeLaMuerte:
    def __init__(self):
        self.nave1=Nave('Atleti',1000,3,600,2,5)
        self.nave2=Nave('Atreas',600,6,5000,1,10)
        self.nave3=Nave('Guillermo',750,40,1050,5,200)
        self.nave4=Nave('La Nevera',1100,2,500,6,8)
        self.nave5=Nave('Atiempo',100,10,1000,3,10)
        self.listadonaves=[self.nave1,self.nave2,self.nave3,self.nave4,self.nave5]

    def __str__(self):
        print('La Estrella de la Muerte consta de 4 naves')
        for i in self.listadonaves:
            print(f'La nave {i} consta de los siguiente:\n'
                  f'Velocidad maxima >>> {i.velocidad} km/h\n'
                  f'Tripulacion >>> {i.tripulacion} entes\n'
                  f'Capacidad de transporte >>> {i.transporte} kg\n')       
    
    def printa_nave(self,nav):
        print('El Halcon Milenario consta de las siguientes caracteristicas:\n'
              f'Velocidad maxima >>> {nav.velocidad} km/h\n'
              f'Tripulacion >>> {nav.tripulacion} entes\n'
              f'Capacidad de transporte >>> {nav.transporte} kg\n')