const React = require("react"),
      Loader = require('react-loader');

class CustomLoader extends Loader {
  render () {
    return (
      <div className="loader-container">
        {super.render()}
      </div>
    );
  }
};

module.exports = CustomLoader;
