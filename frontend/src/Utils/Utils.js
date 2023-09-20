import axios from 'axios';
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
    console.log(err.response, "Error while calling api");
    if (
      err.response !== undefined && err.response.status === 401
    ) {
      // localStorage.removeItem("auth_token");
      // history.push("/login");


    }
      return err?.response;
  }
}
