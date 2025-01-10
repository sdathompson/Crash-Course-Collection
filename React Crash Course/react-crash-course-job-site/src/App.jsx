import { 
  Route, 
  createBrowserRouter, 
  createRoutesFromElements, 
  RouterProvider } from 'react-router-dom';
import React from 'react'
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import HomeCards from './components/HomeCards';
import JobListings from './components/JobListings';
import ViewAllJobs from './components/ViewAllJobs';

const router = createBrowserRouter(
  // Create a router with a path from an element
  createRoutesFromElements(<Route index element={<h1>My App</h1>}/>)
)

const App = () => {
  return <RouterProvider router={router} />
};

export default App



