import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import Clan from '../components/Clan';
import { addClan, changeClan } from '../actions/clan';

function mapStateToProps(state) {
  const { data } = state.clan;
  return {
    clan: data
  };
}

function mapDispatchToProps(dispatch) {
  return bindActionCreators({ addClan, changeClan }, dispatch);
}

export default connect(mapStateToProps, mapDispatchToProps)(Clan);
