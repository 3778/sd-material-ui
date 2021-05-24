// @flow

import React, {Component} from 'react';

import MuiSlider from '@material-ui/core/Slider';

import lightBaseTheme from 'material-ui/styles/baseThemes/lightBaseTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import getMuiTheme from 'material-ui/styles/getMuiTheme';

type Props = {
  classes?: {
      root?: string,
      horizontal?: string,
      vertical?: string,
      alternativeLabel?: string,
  },
  /** CSS class name of the root element */
  className?: string,
  /** 'primary' | 'secondary' */
  color?: string,
  /** Dash callback delay in ms - default is 500 ms */
  dashCallbackDelay?: number,
  /** If true, the input element will be disabled. */
  disabled?: boolean,
  /** Dash event handler for click events */
  fireEvent?: () => void,
  /** Dash ID */
  id: string,
  /** The maximum allowed value of the slider. Should not be equal to min */
  max?: number,
  /** The minimum allowed value of the slider. Should not be equal to max */
  min?: number,
  /** The Slider orientation (layout flow direction) */
  orientation?: 'horizontal' | 'vertical',
  /** Dash callback to update props on the server */
  setProps?: (props: {stepIndex?: number}) => void,
  /** The value of the slider */
  value?: number,
  /** Override the inline-style of the root element */
  style?: Object,
};

type State = {
  disabled: boolean,
  value: any,
};

const defaultProps = {
  classes: {},
  className: '',
  color: 'primary',
  dashCallbackDelay: 500,
  disabled: false,
  fireEvent: () => {},
  max: 100,
  min: 0,
  orientation: 'horizontal',
  setProps: () => {},
  value: 0,
  style: {},
};

/** Material UI Slider component */
export default class Slider extends Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.state = {
      disabled: this.props.disabled,
      value: this.props.value,
    };
  }

  handleChange = (event) => {
    this.setState({value: event.target.value});

    if (typeof this.props.setProps === 'function') {
      this.props.setProps({value: event.target.value});
    }
  };

  render() {
    const {
      id,
      className,
      color,
      disabled,
      max,
      min,
      orientation,
      value,
      style,
    } = this.props;
    this.handleChange = this.handleChange.bind(this);
    return (
      <div id={id} className={className} style={style}>
        <MuiThemeProvider muiTheme={getMuiTheme(lightBaseTheme)}>
          <MuiSlider
            id={id}
            className={className}
            color={color}
            disabled={disabled}
            max={max}
            min={min}
            onChange={(event) => {
              this.setState({value: event.target.value});
            }}
            orientation={orientation}
            value={value}
            style={style}
          />
        </MuiThemeProvider>
      </div>
    );
  }
}

Slider.defaultProps = defaultProps;
