try:
    # attempt to import class 'recursion' from the implementation module
    # 'type: ignore' avoids VSCode marking if module is not present
    from .recursion_impl import Recursion # type: ignore

except ImportError:
    # no implementation module is present, import from the default module
    from .recursion import Recursion

# import 'main()' function from 'driver.py'
from .driver import main


# restrict exports including non-underscored names
__all__ = ["Recursion"]
