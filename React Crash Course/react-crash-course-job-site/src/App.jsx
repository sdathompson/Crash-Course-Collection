import React from 'react';
import { 
  Route, 
  createBrowserRouter, 
  createRoutesFromElements, 
  RouterProvider } from 'react-router-dom';

import HomePage from './pages/HomePage';
import MainLayout from './layouts/MainLayout';
import JobsPage from './pages/JobsPage';
import JobPage, { jobLoader } from './pages/JobPage';
import NotFoundPage from './pages/NotFoundPage';
import AddJobPage from './pages/AddJobPage';
import EditJobPage from './pages/EditJobPage';

const App = () => {
  // Add New Job
  const addJob = async(newJob) => {
    try {      
      const res = await fetch('/api/jobs', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(newJob),
      });
    } catch (error) {      
      console.log('Error fetching New Job', error);
    }
    return;
  };

  //Delete New Job
  const deleteJob = async(id) => {
    const res = await fetch(`/api/jobs/${id}`, {
      method: 'DELETE',
    });
    return;
  }

  //Edit Job Posting
  const updateJob = async(job) => {
    const res = await fetch(`/api/jobs/${job.id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(job),
    });
    return;
  }

  const router = createBrowserRouter(
      // Create a router with a path from an element
      createRoutesFromElements(
        <Route path='/' element = {< MainLayout/>}>
          <Route index element={<HomePage />} />
          <Route path='/jobs' element={<JobsPage />} />
          <Route path='/jobs/:id' element={<JobPage deleteJob= {deleteJob} />} loader={ jobLoader } />
          <Route path='/edit-job/:id' element={<EditJobPage updateJobSubmit={ updateJob } />} loader={ jobLoader } />
          <Route path='/add-job' element={<AddJobPage addJobSubmit={ addJob }/>} />
          <Route path='*' element={<NotFoundPage />} />
    
        </Route>
      )
    );
  
    return <RouterProvider router={router} />
  
  };
  

export default App



