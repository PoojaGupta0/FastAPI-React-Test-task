import React from 'react';

const TravelRecommendations = ({ data }) => {
  return (
    <div className='Travel-card'>
      <h2 className='Travel-card-title'>Travel Recommendations Result</h2>
      <div className='output-card'>
        <p>
          <strong>Country:</strong> {data.country}
        </p>
        <p>
          <strong>Season:</strong> {data.season}
        </p></div>
      <hr className='divider' />
      <h3 className='Travel-card-title my-3'>Recommendations:</h3>
      <ul className='recomd'>
        {data?.recommendations?.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>

    </div>
  );
};

export default TravelRecommendations;
