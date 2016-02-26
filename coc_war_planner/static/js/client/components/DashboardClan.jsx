import React, { Component, PropTypes } from 'react';
import DashboardComponent from "./DashboardComponent";
import Clan from "../containers/Clan";

class DashboardClan extends DashboardComponent {
  init() {
    this.props.initClan(this.props.clanTag);
  }
  renderWhenReady() {
    return (
      <Clan />
    )
  }
}
DashboardClan.propTypes = {
  clanTag: PropTypes.string,
  initClan: PropTypes.func.isRequired
};

export default DashboardClan;
