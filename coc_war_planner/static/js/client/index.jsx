const React = require("react"),
      Troops = require("./troops");

class TroopsDashboard {
  constructor(troops, element) {
    React.render(<Troops troops={troops} />, element);
  }
}

window.TroopsDashboard = TroopsDashboard;
