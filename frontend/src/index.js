import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './components/views/app/App';
import reportWebVitals from './reportWebVitals';
import store from '../src/store';
import { Provider } from 'react-redux'; // Import the Provider
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
<React.StrictMode>
<Provider store={store}>
    <App/>
    </Provider>
  <ToastContainer position="top-right" autoClose={3000} hideProgressBar />
</React.StrictMode>,
)

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
