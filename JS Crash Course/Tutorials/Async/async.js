// sync
// console.log("1. Preheat the oven to 350F.");
// console.log("2. Chop half the chocolate into chunks & melt in microwave.");
// console.log("3. Mix butter & sugar");
// console.log("4. Beat in the eggs and vanilla for 1-2 minutes.");
// console.log("5. Whisk in the melted chocolate.");
// console.log("6. Fold in the other half of chocolate chunks");
// console.log("7. Bake for 20-25 minutes, then let cool completely");
// console.log("8. Slice, serve & enjoy!");

// setTimeout function
//Passes a function and a time as an argument
setTimeout(()=>{"ice cream";}, 4000);

// Chocolate Cake (Callbacks)
function task1(callback){
    setTimeout(() => {
        console.log("1. Preheat the oven to 350F.");
        callback();
    }, 1000);

}
function task2(callback){
    setTimeout(() => {
        console.log("2. Chop half the chocolate into chunks & melt in microwave.");
        callback();
    }, 2000);

}
function task3(callback){
    setTimeout(() => {
        console.log("3. Mix butter & sugar");
        callback();
    }, 1500);

}
function task4(callback){
    setTimeout(() => {
        console.log("4. Beat in the eggs and vanilla for 1-2 minutes.");
        callback();
    }, 3000);

}
function task5(callback){
    setTimeout(() => {
        console.log("5. Whisk in the melted chocolate.");
        callback();
    }, 4000);

}
function task6(callback){
    setTimeout(() => {
        console.log("6. Fold in the other half of chocolate chunks");
        callback();
    }, 3500);

}
function task7(callback){
    setTimeout(() => {
        console.log("7. Bake for 20-25 minutes, then let cool completely");
        callback();
    }, 1800);

}
function task8(callback){
    setTimeout(() => {
        console.log("8. Slice, serve & enjoy!");
        callback();
    }, 500);

}

// Callback Hell
task1 (() => {
    task2(() => {
        task3(() => {
            task4(() => {
                task5(() => {
                    task6(() => {
                        task7(() => {
                            task8(() => {

                            })
                        })
                    })
                })
            })
        })
    })
})

// Promises
//Two attributes resolve (promise went through) and reject (promise rejected)
//Will pend if there's a delay
// const promise = new Promise((resolve, reject) => {
//     const randomNumber = Math.floor(Math.random() * 10);
//     setTimeout(() => {
//         randomNumber < 4 ? resolve ("Well Done! You Guessed Right!") : reject ("Oops! You guessed wrong! Unlucky")
//     }, 2000)
// });
// const promiseTwo = new Promise((resolve, reject) => {
//     const randomNumber = Math.floor(Math.random() * 10);
//     setTimeout(() => {
//         randomNumber < 4 ? resolve ("Well Done! You Guessed Right!") : reject ("Oops! You guessed wrong! Unlucky")
//     }, 2000)
// });
// const promiseThree = new Promise((resolve, reject) => {
//     const randomNumber = Math.floor(Math.random() * 10);
//     setTimeout(() => {
//         randomNumber < 4 ? resolve ("Well Done! You Guessed Right!") : reject ("Oops! You guessed wrong! Unlucky")
//     }, 2000)
// });



// // Promise needs to be consumed to be used
// // Chain promises using .then methods and catch errors with .catch
// // Similar to callback hell
// promise
// .then((value) => {
//     console.log(value)
//     return promiseTwo
// })
// .then((value) =>{
//     console.log(value)
//     return promiseThree
// })
// .catch((error) => {
//     console.log(error)
// })

// const promiseOne = new Promise((resolve, reject) => {
//     setTimeout(() => {         
//         resolve("Promise One Resolved")
//     }, 1500);
// });
// const promiseTwo = new Promise((resolve, reject) => {
//     setTimeout(() => {         
//         reject("Promise Two Rejected")
//     }, 1500);
// });

// // Call the array of promises
// Promise.all([promiseOne,promiseTwo])
// .then((data) => console.log(data[0],data[1]))
// .catch((error) => console.log(error)); 

// Promises / Async-Await

const preHeatOven = () => {
    return new Promise ((resolve, reject) => {
        setTimeout(() => {
            const preHeatOven = true;

            preHeatOven ? resolve("Preheat over to 180deg") : reject("Failed Task One")
        })
    })
}
const addSugarandChocoChips = () => {
    return new Promise ((resolve, reject) => {
        setTimeout(() => {
            const addSugarandChocoChips = true;

            addSugarandChocoChips ? resolve("Place butter and chocolate chips, stir until melted and smooth") : reject("Failed Task")
        })
    })
}
const addFlourCocoaAndSalt = () => {
    return new Promise ((resolve, reject) => {
        setTimeout(() => {
            const addFlourCocoaAndSalt = true;

            addFlourCocoaAndSalt ? resolve("Add flour, cocoa, and salt. Stir until smooth.") : reject("Failed Task")
        })
    })
}
const bakeMixture = () => {
    return new Promise ((resolve, reject) => {
        setTimeout(() => {
            const bakeMixture = true;

            bakeMixture ? resolve("Bake mixture until nice and gooey in the center") : reject("Failed Task")
        })
    })
}

const bakeChocoBrownies = async () => {
    try{
        const taskOne = await preHeatOven();
        console.log(taskOne)
        const taskTwo = await addSugarandChocoChips();
        console.log(taskTwo);
        const taskThree = await addFlourCocoaAndSalt();
        console.log(taskThree);
        const taskFour = await bakeMixture();
        console.log(taskFour);
    
        console.log("Enjoy! Your perfect Chocolate Brownies!")
    } catch(error) {
        console.log(error)
    }
 
}

bakeChocoBrownies();

// Fetch API('<URL>', {})
// To add to the fetch request
// fetch('https://dummyjson.com/products/1', {
//     // Post Request instead of a Fetch Request
//     // methods include POST, PUT, and DELETE
//     method: 'PUT',
//     headers: {
//         'Content-type': 'application/json'
//     },
//     body: JSON.stringify({
//         description: 'Iphone 19',
        
//         price: '1000',
//         rating: '9/10'
//     })
// })
// // Specify these methods for the promise to load the API into the website
// .then(response => console.log(response))
// .then(data => console.log(data))
// .catch(error => console.log(error))

// API Fetch mixed with Async, Try/Catch
const getAllProducts = async () => {
    try{
        const response = await fetch('https://dummyjson.com/products/');
        const json = await response.json();
        console.log(json);        
    } catch (error) {
        console.log(error);
    }        

}

getAllProducts(); //output = products Array with 30 objects

