import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../src")

# Global variables
scriptname = ""
pathname = ""
full_path_name = ""

# Manage functions
#############################################################
def initialize():
    scriptname = sys.argv[0]
    pathname = os.path.dirname(sys.argv[0])
    full_path_name = os.path.abspath(pathname)

    print("\n")
    print("==================================================================")
    print('   Executing: ', scriptname)
    print("==================================================================")
    print("\n")

    print("initialize done!\n")
    return

def abort_exe( exit_message ):
    print(exit_message)
    print("Aborting...")
    sys.exit(0)
    return

# Tests
#############################################################
def try_test1():
    print("== try_test1 ===========================================")

# Main
#############################################################
if __name__ == '__main__':
    # Initialize
    ###########################################################
    initialize()

    # Use class
    ###########################################################
    try_test1()

    print("\n")
    print("==================================================================")
    print("   Finish.")
    print("==================================================================")
    print("\n")
