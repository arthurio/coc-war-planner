const React = require("react"),
      Clan = require("./clan"),
      Member = require("./member"),
      Troops = require("./troops");

class ClanDashboard {
  constructor(source, element) {
    React.render(<Clan source={source} />, element);
  }
}

class TroopsDashboard {
  constructor(source, element) {
    React.render(<Troops source={source} />, element);
  }
}

class MemberProfile {
  constructor(source, element) {
    React.render(<Member source={source} />, element);
  }
}

window.TroopsDashboard = TroopsDashboard;
window.ClanDashboard = ClanDashboard;
window.MemberProfile = MemberProfile;
