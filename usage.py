import sd_material_ui
import dash
import dash_html_components as html

app = dash.Dash('')

app.scripts.config.serve_locally = True

spacer = html.Div(children=[], style=dict(height=20))

app.layout = html.Div([

    # Test BottomNavigation
    sd_material_ui.BottomNavigation(
        id='input',
        selectedIndex=0,
        selectedStyle={'color': 'blue'},
        navItems=[
            dict(label='test 1', value='val1', icon='1'),
            dict(label='test 2', value='val2', icon='2'),
        ]),
    html.Div(id='output'),

    spacer,

    # Test SDDialog (modal)
    sd_material_ui.SDDialog(
        html.Div(children=[
            html.P('pathname'),
            html.P(id='closer', children='Close window'),
        ]),
        id='output2',
        modal=True,
        open=False),
    html.Div(id='input2', children=[html.P('Share the page (modal)')]),

    spacer,

    # Test SDDialog (non-modal)
    sd_material_ui.SDDialog(
        html.Div(children=[
            html.P('Non-modal dialog'),
        ]),
        id='non-modal-output',
        modal=False,
        open=False),
    html.Div(id='non-modal-input', children=[html.P('Share the page (non-modal)')]),

    spacer,

    # Test SDRaisedButton
    html.Div(children=[
        html.P(id='output4', children=['n_clicks value: '])
    ]),
    html.Div(children=[
        sd_material_ui.SDRaisedButton(id='input4',
                                      label='Use',
                                      primary=True,
                                      buttonStyle=dict(width=50)),
    ], style=dict(backgroundColor='#1D3153')),

    spacer,

    # Test SDFlatButton
    html.Div(children=[
        html.P(id='output5', children=['n_clicks value: '])
    ]),
    sd_material_ui.SDFlatButton(id='input5', label='Click me', backgroundColor='orange'),

    spacer,

    # Test for SDDrawer (docked, secondary)
    sd_material_ui.SDDrawer(id='output6', docked=True, openSecondary=True,
                            children=[html.P(children='Drawer item')]),
    html.Div(id='input6', children=[
        html.P(children='Open or close the drawer (docked)')
    ]),

    spacer,

    # Test for SDDrawer (not docked)
    sd_material_ui.SDDrawer(id='output7', docked=False, open=False, children=[
        html.P(id='close-input7', children='Drawer item')]),
    html.Div(id='input7', children=[
        html.P(children='Open or close the drawer (not docked)')
    ]),

    spacer,

    # Test for SDCheckbox
    html.Div(id='output8', children=[
        html.P('Box is not checked')
    ]),
    sd_material_ui.SDCheckbox(id='input8', label='Check to change the text above.'),

    spacer,

    # Test for SDToggle
    html.Div(children=[
        sd_material_ui.SDToggle(id='input9', label='Johnny?'),
        html.Div(id='output9', children=[
            html.P('Flame off')
        ]),
     ], style=dict(width=150)),

    spacer,

    sd_material_ui.SDRaisedButton(id='input10', label='Marco'),
    html.Div(id='output10', children=['Looking...']),
    sd_material_ui.SDSnackbar(id='snackbar', open=False, message='Polo', action='Reveal'),

    spacer,

    # Test for SDDropDownMenu and SDMenuItem (single selection)
    # sd_material_ui.SDDropDownMenu(id='input10', value=1, children=[
    #     sd_material_ui.SDMenuItem(id='input10-item1', value=1, primaryText='Item 1'),
    #     sd_material_ui.SDMenuItem(id='input10-item2', value=2, primaryText='Item 2'),
    #     sd_material_ui.SDMenuItem(id='input10-item3', value=3, primaryText='Item 3'),
    # ]),
    sd_material_ui.SDDropDownMenu(id='input10', value=1),
    html.Div(id='output10', children=['Selected item appears here.']),
    html.Div(id='output10-checked', children=['What menu items are checked?']),
])


# Callback for BottomNavigation
@app.callback(
    dash.dependencies.Output('output', 'children'),
    [dash.dependencies.Input('input', 'selectedIndex')])
def display_output(value: int):
    return 'You have entered {}'.format(value)


# Callback for SDDialog (modal)
@app.callback(
    dash.dependencies.Output('output2', 'open'),
    [dash.dependencies.Input('input2', 'n_clicks'),
     dash.dependencies.Input('closer', 'n_clicks')],
    [dash.dependencies.State('output2', 'open')])
def show_modal_dialog(modal_click: int, close_button: int, open_state: bool):
    if modal_click and modal_click > 0:
        if not open_state:
            return True
    elif close_button:
        if open_state:
            return False
    else:
        return False


# Callback for SDDialog (non-modal)
@app.callback(
    dash.dependencies.Output('non-modal-output', 'open'),
    [dash.dependencies.Input('non-modal-input', 'n_clicks')],
    [dash.dependencies.State('non-modal-output', 'open')])
def show_non_modal_dialog(non_modal_click: int, open_state: bool):
    if non_modal_click and non_modal_click > 0:
        if not open_state:
            return True
    else:
        return False


# Callback for SDRaisedButton
@app.callback(
    dash.dependencies.Output('output4', 'children'),
    [dash.dependencies.Input('input4', 'n_clicks')])
def display_clicks_raised(n_clicks_raised: int):
    if n_clicks_raised:
        return ['n_clicks value: {}'.format(n_clicks_raised)]
    else:
        return ['n_clicks value: ']


# Callback for SDFlatButton
@app.callback(
    dash.dependencies.Output('output5', 'children'),
    [dash.dependencies.Input('input5', 'n_clicks')])
def display_clicks_flat(n_clicks_flat: int):
    if n_clicks_flat:
        return ['n_clicks value: {}'.format(n_clicks_flat)]
    else:
        return ['n_clicks value: ']


# Callback for SDDrawer (docked, secondary)
@app.callback(
    dash.dependencies.Output('output6', 'open'),
    [dash.dependencies.Input('input6', 'n_clicks')],
    [dash.dependencies.State('output6', 'open')])
def operate_drawer(button_click, drawer_state):
    if button_click:
        return not drawer_state


# Callback for SDDrawer (not docked)
@app.callback(
    dash.dependencies.Output('output7', 'open'),
    [dash.dependencies.Input('input7', 'n_clicks'),
     dash.dependencies.Input('close-input7', 'n_clicks')],
    [dash.dependencies.State('output7', 'open')])
def operate_drawer(button_click, menu_item_click, drawer_state):
    if not drawer_state:
        if button_click:
            return True
    if menu_item_click:
        return False


# Callback for SDCheckbox
@app.callback(
    dash.dependencies.Output('output8', 'children'),
    [dash.dependencies.Input('input8', 'checked')])
def use_clickbox(checkbox):
    if checkbox:
        return ['Box is checked']
    else:
        return ['Box is unchecked']


# Callback for SDToggle
@app.callback(
    dash.dependencies.Output('output9', 'children'),
    [dash.dependencies.Input('input9', 'toggled')])
def use_toggle(switch):
    if switch:
        return ['Flame on!']
    else:
        return ['Flame off']


# Callback for SDSnackbar
@app.callback(
    dash.dependencies.Output('snackbar', 'open'),
    [dash.dependencies.Input('input10', 'n_clicks')])
def open_snackbar(button_click: int):
    if button_click is not None and button_click > 0:
        return True
    else:
        return False


# Callback for SDSnackbar's action
@app.callback(
    dash.dependencies.Output('output10', 'children'),
    [dash.dependencies.Input('snackbar', 'n_clicks')])
def click_snackbar(snackbar_click: str):
    if snackbar_click is not None and snackbar_click > 0:
        return ['Found you!']
    else:
        return ['Looking...']


# Callback for SDDropdownMenu and SDMenuItem
@app.callback(
    dash.dependencies.Output('output10', 'children'),
    [dash.dependencies.Input('input10', 'value')])
def dropdown_callback(value):
    return ['Selection is: {}'.format(value)]


# # Callback for checked SDMenuItem
# @app.callback(
#     dash.dependencies.Output('output10-checked', 'children'),
#     [dash.dependencies.Input('input10-item1', 'checked'),
#      dash.dependencies.Input('input10-item2', 'checked'),
#      dash.dependencies.Input('input10-item3', 'checked')])
# def checked_item_callback(item_1, item_2, item_3):
#     return [
#         html.P('What menu items are checked?'),
#         html.P('Item 1: {}'.format('checked' if item_1 else '')),
#         html.P('Item 2: {}'.format('checked' if item_2 else '')),
#         html.P('Item 3: {}'.format('checked' if item_3 else '')),
#     ]


if __name__ == '__main__':
    app.run_server(debug=True)
