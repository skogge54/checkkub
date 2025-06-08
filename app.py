import time
import os
from datetime import datetime

def main():
    print("Hello World from Python on GKE!")
    print(f"Current time: {datetime.now()}")
    print(f"Running in pod: {os.environ.get('HOSTNAME', 'unknown')}")
    
    # Keep the container running (optional)
    # Remove this if you want it to run once and exit
    while True:
        print(f"Still running... {datetime.now()}")
        time.sleep(30)

if __name__ == '__main__':
    main()
