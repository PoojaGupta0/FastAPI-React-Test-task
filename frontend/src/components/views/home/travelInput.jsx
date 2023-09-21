import React, { useState } from 'react';
import {connect } from 'react-redux';
import { fetchTravelRecommendation } from '../../../redux/actions/TravelAction';
import Select from 'react-select';

const TravelForm = ({ dispatch }) => {
  const [formData, setFormData] = useState({
    country: '',
    season: '',
  });
  const [selectedValue, setSelectedValue] = useState(null);
  const handleSelectChange = (selectedOption) => {
    // Handle the change of the Select component separately
    setFormData({ ...formData, season: selectedOption.value });
  };

  const seasonOptions = [
    { value: "summer", label: "Summer" },
    { value: "Spring", label: "Spring" },
    { value: "fall", label: "Fall" },
    { value: "winter", label: "Winter" }
  ]

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
            pattern="[A-Za-z]+" // Only allows letters (no spaces)
            required
          />
        </div>
        <div>
          <label htmlFor="season">Season:</label>
          <Select
            className='selectStyle'
            id='season'
            name='season'
            value={seasonOptions.find((option) => option.value === formData.season)}
            onChange={handleSelectChange}
            options={seasonOptions}
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
