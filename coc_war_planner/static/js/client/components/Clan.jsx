import React, { Component, PropTypes } from 'react';
import Loader from "./Loader";

class Clan extends Component {
render() {
    const { addClan, changeClan } = this.props;
    return (
      <ul>
        <li>{this.props.clan.name} - {this.props.clan.level}</li>
      </ul>
    );
  }
}

Clan.propTypes = {
  clan: PropTypes.object,
  addClan: PropTypes.func.isRequired,
  changeClan: PropTypes.func.isRequired
};

export default Clan;
