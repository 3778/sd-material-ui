// @flow

import React from 'react';
import PropTypes from 'prop-types';

import {
  BottomNavigationItem,
  BottomNavigation as MUIBottomNavigation,
} from 'material-ui/BottomNavigation';
import lightBaseTheme from 'material-ui/styles/baseThemes/lightBaseTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import getMuiTheme from 'material-ui/styles/getMuiTheme';

type T_NAV_ITEM = {
  label: string,
  icon: Element | string,
  value: string | number,
  targetId?: string,
  iconClassName?: string,
}
type Props = {
  navItems: Array<T_NAV_ITEM>,

  setProps?: (props: { selectedIndex: number }) => void,
  selectedIndex?: number,
  selectedStyle?: Object,
};
type State = {
  selectedIndex: number,
};

const propTypes = {
  /**
   * The ID used to identify this compnent in Dash callbacks
   */
  id: PropTypes.string.isRequired,

  /** Array of navigation item props to pass to BottomNavigationItem */
  navItems: PropTypes.arrayOf(PropTypes.shape({
    label: PropTypes.string,
    icon: PropTypes.oneOfType([PropTypes.element, PropTypes.string]),
    value: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
    /** ID of component to jump to when this option is selected */
    targetId: PropTypes.string,
    /** Class to apply to the icon span */
    iconClassName: PropTypes.string,
  })).isRequired,

  /** Initial selected index for the BottomNavigation */
  selectedIndex: PropTypes.number,

  /** Style to apply to the selected icon */
  selectedStyle: PropTypes.objectOf(PropTypes.any),

  /**
   * Dash-assigned callback that should be called whenever any of the
   * properties change
   */
  setProps: PropTypes.func.isRequired,
};

/**
 * BottomNavigationItem is an item in a BottomNavigation component
 */
export default class BottomNavigation extends React.Component<Props, State> {
  props: Props;
  state: State;

  static defaultProps = {
    selectedIndex: 0,
    setProps: () => {
    },
    selectedStyle: {},
  };

  constructor(props: Props) {
    super(props);

    this.state = {
      selectedIndex: props.selectedIndex,
    };
  }

  componentWillReceiveProps(nextProps: Props): void {
    if (nextProps.selectedIndex !== this.props.selectedIndex)
      this.setState({selectedIndex: nextProps.selectedIndex});
  }

  buildBottomNavigationItem = (navItem: T_NAV_ITEM, selectedIndex: number) => {
    const {selectedStyle} = this.props;

    let navItemIcon;

    switch (typeof navItem.icon) {
      case 'string':
      case 'number':
      case 'undefined':
        navItemIcon = (
          <span
            style={selectedIndex === this.state.selectedIndex ? selectedStyle : {}}
            className={navItem.iconClassName}
          >
            {navItem.icon}
          </span>);
        break;
      case 'object':
        navItemIcon = navItem.icon;
        break;
      default:
        break;
    }

    return (
      <BottomNavigationItem
        key={navItem.label}
        label={navItem.label}
        icon={navItemIcon}
        onClick={() => {
          this.setState({selectedIndex});

          if (typeof navItem.targetId === 'string') {
            const targetElement = document.getElementById(navItem.targetId);
            targetElement.scrollIntoView();
          }

          if (typeof this.props.setProps === 'function')
            this.props.setProps({selectedIndex});
        }}
      />);
  };

  render() {
    const {id, navItems} = this.props;

    return (
      <div id={id}>
        <MuiThemeProvider muiTheme={getMuiTheme(lightBaseTheme)}>
          <MUIBottomNavigation selectedIndex={this.state.selectedIndex}>
            {
              navItems.map(this.buildBottomNavigationItem)
            }
          </MUIBottomNavigation>
        </MuiThemeProvider>
      </div>);
  }
}

BottomNavigation.propTypes = propTypes;
