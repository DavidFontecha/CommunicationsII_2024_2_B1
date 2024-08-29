import numpy as np
from gnuradio import gr

class DifferentiatorBlock(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name="DifferentiatorBlock",  # Nombre que aparecerá en GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self._prev_cumsum = 0  # Variable para almacenar la suma acumulativa de la iteración anterior

    def work(self, input_items, output_items):
        x = input_items[0]  # Señal de entrada
        y0 = output_items[0]  # Señal diferenciada
        
        # Limitar la entrada a los primeros 3 datos
        X_LIMITED = x[:3]
        
        # Calcular la suma acumulativa de los datos limitados
        cumsum = np.cumsum(X_LIMITED)
        
        # Calcular la diferencia entre la suma acumulativa actual y la suma acumulativa anterior
        diff = cumsum - self._prev_cumsum
        
        # Actualizar el valor acumulado previo con la última suma acumulativa
        self._prev_cumsum = cumsum[-1] if len(cumsum) > 0 else 0
        
        # Ajustar la salida para que coincida con la longitud de los datos limitados
        y0[:len(diff)] = diff
        
        return len(output_items[0])

