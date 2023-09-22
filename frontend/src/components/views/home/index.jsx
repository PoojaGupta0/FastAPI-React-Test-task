import React, { useState } from 'react';
import TravelForm from './travelInput'; // Assuming the form component is named TravelForm
import TravelRecommendations from './travelOutput'; // Assuming the recommendations component is named TravelRecommendations
import { useSelector } from 'react-redux';
import '../app/App.css'

const TravelSearch = () => {
  const [travelData, setTravelData] = useState(null);
  const travelRecommendData = useSelector((state) => state.TravelDashboard.travelRecommendDetail);
  const handleTravelData = (data) => {
    setTravelData(data);
  };

  return (
    <div>
      <div className='Travel-wrapper'>
      <h1 className='Travel-title'>Travel Recommendations App</h1>

        <div className='container'>
          <div className='row'>
            <TravelForm onTravelData={handleTravelData} />
            {travelRecommendData && <TravelRecommendations data={travelRecommendData} />}
          </div>
        </div>
      </div>

    </div>
  );
};

export default TravelSearch;