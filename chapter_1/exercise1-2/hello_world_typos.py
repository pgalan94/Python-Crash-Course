# Can you find the typos generating errors?
# Tip: try running the script on terminal and look for error messages.
#
# Try solving one error at a time, and running the script to see if anything changes.

# Err1:
print "Hello World 1!"

# Err2:
print("Hello World 2!')

# Can you find this last error? Tip: its right after the 'import sys' line"
# Err3:
import sys
syss.stdout.write("Hello World 3!")


#Trivia:
print                                                                  ("""
                          This is not an error.
""")

# explanation for Err3: sys.stdout.write
# https://stackoverflow.com/questions/2570269/output-alternatives-in-python
# See Eli Bendersky's answer.