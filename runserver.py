#!/usr/bin/env python
#-----------------------------------------------------------------------
# runserver.py
# Authors: Wangari Karani & Alfred Ripoll
#-----------------------------------------------------------------------

import sys
import webversion1
import argparse

def main():
    parser = argparse.ArgumentParser(description = "The registrar application")
    parser.add_argument("port", type = int, help = "the port at which the server should listen")
    parser.parse_args()
    
    if len(sys.argv) != 2:
        print('Usage: ' + sys.argv[0] + ' port', file=sys.stderr)
        sys.exit(1)

    try:
        port = int(sys.argv[1])
    except Exception:
        print('Port must be an integer.', file=sys.stderr)
        sys.exit(1)

    try:
        webversion1.app.run(host='0.0.0.0', port=port, debug=True)
    except Exception as ex:
        print(ex, file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
