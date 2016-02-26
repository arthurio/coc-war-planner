import {
  INIT_CLAN,
  INIT_CLAN_SUCCESS,
  INIT_CLAN_ERROR,
  ADD_CLAN,
  CHANGE_CLAN
} from '../actions/clan';

function async(state={fetching: true}, action) {
  switch (action.type) {
    case INIT_CLAN_SUCCESS:
      return Object.assign({}, state, {
        fetching: false,
        data: action.clan
      });
    case INIT_CLAN_ERROR:
      return Object.assign({}, state, {
        fetching: false,
        data: {}
      });
    case INIT_CLAN:
      return Object.assign({}, state, {
        fetching: true,
        data: {}
      });
    default:
      return state;
  }
}

function sync(state={data: {}}, action) {
  switch (action.type) {
    case ADD_CLAN:
      return Object.assign({}, state, {
        data: action.clan
      });
    case CHANGE_CLAN:
      return Object.assign({}, state, {
        data: action.clan
      });
    default:
      return state;
  }
}

export default function clan(state, action) {
  console.log
  return Object.assign({}, sync(state, action), async(state, action));
}
