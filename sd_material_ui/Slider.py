# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Slider(Component):
    """A Slider component.
Material UI Slider component

Keyword arguments:

- id (string; required):
    Dash ID.

- className (string; default ''):
    CSS class name of the root element.

- classes (dict; optional)

    `classes` is a dict with keys:

    - root (string; optional)

    - horizontal (string; optional)

    - vertical (string; optional)

    - alternativeLabel (string; optional)

- color (string; default 'primary'):
    'primary' | 'secondary'.

- dashCallbackDelay (number; default 500):
    Dash callback delay in ms - default is 500 ms.

- disabled (boolean; default False):
    If True, the input element will be disabled.

- max (number; default 100):
    The maximum allowed value of the slider. Should not be equal to
    min.

- min (number; default 0):
    The minimum allowed value of the slider. Should not be equal to
    max.

- orientation (default 'horizontal'):
    The Slider orientation (layout flow direction).

- style (dict; optional):
    Override the inline-style of the root element.

- value (number; default 0):
    The value of the slider."""
    @_explicitize_args
    def __init__(self, classes=Component.UNDEFINED, className=Component.UNDEFINED, color=Component.UNDEFINED, dashCallbackDelay=Component.UNDEFINED, disabled=Component.UNDEFINED, fireEvent=Component.UNDEFINED, id=Component.REQUIRED, max=Component.UNDEFINED, min=Component.UNDEFINED, orientation=Component.UNDEFINED, value=Component.UNDEFINED, style=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'classes', 'color', 'dashCallbackDelay', 'disabled', 'max', 'min', 'orientation', 'style', 'value']
        self._type = 'Slider'
        self._namespace = 'sd_material_ui'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'classes', 'color', 'dashCallbackDelay', 'disabled', 'max', 'min', 'orientation', 'style', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in ['id']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Slider, self).__init__(**args)
