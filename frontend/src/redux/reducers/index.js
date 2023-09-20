import { combineReducers } from 'redux';
import { TravelReducer } from './TravelReducer';

const appReducer = combineReducers({
    TravelDashboard: TravelReducer,
});
const rootReducer = (state, action) => {
    let innerState = state;
    return appReducer(innerState, action);
};

export default rootReducer;