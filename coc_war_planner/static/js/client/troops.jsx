import React from "react";
import {autobound} from "es7-autobinder";
import Loader from "./loader";
import Troop from "./troop";

class Troops extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      loaded: false,
      troops: []
    };
  }
  componentDidMount() {
    $.get(this.props.source, function(troops) {
      this.setState({
        loaded: true,
        troops: troops
      });
    }.bind(this));
  }
  @autobound
  renderTroops(troop, key) {
    return (
      <Troop key={key} {...troop} />
    );
  }
  render() {
    return (
      <div>
        <h1>Your troops:</h1>
        <Loader loaded={this.state.loaded} left="50px">
          <ul>
            {this.state.troops.map((troop, i) => {
              return this.renderTroops(troop, i);
            })}
          </ul>
        </Loader>
      </div>
    );
  }
}
Troops.propTypes = {
  source: React.PropTypes.string.isRequired
};

module.exports = Troops;

