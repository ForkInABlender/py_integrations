# Dylan Kenneth Eliot

"""
The php interpreter can be embedded such that it runs via python as a c++ library.


Enjoy knowing your interpreter can run inside an interpreter. 

:)


"""

import ctypes
import sys
from ctypes import c_char_p, c_int, POINTER, c_void_p

# Load PHP library
php_lib = ctypes.CDLL("php-src/libs/libphp.so")

# Set up function signatures
php_lib.php_embed_init.argtypes = [c_int, POINTER(c_char_p)]
php_lib.php_embed_init.restype = c_int

php_lib.zend_eval_string.argtypes = [c_char_p, c_void_p, c_char_p]
php_lib.zend_eval_string.restype = c_int

php_lib.php_embed_shutdown.argtypes = []
php_lib.php_embed_shutdown.restype = None

# Initialize PHP interpreter
argc = 1
argv = (c_char_p * 1)(b"python")
php_lib.php_embed_init(argc, argv)

try:
    # Execute PHP code
    php_code = b"""
    function add($a, $b) {
        return $a + $b;
    }
    
    echo add(5, 7);
    """
    
    # The output will be directed to stdout by default
    result = php_lib.zend_eval_string(php_code, None, b"example")
    
    # Check for errors
    if result == -1:
        print("PHP execution failed")
        
finally:
    # Shut down PHP interpreter
    php_lib.php_embed_shutdown()
