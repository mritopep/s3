from src.skull import SkullStripper
import src.helpers as utils
import os
import time

if __name__ == '__main__':

	from sys import argv
	myargs = utils.getopts(argv)

	want_tissues = False

	if '-i' in myargs: 
		input_path = myargs['-i']
	        output_path = os.path.dirname(os.path.abspath(input_path))

	if '-o' in myargs:
		output_path = myargs['-o']
                output_path = os.path.abspath(output_path)
   	
	if '-t' in myargs:
		want_tissues = True

	if not os.path.exists(output_path):
                print("The selected output folder doesn't exist, so I am making it \n")
		os.makedirs(output_path)
   
        start = time.time()
	skull_stripper = SkullStripper(input_path, output_path, want_tissues)
	skull_stripper.strip_skull()
        print 'Done (' + str((time.time() - start) / 60.) + ' min)'