import * as ActionTypes from "./ActionTypes";
import { apiCall, handleError } from "../../Utils/Utils";
import Globals from "../../Global";
import { toast } from "react-toastify";
// handle loader when api started to call
export const travelRecommendationInit = () => {
  return {
    type: ActionTypes.FETCH_TRAVEL_RECOMMENDATIONS_INIT
  };
};
//handle success of api
export const travelRecommendationSuccess = val => {
  return {
    type: ActionTypes.FETCH_TRAVEL_RECOMMENDATIONS_SUCCESS,
    data: val
  };
};
// handle api error
export const travelRecommendationError = () => {
  return {
    type: ActionTypes.FETCH_TRAVEL_RECOMMENDATIONS_ERROR
  };
};
/**
 * @author Pooja
 * @param {*} data
 * @use to fetch travel recommendation
 * @returns
 */
export const fetchTravelRecommendation = data => async dispatch => {
  try {
    dispatch(travelRecommendationInit());
    const apiResponse = await apiCall(
      `${Globals.API_ROOT_URL}travel/recomendations?country=${data.country}&season=${data.season}`,
      "GET",
    );
    if (apiResponse !== undefined && apiResponse.status === 200) {
      dispatch(travelRecommendationSuccess(apiResponse.data));
    } else {
      handleError(apiResponse,dispatch) 
      dispatch(travelRecommendationError());
    }
  } catch (error) {
    toast.error(Globals.errorMsg);
    dispatch(travelRecommendationError());
    throw error;
  }
};
