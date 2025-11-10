from src.import_module import import_module
# export class 'Expressions' from 'expressions.py' or (if present) from
# 'expressions_impl.py'
mod=import_module(__file__, 'expressions', 'expressions_impl')
Expressions=mod.Expressions

# export 'main()' from local './main.py'
from .main import main
