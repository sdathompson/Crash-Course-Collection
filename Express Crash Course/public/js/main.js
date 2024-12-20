const output = document.querySelector('#output');
const button = document.querySelector('#get-posts-btn');

// Get and show posts
async function showPosts() {
    try {        
        // await fetch from our api
        const res = await fetch('http://localhost:8000/api/posts');
        if (!res.ok) {
            throw new Error('Failed to fetch posts');
        }
        
        // await body of the post
        const posts = await res.json();
        output.innerHTML = '';
    
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

// Event listeners: button click to show Posts
button.addEventListener('click', showPosts);