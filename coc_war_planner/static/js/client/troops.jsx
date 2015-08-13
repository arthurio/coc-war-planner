const React = require("react"),
      autobound = require("es7-autobinder").autobound,
      Troop = require("./troop");

class Troops extends React.Component {
  //constructor(props) {
    //super(props);
    //this.state = {
      //count: props.initialCount
    //};
  //}
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
        <ul>
          {this.props.troops.map((troop, i) => {
            return this.renderTroops(troop, i);
          })}
        </ul>
      </div>
    );
  }
}
Troops.propTypes = {
  troops: React.PropTypes.array
};
Troops.defaultProps = {
  troops: []
};

module.exports = Troops;
