
		
	
import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name="Bloque acumulador",  # Nombre del bloque en GRC
            in_sig=[np.float32],       # Tipo de la señal de entrada
            out_sig=[np.float32]       # Tipo de la señal de salida
        )
        
    def work(self, input_items, output_items):
        x = input_items[0]  # Señal de entrada
        y0 = output_items[0]  # Señal acumulada
        
        # Limitamos la señal de entrada a los primeros 2 elementos
        limited_x = x[:2]
        
        # Calculamos la suma acumulativa de los primeros 2 elementos
        if len(limited_x) >= 0:
            acumulado_limited_x = np.cumsum(limited_x)[-1]  # Solo tomamos el último valor acumulado
        else:
            acumulado_limited_x = 0
        
        # Asignamos el valor acumulado a toda la salida
        y0[:] = acumulado_limited_x
        
        return len(x)

