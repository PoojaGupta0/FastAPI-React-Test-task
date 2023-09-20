import React, { useState } from 'react';
import { useDispatch, connect } from 'react-redux';
import { fetchTravelRecommendation } from '../../../redux/actions/TravelAction';

const TravelForm = ({ dispatch }) => {
  const [formData, setFormData] = useState({
    country: '',
    season: '',
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const { country, season } = formData;
    dispatch(fetchTravelRecommendation({ country, season }));
  };

  return (
      <div className='Travel-card'>
      <h2 className='Travel-card-title'>Travel Recommendations</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="country">Country:</label>
          <input
            type="text"
            id="country"
            name="country"
            value={formData.country}
            onChange={handleInputChange}
            placeholder="Enter country..."
            required
          />
        </div>
        <div>
          <label htmlFor="season">Season:</label>
          <input
            type="text"
            id="season"
            name="season"
            value={formData.season}
            onChange={handleInputChange}
            placeholder="Enter season..."
            required
          />
        </div>
        <div>
          <button type="submit" className='getbtn'>Get Recommendations</button>
        </div>
      </form>
      </div>
      
  );
};

export default connect()(TravelForm);
