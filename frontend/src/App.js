import React, { useState } from 'react';
import Login from './login';
import ProductGallery from './ProductGallery';

function App() {
  const [token, setToken] = useState(null);

  return (
    <div className="App">
      {!token ? (
        <Login setToken={setToken} />
      ) : (
        <ProductGallery token={token} />
      )}
    </div>
  );
}

export default App;


