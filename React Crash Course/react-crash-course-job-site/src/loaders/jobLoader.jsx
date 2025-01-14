import React from 'react'
import { useParams, useLoaderData } from 'react-router-dom';

const jobLoader = () => {

    const { id } = useParams();
    const job = useLoaderData();

  return console.log(job);
};

const jobLoaders = async({ params }) => {
    const res = await fetch(`/api/jobs/${params.id}`);
    const data = await res.json();
    return data;
};

export { jobLoader as default, jobLoaders };

