import numpy as np
from gnuradio import gr
class blk (gr. sync_block ):
	def __init__ ( self ) : # only default arguments here
		gr. sync_block . __init__ (
			self ,
			name ="Bloque acumulador", # will show up in GRC
			in_sig =[ np. float32 ],
			out_sig =[ np. float32 ]
		)
		
	def work (self , input_items , output_items ):
		x = input_items [0] # Senial de entrada .
		y0 = output_items [0] # Senial acumulada

		X_LIMITED = x[:3]	
		
		y0 [:3] = np.cumsum(X_LIMITED)
		
		return len(y0)

