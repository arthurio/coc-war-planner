import React from "react";
import { render } from 'react-dom';
import { Provider } from 'react-redux';
import DashboardClan from "./containers/DashboardClan";
import Member from "./components/Member";
import Troops from "./components/Troops";
import configureStore from './store/configureStore';

const store = configureStore();

class DashboardClanPublic {
  constructor(element, clanTag) {
    render(<Provider store={store}><DashboardClan clanId={clanId} /></Provider>, element);
  }
}

// class TroopsDashboard {
//   constructor(source, element) {
//     render(<Troops source={source} />, element);
//   }
// }

// class MemberProfile {
//   constructor(source, element) {
//     render(<Member source={source} />, element);
//   }
// }

// window.TroopsDashboard = TroopsDashboard;
window.DashboardClan = DashboardClanPublic;
// window.MemberProfile = MemberProfile;

if (process.env.NODE_ENV !== 'production') {
  const showDevTools = require('./showDevTools');
  showDevTools(store);
}
