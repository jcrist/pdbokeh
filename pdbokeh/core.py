from __future__ import absolute_import

import bokeh.plotting as bp
from pandas.api.types import is_datetime64_any_dtype, is_categorical_dtype

from .compatibility import register_series_accessor


DEFAULT_WIDTH = 450
DEFAULT_HEIGHT = 300


@register_series_accessor('bkplot')
class BokehSeriesPlot(object):
    """Make plots of Series using Bokeh.

    Examples
    --------
    >>> series.bkplot.line(...)  # doctest: +SKIP

    Plotting methods can also be accessed by calling the accessor as a method
    with the ``kind`` argument. This is equivalent to calling the accessor
    submethod of the same name.

    >>> series.bkplot(kind='line', ...)  # doctest: +SKIP
    """

    def __init__(self, data):
        self._data = data

    def __call__(self, kind='line', **kwargs):
        try:
            return getattr(self, kind)(**kwargs)
        except AttributeError:
            pass
        raise ValueError("series.bkplot(kind=%r, ...) not valid" % kind)

    def line(self, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT, fig=None,
             **kwds):
        """Line plot for series data.

        Parameters
        ----------
        width : int, optional
            The width of the plot in pixels.
        height : int, optional
            The height of the plot in pixels.
        fig : Figure, optional
            If specified, the line is added to the existing figure.
        **kwds :
            Extra keywords passed to ``line``.

        Examples
        --------

        >>> series.plot.line(color='blue', alpha=0.5)  # doctest: +SKIP

        Returns
        -------
        fig : bokeh.plotting.Figure
        """
        df = self._data.reset_index()

        x, y = df.columns = [str(c) for c in df.columns]

        x_data = df[x]
        y_data = df[y]

        axis_kwargs = {}
        for axis, data in [('x', x_data), ('y', y_data)]:
            if is_datetime64_any_dtype(data.dtype):
                axis_kwargs['%s_axis_type' % axis] = 'datetime'
            elif is_categorical_dtype(data.dtype):
                raise ValueError("Categorical dtype not supported for line")

        source = bp.ColumnDataSource({x: x_data, y: y_data})

        if fig is None:
            fig = bp.Figure(plot_height=height,
                            plot_width=width,
                            **axis_kwargs)

        fig.line(x, y, source=source, **kwds)

        return fig
