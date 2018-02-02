from __future__ import absolute_import

__all__ = ('register_dataframe_accessor', 'register_series_accessor')

try:
    from pandas.api.extensions import (register_dataframe_accessor,
                                       register_series_accessor)
except ImportError:
    import pandas as pd
    try:
        from pandas.core.accessor import AccessorProperty
    except ImportError:
        from pandas.core.base import AccessorProperty

    def _make_register_function(pd_cls):
        def _register(name):
            def _(cls):
                setattr(pd_cls, name, AccessorProperty(cls, cls))
                return cls
            return _
        return _register

    register_dataframe_accessor = _make_register_function(pd.DataFrame)
    register_series_accessor = _make_register_function(pd.Series)
