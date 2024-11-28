            // JS in HTML uses a lot of anonymous functions
            document.addEventListener('DOMContentLoaded', function() {                
                document.querySelector('form').addEventListener('submit', function(event) {
                    alert(`Hello, ${document.querySelector('#name').value}`);
                    event.preventDefault();
                });
            });