import React from 'react';
import { 
  Route, 
  createBrowserRouter, 
  createRoutesFromElements, 
  RouterProvider } from 'react-router-dom';

import HomePage from './pages/HomePage';

const router = createBrowserRouter(
  // Create a router with a path from an element
  createRoutesFromElements(<Route index element={<HomePage />} />)
)

const App = () => {
  return <RouterProvider router={router} />
};

export default App



