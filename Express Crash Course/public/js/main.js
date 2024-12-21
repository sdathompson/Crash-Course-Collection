const output = document.querySelector('#output');
const button = document.querySelector('#get-posts-btn');
const form = document.querySelector('#add-post-form');

// Get and show posts
async function showPosts() {
    try {        
        // await fetch from our api
        const res = await fetch('http://localhost:8000/api/posts');
        if (!res.ok) {
            throw new Error('Failed to fetch posts');
        }
        
        // await body of the post (stringified JSON)
        const posts = await res.json();
        output.innerHTML = '';
        
        //iterate through posts array
        posts.forEach((post) => {
            // Create an element for each post
            const postEle = document.createElement('div');
            postEle.textContent = post.title;
            output.appendChild(postEle);
        });
    } catch (error) {
        console.log('Error fetching posts: ', error);
    }
}

// Submit new post
async function addPost(event) {
    // Prevent the post from being added if there's nothing in the field
    event.preventDefault();

    const formData = new FormData(this);
    const title = formData.get('title');

    try {
        // fetch the API with an optional method to POST stringified JSON text 
        const res = await fetch('http://localhost:8000/api/posts', {
            method: 'POST',
            headers: {
                'Content-Type' : 'application/json'
            },
            body: JSON.stringify({title})
        });

        //Null check for post
        if (!res.ok) {
            throw new Error('Failed to add post');
        }

        const newPost = await res.json();

        const postEle = document.createElement('div');
        postEle.textContent = newPost.title;
        output.appendChild(postEle);
        showPosts();
    } catch (error) {
        console.error('Error adding post');
    }
}

// Event listeners: button click to show Posts
button.addEventListener('click', showPosts);
form.addEventListener('submit', addPost);