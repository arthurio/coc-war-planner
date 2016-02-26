import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import DashboardClan from '../components/DashboardClan';
import { initClan } from '../actions/clan';

function mapStateToProps(state) {
  const {fetching} = state.clan;
  return {
    fetching: fetching
  };
}

function mapDispatchToProps(dispatch) {
  return bindActionCreators({ initClan }, dispatch);
}

export default connect(mapStateToProps, mapDispatchToProps)(DashboardClan);
