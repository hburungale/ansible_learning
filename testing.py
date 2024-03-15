import os 
import sys
a= os.environ.get('New_variable')

if( a == 20):
    print("same")
else:
    print(" exiting")
    sys.exit(1)   
