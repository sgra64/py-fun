try:
    # attempt to import class 'Collection' from the implementation module
    # 'type: ignore' avoids VSCode marking if module is not present
    from .collection_impl import Collection # type: ignore

except ImportError:
    # no implementation module is present, import from the default module
    from .collection import Collection

# import 'main()' function from 'driver.py'
from .driver import main


# restrict exports including non-underscored names
__all__ = ["Collection"]
