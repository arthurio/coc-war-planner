import React from "react";
import Loader from "react-loader";

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
