import axios from 'axios';
import { toast } from 'react-toastify';
import Global from '../Global';

/**
 * @author Pooja
 * @use handle axios api call
 * @param {*} url name of the api
 * @param {*} method GET, POST, PUT, DELETE, etc
 * @param {*} data pass data if required to pass in api call
 * @returns
 */
export async function apiCall(url = "", method = "", data = {}) {
  var apiDetail = {
    method: method.toUpperCase(), // *GET, POST, PUT, DELETE, etc.
    url,
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
      "Access-Control-Allow-Origin": "*",
    },
  };
  if (Object.keys(data).length > 0) {
    let objToAdd = {
      data: JSON.stringify(data), // body data type must match "Content-Type" header
    };
    Object.assign(apiDetail, objToAdd);
  }
  try {
    const response = await axios(apiDetail);
    return await response;
  } catch (err) {
      return err?.response;
  }
}

export const handleError = (apiResponse,dispatch) => {
    if (apiResponse) {
      if(apiResponse.status === 500){
        return toast.error(Global.errorMsg);
      }
      else{
        return toast.error(apiResponse.data.detail)
      }
    }
}
