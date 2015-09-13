import React from "react";
import Loader from "./loader";

class Clan extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      loaded: false,
      clan: {}
    };
  }
  componentDidMount() {
    $.get(this.props.source, function(clan) {
      this.setState({
        loaded: true,
        clan: clan
      });
    }.bind(this));
  }
  render() {
    return (
      <div>
        <h1>Your clan:</h1>
        <Loader loaded={this.state.loaded} left="50px">
          <ul>
            <li>{this.state.clan.name} - {this.state.clan.level}</li>
          </ul>
        </Loader>
      </div>
    );
  }
}
Clan.propTypes = {
  source: React.PropTypes.string.isRequired
};

module.exports = Clan;

