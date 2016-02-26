export const ADD_CLAN = "ADD_CLAN";
export const CHANGE_CLAN = "CHANGE_CLAN";
export const INIT_CLAN = "INIT_CLAN";
export const INIT_CLAN_SUCCESS = "INIT_CLAN_SUCCESS";
export const INIT_CLAN_ERROR = "INIT_CLAN_ERROR";

export function addClan(clan) {
  return {
    type: ADD_CLAN,
    clan
  }
}

export function changeClan(clan) {
  return {
    type: CHANGE_CLAN,
    clan
  }
}

export function initClan(clanId) {
  if (clanId === undefined) {
    return {
      type: INIT_CLAN_SUCCESS
    }
  }
  return (dispatch) => {
    dispatch({type: INIT_CLAN});
    fetch('/api/clans')
      .then(req => req.json())
      .then((clan) => {
        dispatch({ type: INIT_CLAN_SUCCESS, clan: clan });
      })
      .catch((error) => {
        dispatch({ type: INIT_CLAN_ERROR, error: error });
      });
  };
}
