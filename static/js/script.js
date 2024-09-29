/*
rather then creating more elements in html creating 3 arrays and appending images to html file 
to keep code cleaner and easier to read
*/
const images1 = [
    "/static/images/vineyard1.png",
    "/static/images/vineyard2.png",
    "/static/images/vineyard3.png"
];

const images2 = [
    "/static/images/grape1.png",
    "/static/images/grape2.png",
    "/static/images/grape3.png"
];

const images3 = [
    "/static/images/bottle1.png",
    "/static/images/bottle2.png",
    "/static/images/bottle3.png"
];

function createSlideshow(slideshowId, images, interval) {
    const slideshow = document.getElementById(slideshowId);
    let currentSlide = 0;

    images.forEach((src, index) => {
        const slide = document.createElement('div');
        slide.className = 'slide' + (index === 0 ? ' active' : ''); // ternary operator instead of if/else statment 
        const img = document.createElement('img');
        img.src = src;
        img.alt = 'wine';
        slide.appendChild(img);
        slideshow.appendChild(slide);
    });

    const slides = slideshow.querySelectorAll('.slide');

    function showSlide(index) {
        slides[currentSlide].classList.remove('active');
        slides[index].classList.add('active');
        currentSlide = index;
    }

    function nextSlide() {
        let next = (currentSlide + 1) % slides.length;
        showSlide(next);
    }

    setInterval(nextSlide, interval);
}

// calling the functions
createSlideshow('slideshow1', images1, 3000);
createSlideshow('slideshow2', images2, 3100);
createSlideshow('slideshow3', images3, 3200);

/*
here sending post requst to server to add wine to wishlsit with id without refresging the page using json
and changing inner text of button if item added
*/

// when button clicked in html it triggers this 
function addToWishlist(id) {
    fetch(`/add_to_wishlist/${id}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    // if the response was successful converts to json object and updates
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            let btn = document.getElementById(`wishlist-btn-${id}`);
            btn.innerText = "Added to Wishlist";
            btn.disabled = true;
            btn.classList.remove('add-btn');
            btn.classList.add('added-btn');
        }
    })
    .catch(error => console.error('Error:', error));
    // for errors if fetch fails
}