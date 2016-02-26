import React, { Component, PropTypes } from 'react';
import Loader from "./Loader";

class DashboardComponent extends Component {
  componentDidMount() {
    this.init();
  }
  render() {
    return (
      <div>
        <h1>{this.props.title}</h1>
        <Loader loaded={this.props.fetching === false} left="50px">
          { this.props.fetching === false && this.renderWhenReady() }
        </Loader>
      </div>
    )
  }
  renderWhenReady() {
    throw "Not implemented";
  }
  init() {
    throw "Not implemented";
  }
}

DashboardComponent.propTypes = {
  source: PropTypes.string.isRequired,
  title: PropTypes.string.isRequired
};

export default DashboardComponent;
