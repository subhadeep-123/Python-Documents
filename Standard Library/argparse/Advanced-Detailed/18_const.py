"""
The const argument of add_arguments() is used to hold connstant values that are not read from the command line but are required for the 
various ArguemntParser actions. The two common uses of it are:

1>
When add_arguemt() is called with action='store_const' or action='append_const'. These actions add the consts value to one of the attributes
of the object returned by parse_args()
2>
When add_argument() is called with option strings (like -f or --foo) and nargs='?'. T
his creates an optional argument that can be followed by zero or one command-line arguments.
When parsing the command line, if the option string is encountered with no command-line argument following it,
the value of const will be assumed instead. 
"""
