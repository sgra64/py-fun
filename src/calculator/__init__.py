try:
    # attempt to import class 'Calculator' from the implementation module
    from .calculator_impl import Calculator

except ImportError:
    # no implementation module is present, import from the default module
    from .calculator import Calculator

# import 'main()' function from 'driver.py'
from .driver import main


# restrict exports including non-underscored names
__all__ = ["Calculator"]
