const React = require("react");

class Troop extends React.Component {
  render() {
    return (
      <li>{this.props.troop.name} - {this.props.troop_level.level}</li>
    );
  }
}
Troop.propTypes = {
  troop: React.PropTypes.object.isRequired,
  troop_level: React.PropTypes.object.isRequired
};

module.exports = Troop;
