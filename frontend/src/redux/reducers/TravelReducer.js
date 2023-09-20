import * as ActionTypes from "../actions/ActionTypes";

const initialState = {
  travelRecommendDetail: {},
  loader: false,
};

export const TravelReducer = (state = initialState, action) => {
  switch (action.type) {
    case ActionTypes.FETCH_TRAVEL_RECOMMENDATIONS_INIT:
      return { ...state, loader: true };
    case ActionTypes.FETCH_TRAVEL_RECOMMENDATIONS_SUCCESS:
      return {
        ...state,
        loader: false,
        travelRecommendDetail: action.data,
      };
    case ActionTypes.FETCH_TRAVEL_RECOMMENDATIONS_ERROR:
      return { ...state, loader: false };

    default:
      return state;
  }
};
