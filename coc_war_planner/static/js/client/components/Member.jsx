import React from "react";
import {autobound} from "es7-autobinder";
import cookie from "react-cookie";
import {Typeahead} from "react-typeahead";
import Loader from "./Loader";

import "babel/polyfill";

class Member extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      csrftoken: cookie.load('csrftoken'),
      loaded: false,
      clans: [],
      member: {}
    };
  }
  componentDidMount() {
    $.get("/api/clans", function (clans) {
      this.setState({
        clans: clans
      });
    }.bind(this));
    $.get(this.props.source, function(member) {
      this.setState({
        loaded: true,
        member: member
      });
    }.bind(this));
  }

  displayClan(clan, index) {
    return clan.name;
  }

  @autobound
  resetClan(clan) {
    var member = this.state.member;
    member.clan = null;
    this.setState({
      member: member
    });
  }

  @autobound
  updateClan(clan) {
    var member = this.state.member;
    member.clan = clan;
    this.setState({
      member: member
    });
  }

  @autobound
  handleSubmit(e) {
    e.preventDefault();
    $.post(this.props.source, $(e.target).serialize(), function (response) {
      // display success message
      window.alert("Profile saved");
    });
  }

  @autobound
  handleChange(event) {
    this.setState({value: event.target.value});
  }

  @autobound
  renderForm() {
    if (!this.state.loaded) {
      return;
    }
    let linkedClan = Object.assign({}, this.state.member.clan);

    return (
      <form action={this.props.source} method="POST" onSubmit={this.handleSubmit}>
        <input type="hidden" name="csrfmiddlewaretoken" value={this.state.csrftoken} />
        <input type="hidden" name="_method" defaultValue="PUT" />
        <input type="hidden" name="id" value={this.state.member.id} />
        <input type="hidden" name="clan" value={linkedClan.id} />
        <ul>
          <li><label htmlFor="member-name">Name</label><input id="member-name" name="name" defaultValue={this.state.member.name} onChange={this.handleChange} /></li>
          <li><label htmlFor="member-level">Level</label><input id="member-level" name="level" defaultValue={this.state.member.level} onChange={this.handleChange} /></li>
          <li><label htmlFor="member-clan">Clan</label><Typeahead id="member-clan" value={linkedClan.name} filterOption="name" displayOption={this.displayClan} options={this.state.clans} onOptionSelected={this.updateClan} onKeyUp={this.resetClan} onKeyDown={this.resetClan} /></li>
        </ul>
        <button className="btn btn-primary center">Save</button>
      </form>
    );
  }

  render() {
    return (
      <div>
        <Loader loaded={this.state.loaded} left="50px">
          {this.renderForm()}
        </Loader>
      </div>
    );
  }
}
Member.propTypes = {
  source: React.PropTypes.string.isRequired
};

module.exports = Member;


